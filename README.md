# Ecommerce Analytics Project

An end-to-end data analytics project that simulates an ecommerce system.  
The project covers **data generation**, **data ingestion**, and **customer spending analysis**
using **Python, Pandas, SQLite, and SQL**.

---

## 📌 Project Overview

This project demonstrates a real-world data pipeline workflow:

1. Generate synthetic ecommerce data (customers, products, orders)
2. Store the data as CSV files
3. Ingest CSV data into a SQLite database
4. Run SQL-based analytics to find top customers by spending

---

## 🧱 Dataset Structure

The project generates the following datasets:

- **Customers**
  - customer_id, name, email, country, signup_date

- **Products**
  - product_id, product_name, category, price

- **Orders**
  - order_id, customer_id, order_date, status

- **Order Items**
  - item_id, order_id, product_id, quantity, price_at_purchase

- **Payments**
  - payment_id, order_id, amount, payment_method, payment_date

---

## 🛠️ Tech Stack

- **Programming Language**: Python
- **Libraries**: Pandas, Faker
- **Database**: SQLite
- **Query Language**: SQL
- **Version Control**: Git & GitHub

## How to Run the Project

**Important:**  
All three Python scripts must be placed in a single folder and executed in the order shown below.

### Project Structure

    project-root/
    ├── generate_data.py
    ├── ingest_db.py
    ├── analyze_sales.py

---

### Step 1: Generate Data

```bash
python generate_data.py
```

This will generate 5 CSV files **(customers, products, orders, order_items, payments)** which will be stored in the **data** subfolder that is created automatically.

---
### Step 2: Ingest Data to sqlite

```bash
python ingest_db.py
```

This will ingest the CSV files into SQLite to create SQL tables, which will be further utilized for analysis

---
### Step 3: Data Analysis Using SQL

```bash
python analyze_sales.py
```

This will run the SQL query that returns the top 5 spenders among the customers.

### Example Output
```text
--- Top 5 Customers by Total Spending ---
customer_name        customer_email                total_orders   total_spent
Joseph Martinez      calebsmith@example.net        2              3510.36
Kimberly Smith       housemelinda@example.org      1              3316.40
Monica Herrera       smiller@example.net           3              3200.70
Jennifer Cole        lisa02@example.net            2              2998.90
Frederick Tate       perezantonio@example.com      1              2857.60

```
### Included Example Data

This repository includes:
- Example generated CSV files (`customers.csv`, `products.csv`, `orders.csv`, `order_items.csv`, `payments.csv`)
- The generated SQLite database file (`ecommerce.db`)

These files are provided for reference so the project can be explored and the analysis can be run immediately without regenerating the data.


