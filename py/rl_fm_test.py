#!/home/sgl/.virtualenvs/PT/bin/python
# coding:utf-8

'''
pycuda test
'''

from pycuda.compiler import SourceModule
from timeit import default_timer as timer
import numpy as np
import pycuda.driver as drv
import pycuda.autoinit
import torch as t
import torchvision

x = t.rand(5, 3)
y = t.rand(5, 3)
print(x)
print(t.cuda.is_available())

if t.cuda.is_available():
    x = x.cuda()
    y = y.cuda()
    print(x+y)



mod = SourceModule("""
__global__ void func(float *a, float *b, size_t N)
{
 const int i = blockIdx.x * blockDim.x + threadIdx.x;
 if (i >= N)
 {
  return;
 }
 float temp_a = a[i];
 float temp_b = b[i];
 a[i] = (temp_a * 10 + 2 ) * ((temp_b + 2) * 10 - 5 ) * 5;
 // a[i] = a[i] + b[i];
}
""")

func = mod.get_function("func")


def test(N):
    # N = 1024 * 1024 * 90  # float: 4M = 1024 * 1024

    print("N = %d" % N)

    N = np.int32(N)

    a = np.random.randn(N).astype(np.float32)
    b = np.random.randn(N).astype(np.float32)
    # copy a to aa
    aa = np.empty_like(a)
    aa[:] = a
    # GPU run
    nTheads = 256
    nBlocks = int((N + nTheads - 1) / nTheads)
    start = timer()
    func(
        drv.InOut(a), drv.In(b), N,
        block=(nTheads, 1, 1), grid=(nBlocks, 1))
    run_time = timer() - start
    print("gpu run time %f seconds " % run_time)
    # cpu run
    start = timer()
    aa = (aa * 10 + 2) * ((b + 2) * 10 - 5) * 5
    run_time = timer() - start

    print("cpu run time %f seconds " % run_time)

    # check result
    r = a - aa
    print(min(r), max(r))


def main():
    for n in range(1, 10):
        N = 1024 * 1024 * (n * 10)
        print("------------%d---------------" % n)
        test(N)


if __name__ == '__main__':
    main()
