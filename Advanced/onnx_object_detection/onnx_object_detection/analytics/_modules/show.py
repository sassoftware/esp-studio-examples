#!/usr/bin/env python
# encoding: utf-8
# Copyright © 2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import cv2

font_face = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.6
thickness = 1
box_color = (5, 74, 153)[::-1]  # SAS Blue (b,g,r)


def draw_bounding_boxes(
    img_np, ret_boxes, ret_label, ret_scores, coords_type, show_labels=True
):
    image_h, image_w, _ = img_np.shape
    n_objects = len(ret_scores)
    lbl_list = ret_label.split(",")

    for i in range(n_objects):
        prob = float(ret_scores[i])
        x = float(ret_boxes[i * 4 + 0])
        y = float(ret_boxes[i * 4 + 1])
        width = float(ret_boxes[i * 4 + 2])
        height = float(ret_boxes[i * 4 + 3])

        if coords_type == "yolo":
            x_min = int(image_w * (x - width / 2))
            y_min = int(image_h * (y - height / 2))
            x_max = int(image_w * (x + width / 2))
            y_max = int(image_h * (y + height / 2))
        elif coords_type == "coco":
            x_min = int(image_w * x)
            y_min = int(image_h * y)
            x_max = int(image_w * width)
            y_max = int(image_h * height)
        elif coords_type == "rect":
            x_min = int(image_w * x)
            y_min = int(image_h * y)
            x_max = int(image_w * (x + width))
            y_max = int(image_h * (y + height))

        # draw bounding box
        cv2.rectangle(img_np, (x_min, y_min), (x_max, y_max), box_color, 1)

        if show_labels:
            # draw object label and the probability
            text = f"{lbl_list[i].capitalize()} ({prob*100:.0f}%)"
            if sum(box_color) / 3 < 140:
                text_color = (255, 255, 255)  # (b,g,r)
            else:
                text_color = (0, 0, 0)  # (b,g,r)
            size = cv2.getTextSize(text, font_face, font_scale, thickness)

            text_width = int(size[0][0])
            text_height = int(size[0][1])
            line_height = size[1]
            margin = 2

            text_x = x_min + margin
            text_y = y_min - line_height - margin

            # draw a filled rectangle around text
            cv2.rectangle(
                img_np,
                (text_x - margin, text_y + line_height + margin),
                (text_x + text_width + margin, text_y - text_height - margin),
                box_color,
                -1,
            )

            cv2.putText(
                img_np,
                text,
                (text_x, text_y),
                font_face,
                font_scale,
                text_color,
                thickness,
                cv2.LINE_AA,
            )

    return img_np
