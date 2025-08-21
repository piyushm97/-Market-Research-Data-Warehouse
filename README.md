# 📊 Market Research Data Warehouse

A **data warehouse project** that integrates survey and sales data for market research insights.  
Implements a **star schema**, an **ETL pipeline**, and **sample BI queries**.

## 🚀 Features
- 🗄️ Star Schema (Fact + Dimension tables)
- 🛠️ Python ETL pipeline for cleaning/loading data
- 📊 Example BI queries (e.g., product trends, demographics, regional sales)
- 📓 Jupyter Notebook demo

## 📂 Schema Design
**Fact Table**  
- `fact_sales` → sales transactions  

**Dimensions**  
- `dim_product`  
- `dim_customer`  
- `dim_region`  
- `dim_time`  

## ⚡ How to Run

### 1. Setup
```bash
git clone https://github.com/piyushm97/market-research-data-warehouse.git
cd market-research-data-warehouse
pip install -r requirements.txt
```

### 2. Run ETL
```bash
python etl/etl_pipeline.py
```

### 3. Load Schema (SQLite example)
```bash
sqlite3 warehouse.db < sql/create_schema.sql
sqlite3 warehouse.db < sql/insert_sample_data.sql
```

### 4. Run Queries
```bash
sqlite3 warehouse.db < sql/queries.sql
```

---

## 🧑‍💻 Author
**Piyush Mahajan**  
🔗 [LinkedIn](https://www.linkedin.com/in/piyushm97/)  
📂 [GitHub](https://github.com/piyushm97)
