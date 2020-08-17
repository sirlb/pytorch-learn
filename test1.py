import torch
import os
os.environ.setdefault('CUDA_VUSIBLE_DEVICE','7,3')

print('hello world')
#多角度
a=1
d='dfdf'
c={"a":1,"b":2,"c":55}
d=[2,3,4,5]
print('nihao ')
# 输出
print('nihao ')
t=torch.tensor([1,2,3,4],device='cuda:0')

print('nihao ')
for i in range(10000):
    print(i)
    print(t)

print("hello")