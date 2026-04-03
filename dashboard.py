import pandas as pd
import matplotlib.pyplot as plt
# Load data
df=pd.read_csv("C:/Users/BHARATH SIMHA REDDY/OneDrive/Desktop/sales-dasshboard-project/sales_data.csv")

#print(df.head())
#print(df.tail())
#print(df.info())

#convert Order_date to datetime type
df["Order_Date"]=pd.to_datetime(df["Order_Date"])

# Extract month name and make categorical order 
months_order = ['January','February','March','April','May','June','July','August','September','October','November','December']
df['Month_Name']=df['Order_Date'].dt.month_name()
df["Month_Name"] = pd.Categorical(df['Month_Name'], categories=months_order, ordered=True)

#Aggregate Data

monthly_sales = df.groupby("Month_Name", observed=True)["Sales"].sum().reset_index()
print(monthly_sales)
top_products = df.groupby("Product_Name")["Sales"].sum().sort_values(ascending=False).head(3)
print(top_products)
Region_sales=df.groupby("Region")["Sales"].sum()
print(Region_sales)
Profit_by_Category=df.groupby("Category")["Profit"].sum()
print(Profit_by_Category)

#Mini Dashboard
fig , axs = plt.subplots(2, 2, figsize=(12,8))
fig.suptitle("Sales Data Dashboard", fontsize=16, fontweight='bold')
# Line chart for Monthly sales

axs[0,0].plot(monthly_sales["Month_Name"], monthly_sales["Sales"] , marker="o", color="#1f77b4")
axs[0,0].set_title("Monthly Sales")
axs[0,0].set_xlabel("Month")
axs[0,0].set_ylabel("Sales")
#plt.xticks(rotation=45)"#1f77b4",,"2ca02c"])#
axs[0,0].grid(True)
# Bar chart for Region by Sales
top_products.plot(kind="bar", ax=axs[0,1], color="#ff7f0e")
axs[0,1].set_title("Top 3 Products by Sales")
axs[0,1].set_xlabel("Product_Name")
axs[0,1].set_ylabel("Sales")
axs[0,1].tick_params(axis="x",rotation=45)
axs[0,1].grid(True)
for i, v in enumerate(top_products.values):
        axs[0,1].text(i, v, str(v), ha='center', va='bottom')
# Bar Chart for sales by category
Region_sales.plot(kind="bar", ax=axs[1,0],color="#2ca02c")
axs[1,0].set_title("Sales by Region")
axs[1,0].set_xlabel("Region")
axs[1,0].set_ylabel("Sales")
axs[1,0].tick_params(axis="x",rotation=45)
axs[1,0].grid(True)
for i, v in enumerate(Region_sales.values):
        axs[1,0].text(i, v, str(v), ha='center', va='bottom')
# Pie chart for profit contribution by category
axs[1,1].pie(Profit_by_Category, labels= Profit_by_Category.index, autopct="%1.1f%%", startangle=90, colors=["#1f77b4","#ff7f0e","#2ca02c"])
axs[1,1].set_title("Profit contribution by Category")
axs[1,1].axis("equal")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("output.png")
plt.show()

