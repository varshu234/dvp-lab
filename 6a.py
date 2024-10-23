import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(1,20,7)
y1=x
y2=np.square(x)
y3=np.sqrt(x)
print(y1)
print(y2)
print(y3)
plt.plot(x,y1,'r',x,y2,'g',x,y3,'b')
plt.legend(['x','square-x','sqrt-x'])
plt.xticks(x)
plt.yticks(y2)
plt.title("linear_varsha s 1KI23CS176")
plt.show()