import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sales = pd.read_csv("sales_data.csv")
# print(sales.head())
# print(sales.shape)
# print(sales.columns)
# print(sales.info())
# print(sales.describe())

# print(sales["Revenue"].sum())
# print(sales["Profit"].sum())
# print(sales["Quantity"].sum())

category_revenue = sales.groupby("Category")["Revenue"].sum()
# print(category_revenue)
# print(sales.groupby("Category")["Revenue"].sum().idxmax())
# print(sales.groupby("Region")["Profit"].sum())
# print(sales.groupby("Region")["Profit"].sum().idxmax())

top5_product = sales.groupby("Product")["Revenue"].sum().sort_values(ascending = False).head(5)
# print(top5_product)
# print(sales["Revenue"].mean())
# print(sales.groupby("Product")["Profit"].sum().idxmax())
total_revenue = sales.groupby("Category")["Revenue"].sum()
total_profit = sales.groupby("Category")["Profit"].sum()
# profit_margin = (total_profit / total_revenue) * 100
# print("Profit Margin : ", profit_margin)

sales["Date"] = pd.to_datetime(sales["Date"])
# print(sales["Date"].dtype)
sales["Month"] = sales["Date"].dt.month_name()
monthly_revenue = sales.groupby("Month")["Revenue"].sum()
# print(monthly_revenue)
# print(sales.groupby("Month")["Revenue"].sum().idxmax())
monthly_profit = sales.groupby("Month")["Profit"].sum()
# print(monthly_profit)
# print(sales.groupby("Month")["Profit"].sum().idxmax())

# plt.plot(
#     monthly_revenue.index,
#     monthly_revenue.values,
#     marker = "o"
# )
# plt.title("Monthly Revenue")
# plt.xlabel("Month")
# plt.ylabel("Total_revenue")
# plt.grid()
# plt.show()

# plt.plot(
#     monthly_profit.index,
#     monthly_profit.values,
#     marker = "o"
# )
# plt.title("Monthly Profit")
# plt.xlabel("Month")
# plt.ylabel("Total_profit")
# plt.grid()
# plt.show()

# plt.bar(
#     category_revenue.index,
#     category_revenue.values,
#     color = "orange"
# )
# plt.title("Revenue By Category")
# plt.xlabel("Category")
# plt.ylabel("Total Revenue")
# plt.grid()
# plt.show()

# plt.bar(
#     total_profit.index,
#     total_profit.values,
#     color = "red"
# )
# plt.title("Profit By Category")
# plt.xlabel("Category")
# plt.ylabel("Profit")
# plt.grid()
# plt.show()

# plt.bar(
#     top5_product.index,
#     top5_product.values,
#     color = "green"
# )
# plt.title("Top 5 Products by Revenue")
# plt.xlabel('Products')
# plt.ylabel('Total Revenue')
# plt.grid()
# plt.show()

# sns.boxplot(
#     data = sales,
#     x = "Category",
#     y = "Revenue"
# )
# plt.title("Revenue Distribution by Category")
# plt.show()

# sns.scatterplot(
#     data =sales,
#     x = "Quantity",
#     y = "Revenue",
#     hue = "Category"
# )
# plt.title("Revenue vs Quantity by Category")
# plt.show()

# sns.scatterplot(
#     data =sales,
#     x = "Quantity",
#     y = "Revenue",
#     hue = "Category",
#     style = "Category"
# )
# plt.title("Revenue vs Quantity by Category")
# plt.show()

# sns.regplot(
#     data = sales,
#     x = "Quantity",
#     y = "Revenue"
# )
# plt.title("Revenue vs Quantity — Regression")
# plt.show()

# print(sales["Quantity"].corr(sales["Revenue"]))

# print(np.sum(sales["Revenue"] > 50000))
# sales["Sales_Level"] = np.where( sales["Revenue"]>= 50000, "High", "Normal")
# print(sales[["Revenue", "Sales_Level"]].head(10))

sales["Sales_Level"] = np.where(sales["Revenue"] >= 70000, "Very High", (np.where(sales["Revenue"] >= 50000, "High", "Normal")))
# print(sales[["Revenue", "Sales_Level"]].head(10))

# print(np.sum(sales["Sales_Level"] == "Very High"))

# print(sales.groupby("Category")["Sales_Level"].value_counts())
# print(sales[sales["Sales_Level"] == "Very High"]["Category"].value_counts().idxmax())
print(sales.groupby("Category")["Revenue"].mean().idxmax())