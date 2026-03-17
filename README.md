# Customer Segmentation with K-Means

## 📌 Project Overview
This project demonstrates **customer segmentation** using the **Mall Customers dataset**.  
The goal is to group customers based on **Annual Income** and **Spending Score** using **K-Means Clustering**, which helps businesses identify different customer types for marketing and strategy.

---

## 🛠️ Technologies & Libraries
- **Python 3**
- **pandas** — data manipulation
- **matplotlib & seaborn** — data visualization
- **scikit-learn** — K-Means clustering

---

## 📊 Dataset
- Source: Mall Customers Dataset  
- Contains **200 customers** with 5 columns:  
  - `CustomerID` — unique ID  
  - `Genre` — Male/Female  
  - `Age` — age of the customer  
  - `Annual Income (k$)` — income in thousands  
  - `Spending Score (1-100)` — spending score

---

## 🚀 How it Works
1. Load dataset using **pandas**  
2. Explore data with `info()` and `describe()`  
3. Visualize customer distribution using a **scatter plot**  
4. Apply **K-Means clustering** (5 clusters) on Income vs Spending Score  
5. Visualize clusters with **color-coded scatter plot**  
6. Save the clustered dataset as `Mall_Customers_Clustered.csv`

---

## 🔍 Observations
- Customers naturally form clusters based on spending and income  
- Clusters can be used to identify:  
  - High spenders with high income  
  - Low spenders with low income  
  - Other mixed groups for targeted marketing  

---

## 🗂️ Project Structure
