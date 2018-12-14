import numpy as np
from common.layers import *
from common.gradient import numerical_gradient

class MultiLayerNet:

    def __init__(self, layerSize, weight_init_std = 0.01):
        self.l = len(layerSize) - 1
        # 初始化权重
        self.W = []
        self.B = []
        self.layers = []
        # 初始化权重
        for i in range(self.l):
            # np.random.randn 为符合高斯分布（正态分布）的随机数据
            self.W.append(weight_init_std * np.random.randn(layerSize[i], layerSize[i+1]))
            self.B.append(np.zeros(layerSize[i+1]))
            # 生成层
            self.layers.append(Affine(self.W[i], self.B[i]))
            # 最后一层 输出层 不需要激活函数， 使用 SoftmaxWithLoss
            if(i<self.l-1):
                self.layers.append(Relu())

        self.lastLayer = SoftmaxWithLoss()
        
    def predict(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        
        return x
        
    # x:输入数据, t:监督数据
    def loss(self, x, t):
        y = self.predict(x)
        return self.lastLayer.forward(y, t)
    
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        if t.ndim != 1 : t = np.argmax(t, axis=1)
        
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy
        
    # x:输入数据, t:监督数据
    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)
        
        gW = []
        gB = []
        for i in range(self.l):
            gW.append(numerical_gradient(loss_W, self.W[i]))
            gB.append(numerical_gradient(loss_W, self.B[i]))
            
        return gW, gB
        
    def gradient(self, x, t):
        # forward
        self.loss(x, t)

        # backward
        dout = 1
        dout = self.lastLayer.backward(dout)
        for layer in self.layers[::-1]:
            dout = layer.backward(dout)

        # 设定
        gW = []
        gB = []
        for layer in self.layers:
            if type(layer) == Affine :
                gW.append(layer.dW)
                gB.append(layer.db)

        return gW, gB
