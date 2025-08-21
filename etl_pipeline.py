import pandas as pd
from sqlalchemy import create_engine

# connect to SQLite
engine = create_engine("sqlite:///warehouse.db")

# sample raw data
sales = pd.DataFrame({
    "sale_id":[1,2,3],
    "product_name":["Laptop","Smartphone","Tablet"],
    "category":["Electronics","Electronics","Electronics"],
    "customer_name":["Alice","Bob","Charlie"],
    "gender":["F","M","M"],
    "age_group":["25-34","35-44","18-24"],
    "region_name":["North","South","East"],
    "date":["2023-05-01","2023-05-02","2023-05-03"],
    "units_sold":[5,10,3],
    "revenue":[5000,7000,1500]
})

# Dimension tables
dim_product = sales[["product_name","category"]].drop_duplicates().reset_index(drop=True)
dim_product["product_id"] = dim_product.index+1

dim_customer = sales[["customer_name","gender","age_group"]].drop_duplicates().reset_index(drop=True)
dim_customer["customer_id"] = dim_customer.index+1

dim_region = sales[["region_name"]].drop_duplicates().reset_index(drop=True)
dim_region["region_id"] = dim_region.index+1

dim_time = pd.DataFrame({"date":sales["date"].unique()})
dim_time["date"] = pd.to_datetime(dim_time["date"])
dim_time["time_id"] = dim_time.index+1
dim_time["year"] = dim_time["date"].dt.year
dim_time["quarter"] = dim_time["date"].dt.quarter
dim_time["month"] = dim_time["date"].dt.month

# Fact table
fact_sales = sales.merge(dim_product, on=["product_name","category"])
fact_sales = fact_sales.merge(dim_customer, on=["customer_name","gender","age_group"])
fact_sales = fact_sales.merge(dim_region, on="region_name")
fact_sales = fact_sales.merge(dim_time, on="date")
fact_sales = fact_sales[["sale_id","product_id","customer_id","region_id","time_id","units_sold","revenue"]]

# Load into warehouse
dim_product.to_sql("dim_product", engine, if_exists="replace", index=False)
dim_customer.to_sql("dim_customer", engine, if_exists="replace", index=False)
dim_region.to_sql("dim_region", engine, if_exists="replace", index=False)
dim_time.to_sql("dim_time", engine, if_exists="replace", index=False)
fact_sales.to_sql("fact_sales", engine, if_exists="replace", index=False)

print("ETL complete. Data loaded into warehouse.db")
