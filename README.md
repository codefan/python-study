# 说明

/MLIA-note 目录中为《机器学习 实战》 Peter Harrington 2013 根据随书源码的重写版本

1. 将源码从python2 迁移到 python3
2. 用juptyter notebook重新编排，便于阅读
3. 将书中绝大多数的图标用源码实现，便于比较

最后一章 大数据与MapReduce缺少环境没有编写对应的实验代码

/deepLearning 目录为《深度学习入门：基于Python的理论与实现》 斋藤康毅 

这个文件夹中的源码为学习是测试代码，和随书源码有较大的差异

MultiLayerNet.py 是根据原来的第4章的 two_layer_net.py 改写的，可以实现多层网络，并在 trainNeuralNet.ipynb 中进行训练，不过对于手写识别的示例来说3层网络似乎还没有2层网络效果好。