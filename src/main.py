import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# check working directory
print("Current working directory:", os.getcwd())

# load dataset
df = pd.read_csv('data/Mall_Customers.csv')

# preview data
print(df.head())

# info
print("\n--- INFO ---")
print(df.info())

# description
print("\n--- DESCRIPTION ---")
print(df.describe())

# scatter plot
plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'])

plt.title('Income vs Spending Score')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')

plt.show()

from sklearn.cluster import KMeans

# select features for clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# define KMeans with 5 clusters (common choice for this dataset)
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# plot clusters
plt.figure(figsize=(8,6))
colors = ['red', 'blue', 'green', 'cyan', 'magenta']

for i in range(5):
    plt.scatter(
        X[df['Cluster'] == i]['Annual Income (k$)'],
        X[df['Cluster'] == i]['Spending Score (1-100)'],
        s=50,
        c=colors[i],
        label=f'Cluster {i+1}'
    )

plt.title('Customer Segments')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

# save dataset with cluster labels
df.to_csv('data/Mall_Customers_Clustered.csv', index=False)

print("Clustered dataset saved as 'Mall_Customers_Clustered.csv'")