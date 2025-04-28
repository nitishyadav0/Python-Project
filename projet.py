import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_path = r"C:\Users\ASUS\OneDrive\Desktop\Dataset Degree.xlsx"
df = pd.read_excel(data_path) 

sns.histplot(df['Employment Rate'], kde=True, color="skyblue")
plt.title('Histogram of Employment Rate')
plt.xlabel('Employment Rate')
plt.ylabel('Frequency')
plt.show()
sns.barplot(x='Degree', y='Employment Rate', data=df, palette='Set2')
plt.title('Employment Rate by Degree')
plt.xlabel('Degree')
plt.ylabel('Employment Rate')
plt.xticks(rotation=45)  
plt.show()
sns.scatterplot(x='Year', y='Employment Rate', data=df, hue='Degree', palette='coolwarm')
plt.title('Employment Rate vs Year')
plt.xlabel('Year')
plt.ylabel('Employment Rate')
plt.legend(title='Degree')
plt.show()
sns.boxplot(x='Degree', y='Employment Rate', data=df, palette='pastel')  # Fixed typo: 'Pastell' to 'pastel'
plt.title('Boxplot of Employment Rate by Degree')
plt.xlabel('Degree')
plt.ylabel('Employment Rate')
plt.xticks(rotation=45)
plt.show()

# 5. Line Plot of Employment Rate over Time
sns.lineplot(x='Year', y='Employment Rate', data=df, marker='o', color="orange")  # Fixed: Y → y
plt.title('Employment Rate Over Time')
plt.xlabel('Year')
plt.ylabel('Employment Rate')
plt.show()
