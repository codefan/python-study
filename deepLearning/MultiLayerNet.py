from common.functions import sigmoid, softmax, sigmoid_grad, cross_entropy_error
from common.gradient import numerical_gradient
import numpy as np

class MultiLayerNet:
    
    def __init__(self, layerSize, weight_init_std=0.01, h = sigmoid, sigma = softmax):
        self.l = len(layerSize) - 1
        self.h = h
        self.sigma = sigma
        self.W = []
        self.B = []
        # 初始化权重
        for i in range(self.l):
            # np.random.randn 为符合高斯分布（正态分布）的随机数据
            self.W.append(weight_init_std * np.random.randn(layerSize[i], layerSize[i+1]))
            self.B.append(np.zeros(layerSize[i+1]))

    def calcLayer(self, A, w, b, h):
        return self.h(np.dot(A,w) + b)
                          
    def predict(self, x):
        A = x
        # 隐藏层
        for i in range(self.l - 1):
            A = self.calcLayer(A, self.W[i], self.B[i], self.h)
        # 输出层
        return self.calcLayer(A, self.W[self.l-1], self.B[self.l-1], self.sigma)
        
    # x:输入数据, t:监督数据
    def loss(self, x, t):
        y = self.predict(x)        
        return cross_entropy_error(y, t)
    # 计算精度（准确率）
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)
        
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
        batch_num = x.shape[0]
        # forward
        # 输入层
        A = []
        Z = []
        z = x
        A.append(x)
        Z.append(x)
        # 隐藏层
        for i in range(self.l - 1):
            a = np.dot(z, self.W[i]) + self.B[i]
            z = self.h(a)
            A.append(a)
            Z.append(z)
        # 输出层
        a = np.dot(z, self.W[self.l-1]) + self.B[self.l-1]
        y = self.sigma(a)
        
        A.append(a)
        Z.append(y)
        # backward
        dy = (y - t) / batch_num
        
        gW = []
        gB = []
        
        gW.append(np.dot(Z[self.l-1].T, dy))
        gB.append(np.sum(dy, axis=0))
            
        for i in range(self.l-2,-1,-1):    
            da = np.dot(dy, self.W[i+1].T)
            dy = sigmoid_grad(A[i+1]) * da
            gW.append(np.dot(A[i].T, dy))
            gB.append(np.sum(dy, axis=0))
        # numerical_gradient 和这个返回的顺序一致
        return gW[::-1], gB[::-1]
