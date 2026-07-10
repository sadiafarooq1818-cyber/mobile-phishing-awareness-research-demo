# Project 02: Power BI Retail Performance Dashboard

## Business Objective

This project demonstrates a Power BI dashboard concept for a medium-sized retail business. The dashboard is designed to help managers monitor revenue, profit, product category performance, regional results and monthly trends.

## Business Questions

- How is revenue trending month by month?
- Which region contributes the highest sales and profit?
- Which product categories perform best?
- Which customer segments generate stronger revenue?
- Where should management focus performance improvement?

## Dataset

Use the sample dataset from:

`../project-01-retail-sales-excel-dashboard/data/retail_sales_sample.csv`

## Suggested Power BI Model

### Fact Table

`fact_sales`

Fields:

- order_id
- order_date
- region
- state
- customer_segment
- product_category
- product_name
- sales
- quantity
- discount
- profit

### Dimension Tables

- `dim_date`
- `dim_region`
- `dim_product`
- `dim_customer_segment`

## Dashboard Pages

### Page 1: Executive Overview

- Total Sales
- Total Profit
- Profit Margin
- Total Orders
- Sales Trend by Month
- Sales by Region
- Sales by Category

### Page 2: Operational Performance

- Sales by customer segment
- Profit by product category
- Discount impact review
- Top 10 products by revenue

### Page 3: Data Quality & Definitions

- Data refresh date
- KPI definitions
- Data assumptions
- Known limitations

## Power BI Skills Demonstrated

- Dashboard design
- DAX measures
- KPI reporting
- Data modelling concepts
- Data visualisation principles
- Business intelligence documentation
- Stakeholder-focused insights

## Recruiter-Relevant Keywords

Business Intelligence, Power BI, Data Visualisation, Dashboard Development, KPI Reporting, Performance Reporting, Data Modelling, Data Quality, Data Documentation, Decision Support.