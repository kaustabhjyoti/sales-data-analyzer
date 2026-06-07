import pandas as pd

# ── Load & Prepare ─────────────────────────────────────
df = pd.read_csv("sales_data.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.strftime("%b")
df["Month Number"] = df["Order Date"].dt.month
df["Revenue"] = df["Quantity"] * df["Unit Price"]

# ── Build Summary Tables ───────────────────────────────
category_summary = df.groupby("Category")["Revenue"].sum().reset_index()
category_summary.columns = ["Category", "Total Revenue"]
category_summary = category_summary.sort_values("Total Revenue", ascending=False)

city_summary = df.groupby("City")["Revenue"].sum().reset_index()
city_summary.columns = ["City", "Total Revenue"]
city_summary = city_summary.sort_values("Total Revenue", ascending=False)

product_summary = df.groupby("Product")["Revenue"].sum().reset_index()
product_summary.columns = ["Product", "Total Revenue"]
product_summary = product_summary.sort_values("Total Revenue", ascending=False)

monthly_summary = df.groupby(["Month Number","Month"])["Revenue"].sum().reset_index()
monthly_summary = monthly_summary.sort_values("Month Number")
monthly_summary = monthly_summary[["Month", "Revenue"]]

# ── KPI Summary ────────────────────────────────────────
kpi = pd.DataFrame({
    "Metric": [
        "Total Revenue",
        "Total Orders",
        "Average Order Value",
        "Best City",
        "Best Category",
        "Best Product"
    ],
    "Value": [
        f"₹ {df['Revenue'].sum():,}",
        str(len(df)),
        f"₹ {int(df['Revenue'].mean()):,}",
        city_summary.iloc[0]["City"],
        category_summary.iloc[0]["Category"],
        product_summary.iloc[0]["Product"]
    ]
})

# ── Write to Excel (multiple sheets) ──────────────────
with pd.ExcelWriter("sales_report.xlsx", engine="openpyxl") as writer:
    kpi.to_excel(writer, sheet_name="KPI Summary", index=False)
    df.to_excel(writer, sheet_name="Raw Data", index=False)
    category_summary.to_excel(writer, sheet_name="By Category", index=False)
    city_summary.to_excel(writer, sheet_name="By City", index=False)
    product_summary.to_excel(writer, sheet_name="By Product", index=False)
    monthly_summary.to_excel(writer, sheet_name="Monthly Trend", index=False)

print("✅ sales_report.xlsx created with 6 sheets!")
print("\n📊 KPI Summary:")
print(kpi.to_string(index=False))