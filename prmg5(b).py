import matplotlib.pyplot as plt 
labels = ['Category A', 'Category B', 'Category C', 'Category D'] 
sizes = [25, 40, 30, 35] 
colors = ['gold', 'lightcoral', 'lightgreen', 'lightskyblue'] 
explode = (0.1, 0, 0, 0)  # Explode the first slice (Category A) 
plt.pie(sizes, explode=explode, labels=labels, colors=colors, 
autopct='%1.1f%%', startangle=140) 
plt.title('Pie Chart Example') 
plt.show() 
