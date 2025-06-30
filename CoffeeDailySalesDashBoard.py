#import pandas as pd
# Scenario: You are a sales analyst. You have CSV files of daily sales (Date, Product, Units, Revenue)

# Practice Goals:

# Read the CSV

# Create a summary: total revenue per product

# Add a new column: Revenue per Unit

# Filter top 5 products with highest sales

# Export summary to Excel . give the link for excel sheet
# and solve it too

import pandas as pd
df = pd.read_excel("C:\\Users\\alimo\\Downloads\\Coffee Shop Sales.xlsx\\Coffee Shop Sales.xlsx")
# Inspect the data
print("Data Loaded:", df.shape)
print(df.head())

# Step 2: Add total units per product
unit_summary = (
    df.groupby("product_category")["unit_price"]
      .sum()
      .reset_index(name="Total_Units")
)



# Step 4: Filter top 5 products by total revenue
unit_summary["Revenue_per_Unit"] = unit_summary["Total_Units"] / df["store_id"]
top5 = unit_summary.sort_values("Total_Units", ascending=False).head(5)
print("\nTop 5 Products by Revenue:\n", top5)
# Step 5: Export to Excel
output_path = "daily_sales_summary.xlsx"
top5.to_excel(output_path, index=False)
print(f"\n✅ Summary exported to '{output_path}'")
