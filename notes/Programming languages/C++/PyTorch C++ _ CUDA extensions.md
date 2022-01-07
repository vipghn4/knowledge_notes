---
title: PyTorch C++ / CUDA extensions
tags: Programming languages
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [Writing a C++ Extension](#writing-a-c-extension)
  * [Building with `setuptools`](#building-with-setuptools)
  * [Building with `torch.utils.cpp_extension.load()`](#building-with-torchutilscppextensionload)
* [Writing a mixed C++/CUDA extension](#writing-a-mixed-ccuda-extension)
  * [CUDA basic](#cuda-basic)
    * [CUDA programming model](#cuda-programming-model)
    * [Basics of CUDA programming](#basics-of-cuda-programming)
  * [Writing CUDA extension](#writing-cuda-extension)
* [References](#references)
<!-- /TOC -->

## Writing a C++ Extension
### Building with `setuptools`
**`setuptools`**. Allow building C++ extensions ahead of time

**Build C++ extension**. Write a `setup.py` using `setuptools` to compile our C++ code
* *Code*.

    ```python
    from setuptools import setup, Extension
    from torch.utils import cpp_extension

    r"""
    Documentation: https://docs.python.org/3/distutils/apiref.html#distutils.core.setup
    Explain:
    * `ext_modules`: A list of Python extensions to be built
        * cpp_extension.CppExtension: Create a `setuptools.Extension` for C++
    * `cmdclass`: A mapping of command names to Command subclasses
        * cpp_extension.BuildExtension: Create a cutom setuptools build extension
    """
    setup(
        name='lltm_cpp',
        ext_modules=[cpp_extension.CppExtension(
            name='lltm_cpp',
            sources=['lltm.cpp']
        )],
        cmdclass={
            'build_ext': cpp_extension.BuildExtension
        }
    )
    ```

* *Explain*.
    * `CppExtension` is a convenient wrapper for `setuptools.Extension` passing the correct include paths and sets the language of the extension to C++. The equivalent vanilla `setuptools` code would be

        ```python
        Extension(name='lltm_cpp',
                  sources=['lltm.cpp'],
                  include_dirs=cpp_extension.include_paths(),
                  language='c++')
        ```

    * `BuildExtension` performs a number of required configuration steps and checks and also manages mixed compilation in case of mixed C++/CUDA extensions

**Write C++ code**.
* *Code for `lltm.cpp`*. Small piece of code within `lltm.cpp`

```c++
#include <torch/extension.h>
#include <iostream>

torch::Tensor d_sigmoid(torch::Tensor z) {
    auto s = torch::sigmoid(z);
    return (1 - s) * s;
}
```

* *Exlpain*.
    * `torch/extension.h` is a one-stop header to include all necessary pyTorch bits to write C++ extensions, i.e.
        * The ATen library, i.e. primary API for tensor computation
        * pybind11, i.e. PyTorch bindings for C++ code
        * Headers managing the details of interaction between ATen and pybind11
    * `torch::Tensor` is the primary datatype for all computations
    * `auto` is a placeholder type specifiers
        * For variables, the type is deduced from the initializer
        * For functions, the return type is deduced from its return statements
        * For non-type template parameters, the type will be deduced form the argument

**Write LLTM module**.
* *Step 1: Forward pass*.
    * *Code*.

        ```cpp
        #include <torch/extension.h>
        #include <vector>

        std::vector<torch::Tensor> lltm_forward(
            torch::Tensor input,
            torch::Tensor weights,
            torch::Tensor bias,
            torch::Tensor old_h,
            torch::Tensor old_cell) {
            auto X = torch::cat({old_h, input}, /*dim=*/1);

            auto gate_weights = torch::addmm(bias, X, weights.transpose(0, 1));
            auto gates = gate_weights.chunk(3, /*dim=*/1);

            auto input_gate = torch::sigmoid(gates[0]);
            auto output_gate = torch::sigmoid(gates[1]);
            auto candidate_cell = torch::elu(gates[2], /*alpha=*/1.0);

            auto new_cell = old_cell + candidate_cell * input_gate;
            auto new_h = torch::tanh(new_cell) * output_gate;

            return {new_h,
                    new_cell,
                    input_gate,
                    output_gate,
                    candidate_cell,
                    X,
                    gate_weights};
        }
        ```
* *Step 2: Backward pass*. The C++ extension API currently (2020) does not provide a way of automatically generating a backward function
    * *Code*.

        ```cpp
        std::vector<torch::Tensor> lltm_backward(
            torch::Tensor grad_h,
            torch::Tensor grad_cell,
            torch::Tensor new_cell,
            torch::Tensor input_gate,
            torch::Tensor output_gate,
            torch::Tensor candidate_cell,
            torch::Tensor X,
            torch::Tensor gate_weights,
            torch::Tensor weights) {

            auto d_output_gate = torch::tanh(new_cell) * grad_h;
            auto d_tanh_new_cell = output_gate * grad_h;
            auto d_new_cell = d_tanh(new_cell) * d_tanh_new_cell + grad_cell;

            auto d_old_cell = d_new_cell;
            auto d_candidate_cell = input_gate * d_new_cell;
            auto d_input_gate = candidate_cell * d_new_cell;

            auto gates = gate_weights.chunk(3, /*dim=*/1);
            d_input_gate *= d_sigmoid(gates[0]);
            d_output_gate *= d_sigmoid(gates[1]);
            d_candidate_cell *= d_elu(gates[2]);

            auto d_gates =
                torch::cat({d_input_gate, d_output_gate, d_candidate_cell}, /*dim=*/1);

            auto d_weights = d_gates.t().mm(X);
            auto d_bias = d_gates.sum(/*dim=*/0, /*keepdim=*/true);

            auto d_X = d_gates.mm(weights);
            const auto state_size = grad_h.size(1);
            auto d_old_h = d_X.slice(/*dim=*/1, 0, state_size);
            auto d_input = d_X.slice(/*dim=*/1, state_size);

            return {d_old_h, d_input, d_weights, d_bias, d_old_cell};
        }
        ```

* *Step 3: Bind C++ functions or classes into Python*. Use `pybind11`
    * *Code*.

        ```c++
        PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
            m.doc() = "Some doc string here...";
            m.def("forward", &lltm_forward, "LLTM forward");
            m.def("backward", &lltm_backward, "LLTM backward");
        }
        ```

    * *Explain*. `TORCH_EXTENSION_NAME` will be defined, by the torch extension build, as the name we give our extension in `setup.py`, i.e. in this case is `lltm`
* *Step 4*. Compile our extension
    * *Directory structure*.

        ```
        pytorch/
            lltm-extension/
                lltm.cpp
                setup.py
        ```

    * *Command*. `python setup.py install` to build and install our extension
* *Step 5*. Use our extension
    * *Code*.

        ```python
        import math
        import torch

        # Our module!
        import lltm_cpp

        class LLTMFunction(torch.autograd.Function):
            @staticmethod
            def forward(ctx, input, weights, bias, old_h, old_cell):
                outputs = lltm_cpp.forward(input, weights, bias, old_h, old_cell)
                new_h, new_cell = outputs[:2]
                variables = outputs[1:] + [weights]
                ctx.save_for_backward(*variables)

                return new_h, new_cell

            @staticmethod
            def backward(ctx, grad_h, grad_cell):
                outputs = lltm_cpp.backward(
                    grad_h.contiguous(), grad_cell.contiguous(), *ctx.saved_variables)
                d_old_h, d_input, d_weights, d_bias, d_old_cell = outputs
                return d_input, d_weights, d_bias, d_old_h, d_old_cell
        ```

### Building with `torch.utils.cpp_extension.load()`
**`torch.utils.cpp_extension.load()`**. Allow building C++ extensions just in time (JIT)

**JIT compilation mechanism**. Provide us with a way of compiling and loading our extensions on the fly
* *Code*.

    ```python
    from torch.utils.cpp_extension import load

    lltm_cpp = load(name="lltm_cpp", sources=["lltm.cpp"])
    ```
* *Steps*.
    1. Create a temporary directory `/tmp/torch_extensions/lltm`
    2. Emit a `Ninja` build file into that temporary directory
    3. Compile our source files to a shared library
    4. Import this shared library as a Python module
* *Advantages and when to use*.
    * *Advantages*. Perform the same as `setuptools` but remove the needs of maintaining a separate `setup.py`
    * *When to use*. When `setup.py` is not very complicated


## Writing a mixed C++/CUDA extension
### CUDA basic
#### CUDA programming model
**Device and host**.
* *Device*. Equivalent to GPU
* *Host*. Equivalent to CPU

**CUDA kernels and threads**.
* *Definitions*
    * *Kernel*. Function which runs on the device
    * *Threads*. A CUDA kernel is executed by an array of threads
        * All threads run the same code
        * Each thread has an ID used to compute memory addresses and control decisions
* *Principle*.
    * One kernel is executed at a time
    * Many threads execute each kernel
* *Example code*.

    ```cpp
    float x = input[threadId];
    float y = func(x);
    output[threadId] = y;
    ```

**Grids**. Kernel launches a grid of thread blocks
* *Thread coorperation*.
    * *Purposes*.
        * Share results to avoid redundant computation
        * Share memory accesses to drastically reduce bandwidth
* *Principles*.
    * Threads within a block coorperate via a shared memory
    * Threads within a block can synchronize
    * Threads in different blocks cannot coorperate
* *Advantage*. Allow programs to transparently scale to different GPUs

#### Basics of CUDA programming
**Kernels**. C functions with some restrictions
* *Restrictions*.
    * Cannot access host memory
    * Must have `void` return type
    * No variable number of arguments, i.e. `varargs`
    * No recursive
    * No static variables
* *Function arguments*. Automatically copied from host to device

**CUDA function qualifiers**.
* `__global__`
    * Function called from host and executed on device
    * Must return `void`
* `__device__`
    * Function called from device and run on device
    * Cannot be called from host code
* `__host__`
    * Function called from host and executed on host (default)
    * `__host__` and `__device__` quanlifiers can be combined to generate both GPU and GPU code

**Launching kernels**.
* *Syntax*. `kernel<<<dim3 dG, dim3 dB>>>(...)`
* *Execution configuration*. `<<< >>>`
    * `dG` - dimension and size of grid (in blocks).
        * Two-dimensional: `x` and `y`
        * Blocks launched in the grid: `dG.x * dG.y`
    * `dB` - dimension and size of blocks (in threads).
        * Three-dimensional: `x`, `y`, and `z`
        * Threads per block: `dB.x * dB.y * dB.z`
    * *Default `dim3` fields*. `1`
* *Example code*.

    ```cpp
    dim3 grid, block;
    grid.x = 2; grid.y = 4;
    block.x = 8; block.y = 16;

    kernel<<<grid, block>>>(...);
    ```

    or

    ```cpp
    dim3 grid(2, 4), block(8, 16);

    kernel<<<grid, block>>>(...);
    ```

**Built-in device variables**.
* *Built-in device variables*. All `__global__` and `__device__` functions have access to
    * `dim3 gridDim`. Dimensions of the grid in blocks
    * `dim3 blockDim`. Dimensions of the grid in threads
    * `dim3 blockIdx`. Block index within the grid
    * `dim3 threadIdx`. Thread index within the block
* *Purpose*. Determine unique thread IDs, i.e. map from local thread ID (`threadIdx`) to a global ID which can be used as array indices

**Example CUDA code**.
* *Minimal kernel*
    ```cpp
    __global__ void assign(int* a_d, int value){
        int idx = blockDim.x * blockIdx.x + threadIdx.x;
        a_d[idx] = value;
    }
    ```
* *C++ and CUDA codes*.
    * *C++ code*.

        ```cpp
        void inc_cpu(int *a, int N){
            int idx;
            for (idx = 0; idx<N; idx++) a[idx] = a[idx] + 1;
        }

        int main(){
            inc_cpu(a, N);
        }
        ```

    * *CUDA code*.

        ```cpp
        __global__ void inc_gpu(int *a, int N){
            int idx = blockIdx.x * blockDim.x
            + threadIdx.x;
            if (idx < N) a[idx] = a[idx] + 1;
        }

        int main(){
            dim3 dimBlock (blocksize);
            dim3 dimGrid( ceil( N / (float)blocksize) );
            inc_gpu<<<dimGrid, dimBlock>>>(a, N);
        }
        ```

### Writing CUDA extension
**General strategy**.
1. Write a C++ file defining the functions which will be called from Python
    * *CUDA files*. Contain actual CUDA kernels
    * *CUDA functions*. This file will also declare functions defined in CUDA (`.cu`) files
    * *Using CUDA functions*.
        * The C++ functions will then do some checks
        * The C++ functions forward their calls to the CUDA functions
2. Bind the functions to Python with pybind11
3. Write `setup.py` file
    * `cpp_extension` package takes care of compiling the C++ sources with a C++ compiler, e.g. `gcc`, and the CUDA sources with NVIDIA's `nvcc` compiler
    * The sources will be linked to one shared library, which is available to us from Python code

**Writing C++ file**.
* *Code*.

    ```cpp
    #include <torch/extension.h>
    #include <vector>

    // CUDA forward declarations

    std::vector<torch::Tensor> lltm_cuda_forward(
        torch::Tensor input,
        torch::Tensor weights,
        torch::Tensor bias,
        torch::Tensor old_h,
        torch::Tensor old_cell);

    std::vector<torch::Tensor> lltm_cuda_backward(
        torch::Tensor grad_h,
        torch::Tensor grad_cell,
        torch::Tensor new_cell,
        torch::Tensor input_gate,
        torch::Tensor output_gate,
        torch::Tensor candidate_cell,
        torch::Tensor X,
        torch::Tensor gate_weights,
        torch::Tensor weights);

    // C++ interface

    #define CHECK_CUDA(x) TORCH_CHECK(x.type().is_cuda(), #x " must be a CUDA tensor")
    #define CHECK_CONTIGUOUS(x) TORCH_CHECK(x.is_contiguous(), #x " must be contiguous")
    #define CHECK_INPUT(x) CHECK_CUDA(x); CHECK_CONTIGUOUS(x)

    std::vector<torch::Tensor> lltm_forward(
        torch::Tensor input,
        torch::Tensor weights,
        torch::Tensor bias,
        torch::Tensor old_h,
        torch::Tensor old_cell) {
        CHECK_INPUT(input);
        CHECK_INPUT(weights);
        CHECK_INPUT(bias);
        CHECK_INPUT(old_h);
        CHECK_INPUT(old_cell);

        return lltm_cuda_forward(input, weights, bias, old_h, old_cell);
    }

    PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
        m.def("forward", &lltm_forward, "LLTM forward (CUDA)");
    }
    ```

* *Notes*.
    * NVCC can reasonably compile C++11, thus we still have ATen and C++ standard library available to us
    * `setuptools` cannot handle files with the same name but different extensions

        $\to$ We must give our CUDA file a different ame than the C++ file, e.g. we cannot use `lltm.cpp` and `lltm.cu`
    * For JIT, we can still use the same name with different extensions

**Writing CUDA file**.
* *Code*.
    * *Utility codes*.

        ```c++
        #include <torch/extension.h>
        #include <cuda.h>
        #include <cuda_runtime.h>
        #include <vector>

        template <typename scalar_t>
        __device__ __forceinline__ scalar_t sigmoid(scalar_t z) {
            return 1.0 / (1.0 + exp(-z));
        }

        template <typename scalar_t>
        __device__ __forceinline__ scalar_t d_sigmoid(scalar_t z) {
            const auto s = sigmoid(z);
            return (1.0 - s) * s;
        }

        template <typename scalar_t>
        __device__ __forceinline__ scalar_t d_tanh(scalar_t z) {
            const auto t = tanh(z);
            return 1 - (t * t);
        }

        template <typename scalar_t>
        __device__ __forceinline__ scalar_t elu(scalar_t z, scalar_t alpha = 1.0) {
            return fmax(0.0, z) + fmin(0.0, alpha * (exp(z) - 1.0));
        }

        template <typename scalar_t>
        __device__ __forceinline__ scalar_t d_elu(scalar_t z, scalar_t alpha = 1.0) {
            const auto e = exp(z);
            const auto d_relu = z < 0.0 ? 0.0 : 1.0;
            return d_relu + (((alpha * (e - 1.0)) < 0.0) ? (alpha * e) : 0.0);
        }
        ```

    * *Main CUDA kernels*.

        ```cpp
        // torch::RestrictPtrTraits indicates that __restrict__ must be used, i.e. to
        // tell the compiler that there will be no pointer aliasing among the arguments
        // passed into the function. Consequentially, the compiler can further optimize
        // its operations

        // size_t is an unsigned integer data type, which measures bytes of any object's
        // size and returned by sizeof operator. In C++, the default size for array
        // indices and loop counting is size_t. This is because of the fact that the
        // largest array supported by the platform will be indexable with size_t
        // Reference:
        //     * https://en.cppreference.com/w/c/types/size_t
        //     * https://stackoverflow.com/questions/59728149/why-size-t-is-used-for-indexing-representing-size-of-an-array

        template <typename scalar_t>
        __global__ void lltm_cuda_forward_kernel(
            const torch::PackedTensorAccessor<scalar_t,3,torch::RestrictPtrTraits,size_t> gates,
            const torch::PackedTensorAccessor<scalar_t,2,torch::RestrictPtrTraits,size_t> old_cell,
            torch::PackedTensorAccessor<scalar_t,2,torch::RestrictPtrTraits,size_t> new_h,
            torch::PackedTensorAccessor<scalar_t,2,torch::RestrictPtrTraits,size_t> new_cell,
            torch::PackedTensorAccessor<scalar_t,2,torch::RestrictPtrTraits,size_t> input_gate,
            torch::PackedTensorAccessor<scalar_t,2,torch::RestrictPtrTraits,size_t> output_gate,
            torch::PackedTensorAccessor<scalar_t,2,torch::RestrictPtrTraits,size_t> candidate_cell) {

            //batch index
            const int n = blockIdx.y;
            // column index
            const int c = blockIdx.x * blockDim.x + threadIdx.x;
            if (c < gates.size(2)){
                input_gate[n][c] = sigmoid(gates[n][0][c]);
                output_gate[n][c] = sigmoid(gates[n][1][c]);
                candidate_cell[n][c] = elu(gates[n][2][c]);
                new_cell[n][c] =
                    old_cell[n][c] + candidate_cell[n][c] * input_gate[n][c];
                new_h[n][c] = tanh(new_cell[n][c]) * output_gate[n][c];
            }
        }
        ```

    * *Main C++ code*.

        ```c++
        std::vector<torch::Tensor> lltm_cuda_forward(
            torch::Tensor input,
            torch::Tensor weights,
            torch::Tensor bias,
            torch::Tensor old_h,
            torch::Tensor old_cell) {
            auto X = torch::cat({old_h, input}, /*dim=*/1);
            auto gate_weights = torch::addmm(bias, X, weights.transpose(0, 1));

            const auto batch_size = old_cell.size(0);
            const auto state_size = old_cell.size(1);

            auto gates = gate_weights.reshape({batch_size, 3, state_size});
            auto new_h = torch::zeros_like(old_cell);
            auto new_cell = torch::zeros_like(old_cell);
            auto input_gate = torch::zeros_like(old_cell);
            auto output_gate = torch::zeros_like(old_cell);
            auto candidate_cell = torch::zeros_like(old_cell);

            const int threads = 1024;
            const dim3 blocks((state_size + threads - 1) / threads, batch_size);

            AT_DISPATCH_FLOATING_TYPES(gates.type(), "lltm_forward_cuda", ([&] {
                lltm_cuda_forward_kernel<scalar_t><<<blocks, threads>>>(
                    gates.packed_accessor<scalar_t,3,torch::RestrictPtrTraits,size_t>(),
                    old_cell.packed_accessor<scalar_t,2,torch::RestrictPtrTraits,size_t>(),
                    new_h.packed_accessor<scalar_t,2,torch::RestrictPtrTraits,size_t>(),
                    new_cell.packed_accessor<scalar_t,2,torch::RestrictPtrTraits,size_t>(),
                    input_gate.packed_accessor<scalar_t,2,torch::RestrictPtrTraits,size_t>(),
                    output_gate.packed_accessor<scalar_t,2,torch::RestrictPtrTraits,size_t>(),
                    candidate_cell.packed_accessor<scalar_t,2,torch::RestrictPtrTraits,size_t>());
            }));

            return {new_h, new_cell, input_gate, output_gate, candidate_cell, X, gates};
        }
        ```

* *Explain*.
    * `AT_DISPATCH_FLOATING_TYPES`.
        * *Description*. ATen abstract away the device and data type of the tensors we deal with. A tensor will, at runtime, still be backed by memory of a concrete type, on a concrete device

            $\to$ We need a way of determining, at runtime, what type a tensor is, and then selectively call functions with the corresponding correct type signature
        * *Arguments*.
            * A type, e.g. `gate.type()`
            * A name (for error messages)
            * A lambda function, where the type alias `scalar_t` is available and is defined as the type that the tensor actually is, at runtime, in that context

        >**NOTE**. If we want to dispatch over all types, not just floating point types, we can use `AT_DISPATCH_ALL_TYPES`

    * In CUDA kernels, we work directly on pointers with the right type, since working directly with high level type agnotic tensors inside CUDA kernels is very inefficient
    * `gates.packed_accessor<scalar_t,3,torch::RestrictPtrTraits,size_t>()`. Provide an easier way to index elements of `gates`, i.e. `gates[n][c][h]` rather than `gates[3*n + 5*c + h]`
        * `scalar_t` is the true type of the tensor
        * `3` is the number of dimension

* *References*. https://www.nvidia.com/content/cudazone/download/Getting_Started_w_CUDA_Training_NVISION08.pdf

**Write `setup.py`**.

```python
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='lltm',
    ext_modules=[
        CUDAExtension('lltm_cuda', [
            'lltm_cuda.cpp',
            'lltm_cuda_kernel.cu',
        ])
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
```

## References
* [CUDA documentations](http://developer.download.nvidia.com/compute/cuda/2_3/toolkit/docs/online/group__CUDART__MEMORY_ge4366f68c6fa8c85141448f187d2aa13.html)
* [Triton inference server](https://docs.nvidia.com/deeplearning/triton-inference-server/master-user-guide/docs/index.html)
* *Frameworks for model inference*
    * *Model quantization*. TensorRT, ONN
