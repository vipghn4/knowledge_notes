---
title: Key notes on object detection
tags: Computer vision
---

# Table of Contents
[toc]

# Key notes on object detection
## Bounding box encoding and decoding
**Bounding box encoding and decoding**.
* *Assumptions*.
    * $B=(x_1, y_1, x_2, y_2)=(x_c, y_c, w, h)$ is a bounding box
    * $(x_1, y_1)$ is the top-left corner of the box
    * $(x_2, y_2)$ is the bottom-right corner of the box
    * $(x_c,y_c)$ is the center of the box
    * $(w, h)$ is the width and height of the bounding box
* *RCNN*.
    * *Assumptions*.
        * $P=(x_p,y_p,w_p,h_p)$ is a region proposal
        * $(x_p,y_p)$ is the region center
        * $(w_p,h_p)$ is the region width and height
    * *Box encoding*. $o=(x_o,y_o,w_o,h_o)$
        * $(x_o,y_o)$ specifies a scale-invariant translation of $P$'s center
        * $(w_o,h_o)$ specifies log-space translations of $P$'s sizes
    * *Box decoding*.
        * $\hat{x}_c=w_p x_o+x_p\to x_o=(\hat{x}_c-x_p)/w_p$
        * $\hat{y}_c=h_p y_o+y_p\to y_o=(\hat{y}_c-y_p)/h_p$
        * $\hat{w}=w_p \exp w_o\to w_o=\log (\hat{w}/w_p) = \log \hat{w} - \log w_p$
        * $\hat{h}=h_p \exp h_o\to h_o=\log (\hat{h}/h_p) = \log \hat{h} - \log h_p$
* *Faster RCNN*. Similar to RCNN but $P$ is an anchor box, not a region proposal
* *YOLO*.
    * *Box encoding*. $o=(x_o,y_o,w_o,h_o)$
        * $(x,y)$ is the center of the box relative to the bounds of the grid-cell
        * $(w,h)$ is the width and height of the box, relative to the whole image
* *SSD*. Similar to Faster RCNN
* *YOLOv3*. 
    * *Assumptions*.
        * $(c_x,c_y)$ is the top-left corner of the cell
        * $(p_w,p_h)$ is the width and height of the prior box
        * $\sigma(\cdot)$ is the sigmoid function
    * *Box encoding*. $o=(t_x,t_y,t_w,t_h)$
    * *Box decoding*.
        * $b_x=\sigma(t_x) + c_x$
        * $b_y=\sigma(t_y) + c_y$
        * $b_w=p_w \exp t_w$
        * $b_h=p_h \exp t_h$
* *Retinanet*. Similar to Faster RCNN

## Prediction - target matching strateiges and loss contribution of predictions
**Object deteciton detection-groundtruth matching strategies**.
* *Assumptions*.
    * $\{t_1,\dots,t_N\}$ are target boxes
    * $\{p_1,\dots,p_M\}$ are predicted boxes
    * $p_i^*$ is the predicted boxes which is the best to target box $i$, compared to other predicted boxes
    * $t_i^*$ is the target boxes which is the best to predicted box $i$, compared to other target boxes
* *RCNN*.
    * *Matching strategy*.
        * $(t_i,p_j)$ is a match if $p_j = p_i^*$ and $\text{IoU}(t_i,p_j) \geq 0.5$
        * $p_j$ is negative if $\max_{t_i} \text{IoU}(t_i,p_j) < 0.3$ (via grid search)
    * *Loss computation*. MSE for localization, and cross entropy for classification
* *YOLO*.
    * *Matching strategy*.
        * $(t_i,p_j)$ is a match if $p_j = p_i^*$
    * *Loss computation*. MSE for localization, objectness classification, and classification
        * If $t_i$ appears in cell $j$, then the cell is regressed towards the corresponding object class
        * If $(t_i,p_j)$ is a match, then $p_j$ is regressed towards $t_i$ in terms of location and objectness
* *Faster RCNN*.
    * *Matching strategy*. 
        * $(t_i,p_j)$ is a match, and $p_j$ is hence positive, if
            * $p_j = p_i^*$, or
            * $\text{IoU}(t_i, p_j) \geq 0.7$ and $t_i = t^*_j$
        * $p_j$ is negative if $\max_{t_i} \text{IoU}(t_i,p_j) < 0.3$
    * *Loss computation*. Smooth L1 for localization and cross entropy for classification
    * *Imbalance class handling*. Only consider very negative examples, i.e. max IoU to all target boxes is below $0.3$
* *SSD*.
    * *Matching strategy*. 
        * $(t_i,p_j)$ is a match, and $p_j$ is hence positive, if
            * $p_j = p_i^*$, or
            * $\text{IoU}(t_i, p_j) \geq 0.5$ and $t_i = t^*_j$
        * $p_j$ is negative if it is not positive
    * *Loss computation*. Smooth L1 for localization and cross entropy for classification
        * *Localization loss*. Matched predicted boxes are regressed towards their target boxes
        * *Classification loss*. 
            * Positive predicted boxes are regressed towards their target boxes' classes
            * Negative predicted boxes are regressed towards background class
    * *Imbalance class handling*. Use hard negative mining
* *YOLOv3*.
    * *Matching strategy*.
        * $(t_i,p_j)$ is a match if $p_j=p_i^*$
        * $p_j$ is negative if $\max_{t_i} \text{IoU}(t_i,p_j) < 0.5$
    * *Loss computation*. Similar to YOLOv2, which is again similar to YOLOv1
* *Retinanet*.
    * *Matching strategy*. Similar to Faster RCNN with IOU thresholds $0.5$ and $0.4$
    * *Loss computation*. Smooth L1 for localization and focal loss for classification

# Appendix
## Concepts
**Aspects to consider when working on object detection**.
* Data augmentation and preprocessing
* Model and optimization algorithm
* Box encoding and decoding
* NMS strategy
* Prediction-groundtruth matching when training
* Prediction-groundtruth matching when evaluation

**Other notable points**. 
* Multi-scale training
* Anchor boxes, i.e. how to remove anchor boxes (Centernet has done this)
* Smoothed target confidence score, i.e. $\text{conf\_t} = \text{Pr}(\text{objectness}) \cdot \text{IOU}(\text{truth}, \text{pred})