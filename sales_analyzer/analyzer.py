import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load & Prepare (same as before) ───────────────────
df = pd.read_csv("sales_data.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.strftime("%b")
df["Month Number"] = df["Order Date"].dt.month
df["Revenue"] = df["Quantity"] * df["Unit Price"]

# ── Style ──────────────────────────────────────────────
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)

# ══════════════════════════════════════════════════════
# CHART 1 — Revenue by Category (Bar Chart)
# ══════════════════════════════════════════════════════
cat_rev = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

plt.figure()
sns.barplot(x=cat_rev.index, y=cat_rev.values, palette="Blues_d")
plt.title("Revenue by Category", fontsize=16, fontweight="bold")
plt.xlabel("Category")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.savefig("chart1_category.png", dpi=150)
plt.show()
print("✅ Chart 1 saved!")

# ══════════════════════════════════════════════════════
# CHART 2 — Revenue by City (Horizontal Bar)
# ══════════════════════════════════════════════════════
city_rev = df.groupby("City")["Revenue"].sum().sort_values()

plt.figure()
sns.barplot(x=city_rev.values, y=city_rev.index, palette="Greens_d")
plt.title("Revenue by City", fontsize=16, fontweight="bold")
plt.xlabel("Revenue (₹)")
plt.ylabel("City")
plt.tight_layout()
plt.savefig("chart2_city.png", dpi=150)
plt.show()
print("✅ Chart 2 saved!")

# ══════════════════════════════════════════════════════
# CHART 3 — Monthly Revenue Trend (Line Chart)
# ══════════════════════════════════════════════════════
monthly = df.groupby(["Month Number", "Month"])["Revenue"].sum().reset_index()
monthly = monthly.sort_values("Month Number")

plt.figure()
sns.lineplot(x="Month", y="Revenue", data=monthly,
             marker="o", linewidth=2.5, color="steelblue")
plt.title("Monthly Revenue Trend", fontsize=16, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.savefig("chart3_monthly.png", dpi=150)
plt.show()
print("✅ Chart 3 saved!")

# ══════════════════════════════════════════════════════
# CHART 4 — Top Products (Bar Chart)
# ══════════════════════════════════════════════════════
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

plt.figure()
sns.barplot(x=top_products.values, y=top_products.index, palette="Oranges_d")
plt.title("Revenue by Product", fontsize=16, fontweight="bold")
plt.xlabel("Revenue (₹)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("chart4_products.png", dpi=150)
plt.show()
print("✅ Chart 4 saved!")

print("\n🎉 All 4 charts saved in your project folder!")