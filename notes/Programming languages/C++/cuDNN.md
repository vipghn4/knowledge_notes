---
title: cuDNN
tags: Programming languages
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [Overview](#overview)
* [Programming model](#programming-model)
  * [Tensor descriptor](#tensor-descriptor)
  * [Tensor core operations](#tensor-core-operations)
* [Example code](#example-code)
* [References](#references)
<!-- /TOC -->

## Overview
**cuDNN**. A GPU-accelerated library of primitives for deep neural networks

**Provided implementations**.
* Convolution forward and backward, including cross-correlation
* Pooling forward and backward
* Softmax forward and backward
* Neuron activations forward and backward:
    * Rectified linear (ReLU)
    * Sigmoid
    * Hyperbolic tangent (TANH)
* Tensor transformation functions
* LRN, LCN and batch normalization forward and backward

## Programming model
**Lifetime of a cuDNN process**.
* *Create cuDNN handle*. An application using cuDNN must initialize a handle to the library context by calling `cudnnCreate()`

    >**NOTE**. This handle is explicitly passed to every subsequent library function which operates on GPU data
* *Release cuDNN handle*. After finishing using cuDNN, the application can release the resources associated with the library handle by `cudnnDestroy`

### Tensor descriptor
**cuDNN n-D tensor**.
* *Parameters*.
    * A tensor dimension `nbDims` (from 3 to 8)
    * A data type
    * `dimA` integer array defining the size of each dimension
    * `strideA` integer array defining the stride of each dimension
* *Dimension order*.
    * *First dimension*. Batch size `n`
    * *Second dimension*. The number of feature maps `c`
* *Overlapping dimensions*. We can have some dimensions overlapping each other within the same tensor by having the stride of one dimension smaller than the product of the dimension and the stride of the next dimension
    * *Overlapping dimension for I/O tensors*.
        * *Input tensor*. All routines will support tensors with overlapping dimensions for forward-pass input tensors
        * *Output tensor*. Dimensions of the output tensors cannot overlap

    >**NOTE**. cuDNN does not support negative strides unless specified

**WXYZ Tensor descriptor**. Tensor descriptor formats are identified using acronyms, with each letter referencing a corresponding dimension
* *Notes*.
    * All strides are strictly positive
    * Dimensions referenced by the letters are sorted in decreasing order of their respective strides
* *4D tensor descriptor*. Define the format for batches of 2D images with 4 letter `N`, `C`, `H`, `W`
    * *Commonly used formats*. `NCHW`, `NHWC`, `CHWN`
* *5D tensor descriptor*. Define the format of the batch of 3D images with 5 letters `N`, `C`, `D`, `H`, `W`
    * *Commonly used formats*. `NCDHW`, `NDHWC`, `CDHWN`

**Fully-packed tensors**.
* *Fully-packed tensors*. A tensor is `XYZ-fully-packed` if and only if
    * The number of tensor dimensions is equal to the number of letters preceding the `fully-packed` suffix
    * The stride of the `i`-th dimension is equal to the product of the `(i+1)`-th dimension by the `(i+1)`-th stride
    * The stride of the last dimension is `1`
* *Partially-packed tensors*. A `WXYZ` tensor is defined as `XYZ`-packed if and only if
    * The strides of all dimensions not referenced in the `-packed` suffix are greater or equal to the product of the next dimension by the next stride
    * The stride of each dimension referenced in the `-packed` suffix in position `i` is equal to the product of the `(i+1)`-st dimension by the `(i+1)`-st stride
    * If the last tensor's dimension is present in the `-packed` suffix, its stride is `1`
* *Spatially packed tensors*. Tensors which are partially packed in spatial dimensions
* *Overlapping tensors*. A tensor is defined to be overlapping if iterating over a full range of dimensions produces the same address more than once
    * *Explain*. `stride[i-1] < stride[i] * dim[i]` for some dimension `i` from `[1, nbDims]`

### Tensor core operations
**Tensor core operations**. Perform parallel floating-point accumulation of multiple floating-point product terms
* *Set up Tensor core operations*. Set the math mode to `CUDNN_TENSOR_OP_MATH` via `cudnnMathType_t` enumerator
    * *Default math mode*. `CUDNN_DEFAULT_MATH`, i.e. vaoid Tensor Core operations
* *Notes*.
    * Two math modes may generate different but still very close results
    * cuDNN library treats both modes of operation as functionally indistinguishable

**Commonly used operations**. See [here](https://docs.nvidia.com/deeplearning/sdk/cudnn-developer-guide/index.html)
* Convolution forwad and backward (by data and by filter)
* RNN

## Example code
See [here](https://github.com/tbennun/cudnn-training/blob/master/lenet.cu#L957)

## References
**Discussion**.
* cuDNN is thread-safe and its function can be called from multiple host threads, as long as threads do not share the same cuDNN handle simultaneously
* There are some cuDNN routines, which is not reproducible, i.e. generating the same bit-wise results across runs when executed on GPUs with the same architecture and the same number of SMs, i.e.
    * `cudnnConvolutionBackwardFilter` when `CUDNN_CONVOLUTION_BWD_FILTER_ALGO_0` or `CUDNN_CONVOLUTION_BWD_FILTER_ALGO_3` is used
    * `cudnnConvolutionBackwardData` when `CUDNN_CONVOLUTION_BWD_DATA_ALGO_0` is used
    * `cudnnPoolingBackward` when `CUDNN_POOLING_MAX` is used
    * `cudnnSpatialTfSamplerBackward`
    * `cudnnCTCLoss` and `cudnnCTCLoss_v8` when `CUDNN_CTC_LOSS_ALGO_NON_DETERMINSTIC` is used

**Terminologies**
* [Main reference](https://docs.nvidia.com/deeplearning/sdk/cudnn-developer-guide/index.html)
* [Documentations](https://docs.nvidia.com/deeplearning/sdk/cudnn-api/index.html)
* [CUDA context](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#context)
    * A CUDA context is analogous to a CPU process
    * All resources and actions performed within the driver API are encapsulated inside a CUDA context
    * The system automatically cleans up these resources when the context is destroyed
* [Why use FP16 rather than FP32](https://www.quora.com/What-is-the-difference-between-FP16-and-FP32-when-doing-deep-learning#:~:text=FP32%20is%20single%2Dprecision%20floating,FP32%20is%20big%20and%20slow.
