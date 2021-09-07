import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rcParams['font.family']='YouYuan'
matplotlib.rcParams['font.size']=20
a=np.arange(0,100,1)
plt.plot(a,a*a,'r--') #红色虚线
plt.xlabel('横轴：x',color='green')
plt.ylabel('纵轴：y=x^2',color='red')
plt.axis([0,10,0,100])
plt.show()
