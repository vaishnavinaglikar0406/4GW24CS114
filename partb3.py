import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
temperature = [20, 25, 30, 28, 35, 32, 30, 28, 25, 22, 18, 15]

plt.plot(months, temperature, marker='o', linestyle='-', color='red')
plt.xlabel('Months')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Temperature Variation')
plt.show()
