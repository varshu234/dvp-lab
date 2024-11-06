import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def sinplot(n=10):
    x=np.linspace(0,14,100)
    for i in range(1,n+1):
     plt.plot(x,np.sin(x+i*0.5)*(n+2-i))
sns.set_context("talk")
sinplot()
plt.title("varsha s - 1KI23CS176 sinplot")
plt.show()
