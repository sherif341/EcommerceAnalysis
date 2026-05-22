[README.md](https://github.com/user-attachments/files/28161394/README.md)
# 🛒 E-Commerce Orders Analysis

A Python-based data analysis project that processes raw e-commerce order data, cleans it, and generates actionable insights on **sales revenue** and **product performance** — complete with visual charts and exported reports.

---

## 📌 Overview

This project takes a real-world e-commerce orders dataset (`ecommerce_orders.xlsx`), applies thorough data cleaning and preprocessing, and produces business-ready analysis covering category revenue, best-selling products, and monthly sales trends.

---

## 🎯 What This Project Analyzes

- 💰 **Revenue by Category** — Which product categories generate the most sales
- 🏆 **Best-Selling Products** — Top items ranked by units sold
- 📅 **Monthly Sales Trends** — How revenue moves across time
- 💳 **Payment Method Distribution** — Customer payment preferences
- 📦 **Order Status Breakdown** — Delivered, cancelled, pending, etc.

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| `pandas` | Data loading, cleaning & aggregation |
| `numpy` | Numerical operations & null handling |
| `matplotlib` | Bar charts and visualizations |
| `openpyxl` | Reading & writing Excel files |

---

## 📁 Project Structure

```
EcommerceAnalysis/
│
├── ecommerce_orders.xlsx        # Raw input dataset
├── POne.py                      # Main analysis script
│
├── Cleaned_ecommerce_orders.xlsx  # Cleaned output dataset
├── report_of_category.csv         # Category-level sales report
└── report_of_product.csv          # Product-level sales report
```

---

## 🔄 Data Pipeline

### 1. Data Cleaning
- Standardized column names (lowercase, stripped whitespace)
- Cleaned text fields: `customer_name`, `order_id`, `product`, `category`, `payment_method`, `status`
- Parsed and validated `order_date` as datetime
- Converted `quantity` and `price` to numeric types
- Filled missing prices using **per-product median** (group-wise imputation)
- Dropped rows with missing `order_date` or `quantity`
- Detected duplicate `order_id` entries for review

### 2. Feature Engineering
- `total` — calculated as `price × quantity` per order line
- `year` — extracted from `order_date`
- `month` — extracted as monthly period for time-series analysis

### 3. Aggregations
- **Category Sales** — total revenue & units sold per category
- **Product Sales** — total units and revenue per product, sorted by popularity
- **Monthly Sales** — total revenue per month
- **Payment Method** — frequency count per method
- **Order Status** — frequency count per status

---

## 📊 Output Visualizations

| Chart | Description |
|---|---|
| `Revenue by Category` | Bar chart comparing total revenue across product categories |
| `Best Seller Items` | Horizontal bar chart ranking products by quantity sold |

---

## 📤 Output Files

| File | Description |
|---|---|
| `Cleaned_ecommerce_orders.xlsx` | Fully cleaned version of the original dataset |
| `report_of_category.csv` | Aggregated sales report by category |
| `report_of_product.csv` | Aggregated sales report by product |

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/sherif341/EcommerceAnalysis.git
cd EcommerceAnalysis
```

### 2. Install dependencies
```bash
pip install pandas numpy matplotlib openpyxl
```

### 3. Add your dataset
Place your `ecommerce_orders.xlsx` file in the root project directory.

### 4. Run the script
```bash
python POne.py
```

The script will display charts and export the cleaned data and reports automatically.

---

## 📋 Dataset Columns Expected

| Column | Type | Description |
|---|---|---|
| `order_id` | String | Unique order identifier |
| `customer_name` | String | Name of the customer |
| `order_date` | Date | Date the order was placed |
| `product` | String | Product name |
| `category` | String | Product category |
| `quantity` | Integer | Number of units ordered |
| `price` | Float | Unit price |
| `payment_method` | String | Payment method used |
| `status` | String | Order status (e.g. Delivered, Cancelled) |

---

## 👤 Author

**Sherif**
- GitHub: [@sherif341](https://github.com/sherif341)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
