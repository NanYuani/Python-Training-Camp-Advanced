# exercises/conv.py
"""
练习：二维卷积 (Convolution)

描述：
实现一个简单的二维卷积操作。

请补全下面的函数 `conv2d`。
"""
import numpy as np

def conv2d(x, kernel):
    """
    执行二维卷积操作 (无填充, 步幅为 1)。

    Args:
        x (np.array): 输入二维数组, 形状 (H, W)。
        kernel (np.array): 卷积核二维数组, 形状 (kH, kW)。

    Return:
        np.array: 卷积结果, 形状 (out_H, out_W)。
                  out_H = H - kH + 1
                  out_W = W - kW + 1
    """
    # 请在此处编写代码
    # 提示：
    # 1. 获取输入 x 和卷积核 kernel 的形状。
    # 2. 计算输出的高度和宽度。
    # 3. 初始化输出数组。
    # 4. 使用嵌套循环遍历输出数组的每个位置 (i, j)。
    # 5. 提取输入 x 中与当前卷积核对应的区域 (patch)。
    # 6. 计算 patch 和 kernel 的元素乘积之和 (np.sum(patch * kernel))。
    # 7. 将结果存入输出数组 out[i, j]。
    # pass
    out_h = x.shape[0] - kernel.shape[0] + 1 # 输出的高度
    out_w = x.shape[1] - kernel.shape[1] + 1 # 输出的宽度
    out = np.zeros((out_h, out_w)) # 初始化输出数组
    for i in range(out_h): # 遍历输出数组的每个位置
        for j in range(out_w): # 遍历输出数组的每个位置
            patch = x[i: i + kernel.shape[0], j: j + kernel.shape[1]] # 提取输入 x 中与当前卷积核对应的区域
            out[i, j] = np.sum(patch * kernel) # 计算 patch 和 kernel 的元素乘积之和
    return out 