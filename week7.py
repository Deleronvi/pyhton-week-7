import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("path_to_your_dataset.csv")

print(data.head())
print(data.info())
print(data.describe())

data = data.fillna(method='ffill')

grouped_data = data.groupby('column_name').mean()

plt.figure(figsize=(10, 6))
plt.bar(grouped_data.index, grouped_data['target_column'])
plt.title('Bar Chart Example')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

plt.scatter(data['feature_1'], data['feature_2'])
plt.title('Scatter Plot Example')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
