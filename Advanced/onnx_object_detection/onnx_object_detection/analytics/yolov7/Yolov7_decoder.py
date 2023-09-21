#!/usr/bin/env python
# encoding: utf-8
# Copyright © 2020, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# The module is copy-paste from yolov5 project

import math
import numpy as np


class Decoder:
    def __init__(self, output_decoder_parameters, inputs_parameters):
        self.decoder_params = output_decoder_parameters
        self.input_image_size = inputs_parameters['input_image_size']
        if 'detection_threshold' in self.decoder_params.keys():
            self.confidenceThresh = self.decoder_params['detection_threshold']
        else:
            self.confidenceThresh = 0.4

    def decode(self, inference_result, image_shape, is_video=False):
        scale = min(self.input_image_size[0] / image_shape[0], self.input_image_size[1] / image_shape[1])
        #Provide real image size excluding letterbox stripes
        adj_input_image_size = [(image_shape[0] * scale), (image_shape[1] * scale)]
        tot_area = adj_input_image_size[0] * adj_input_image_size[1]

        return self.decodeYoloV7Output(inference_result[0][0], tot_area, adj_input_image_size)

    def decodeYoloV7Output(self, boxes, tot_area, adj_input_image_size):
        mask1 = boxes[:, 2] * boxes[:, 3] / tot_area <= 0.6
        boxes = boxes[mask1]
        if len(boxes) > 0:
            mask2 = boxes[:, 4] > self.confidenceThresh
            boxes = boxes[mask2]
        if boxes is not None and len(boxes) > 0:
            boxes = np.concatenate([boxes[:, :4], boxes[:, 4:]], axis=-1)
            if len(boxes) > 1:
                keep =self.non_max_suppression_fast(boxes[:, :4],self.decoder_params['iou_threshold'])
                boxes = boxes[keep]
            boxes[:, :4] = np.round(boxes[:, :4], 0)

            # boxes = boxes * (1 / scale[0])
            out_boxes = boxes[:, :4]
            out_scores = boxes[:, 4]
            out_classes = np.argmax(boxes[:, 5:], -1).astype(np.int32)

            #Adjust the coordinates of shorter side of image/frame to remove letterbox resizing top stripe
            if adj_input_image_size[1] > adj_input_image_size[0]:
                out_boxes[:, 1] -= (self.input_image_size[0] - adj_input_image_size[0])/2
            elif adj_input_image_size[1] < adj_input_image_size[0]:
                out_boxes[:, 0] -= (self.input_image_size[1] - adj_input_image_size[1]) / 2

            # make image coordinate size independent by dividing all content of box array for current image size declared
            out_boxes[:, 0] /= adj_input_image_size[1] #x-center
            out_boxes[:, 1] /= adj_input_image_size[0] #y-center
            out_boxes[:, 2] /= adj_input_image_size[1] #width
            out_boxes[:, 3] /= adj_input_image_size[0] #height

            return out_boxes, out_classes, out_scores
        else:
            out_boxes = np.empty((0, 4), float)
            out_classes = np.asarray([], float)
            out_scores = np.asarray([])
            return out_boxes, out_classes, out_scores

    def non_max_suppression_fast(self, boxes, overlapThresh):
        # if there are no boxes, return an empty list
        if len(boxes) == 0:
            return []

        # if the bounding boxes integers, convert them to floats --
        # this is important since we'll be doing a bunch of divisions
        if boxes.dtype.kind == "i":
            boxes = boxes.astype("float")

        # initialize the list of picked indexes
        pick = []

        x = boxes[:, 0]
        y = boxes[:, 1]
        w = boxes[:, 2]
        h = boxes[:, 3]

        x1 = (x - w / 2)
        x2 = (x + w / 2)
        y1 = (y - h / 2)
        y2 = (y + h / 2)

        # compute the area of the bounding boxes and sort the bounding
        # boxes by the bottom-right y-coordinate of the bounding box
        area = (x2 - x1 + 1) * (y2 - y1 + 1)
        idxs = np.argsort(y2)

        # keep looping while some indexes still remain in the indexes
        # list
        while len(idxs) > 0:
            # grab the last index in the indexes list and add the
            # index value to the list of picked indexes
            last = len(idxs) - 1
            i = idxs[last]
            pick.append(i)

            # find the largest (x, y) coordinates for the start of
            # the bounding box and the smallest (x, y) coordinates
            # for the end of the bounding box
            xx1 = np.maximum(x1[i], x1[idxs[:last]])
            yy1 = np.maximum(y1[i], y1[idxs[:last]])
            xx2 = np.minimum(x2[i], x2[idxs[:last]])
            yy2 = np.minimum(y2[i], y2[idxs[:last]])

            # compute the width and height of the bounding box
            w = np.maximum(0, xx2 - xx1 + 1)
            h = np.maximum(0, yy2 - yy1 + 1)

            # compute the ratio of overlap
            overlap = (w * h) / area[idxs[:last]]

            # delete all indexes from the index list that have
            idxs = np.delete(idxs, np.concatenate(([last],
                                                   np.where(overlap > overlapThresh)[0])))

        # return only the bounding boxes that were picked using the
        # integer data type
        return pick
