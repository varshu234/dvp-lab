import matplotlib.pyplot as plt
std=['sslc','puc','1sem','2sem']
values=[500,600,620,680]
plt.bar(std,values,color='blue')
plt.xlabel("education", fontsize=12)
plt.ylabel("marks obtained",fontsize=12)
plt.title("ABC-123")
plt.show()
