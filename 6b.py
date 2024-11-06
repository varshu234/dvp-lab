import matplotlib.pyplot as plt
overs=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
runs=[7,10,17,22,8,9,6,11,23,14,15,19,23,26,22,23,10,12,14,15]
plt.plot(overs,runs,marker='X',markerfacecolor='blue',markersize=8,linestyle='dashed',linewidth=2,color='red')
plt.xlabel("overs",color='green')
plt.ylabel("runs",color='blue')
plt.title("varsha s-1KI23CS176 - linearplot")
plt.show()