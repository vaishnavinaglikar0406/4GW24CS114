import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.violinplot( x="day",y="total_bill",hue="sex",data=tips,palette="Set3")
plt.xlabel("Day of the week", fontsize=12)
plt.ylabel("Total Bill ($)", fontsize=12)
plt.title("Total Bill Amounts by Day", fontsize=14)
plt.show()
