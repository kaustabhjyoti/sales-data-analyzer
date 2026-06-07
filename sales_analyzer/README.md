# 📊 Sales Data Analyzer

A Python project that analyzes sales data, generates insights, and produces visualizations.

## 🔧 Tech Stack

- Python 3.13
- Pandas — data manipulation
- Matplotlib & Seaborn — data visualization
- OpenPyXL — Excel report generation

## 📈 Features

- Loads and cleans raw sales CSV data
- Calculates revenue by Category, City, Product and Month
- Generates 4 charts saved as PNG files
- Exports a multi-sheet Excel summary report

## 📊 Key Insights Found

- Total Revenue: ₹7,87,500
- Top Category: Electronics (78% of revenue)
- Top City: Hyderabad
- Best Product: Laptop (₹3,30,000)

## 🚀 How to Run

```bash
pip install pandas matplotlib seaborn openpyxl
python analyzer.py   # generates charts
python report.py     # generates Excel report
```

## 📁 Output Files

- `chart1_category.png`
- `chart2_city.png`
- `chart3_monthly.png`
- `chart4_products.png`
- `sales_report.xlsx`
