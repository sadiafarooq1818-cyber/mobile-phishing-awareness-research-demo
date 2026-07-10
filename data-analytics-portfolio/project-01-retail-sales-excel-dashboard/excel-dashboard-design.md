# Excel Dashboard Design Guide

## Data Preparation Steps

1. Convert the sales dataset into an Excel Table.
2. Check missing values in key fields: order date, region, category, sales and profit.
3. Add helper columns:
   - Month: `=TEXT([@[order_date]],"mmm yyyy")`
   - Profit Margin: `=[@profit]/[@sales]`
   - Average Order Value: `=[@sales]/[@quantity]`
4. Create PivotTables from the cleaned table.
5. Build dashboard visuals from PivotCharts.

## Recommended PivotTables

### 1. Monthly Revenue Trend
- Rows: Month
- Values: Sum of Sales, Sum of Profit

### 2. Region Performance
- Rows: Region
- Values: Sum of Sales, Sum of Profit, Count of Order ID

### 3. Category Performance
- Rows: Product Category
- Values: Sum of Sales, Sum of Quantity, Sum of Profit

### 4. Customer Segment Performance
- Rows: Customer Segment
- Values: Sum of Sales, Sum of Profit

### 5. Top Products
- Rows: Product Name
- Values: Sum of Sales
- Sort: Largest to Smallest

## Dashboard KPI Cards

- Total Sales: `=SUM(Table1[sales])`
- Total Profit: `=SUM(Table1[profit])`
- Profit Margin: `=SUM(Table1[profit])/SUM(Table1[sales])`
- Total Orders: `=COUNTA(Table1[order_id])`
- Total Quantity: `=SUM(Table1[quantity])`

## Suggested Visuals

- Line chart: Monthly sales and profit trend
- Bar chart: Sales by region
- Column chart: Sales by product category
- Donut chart: Sales by customer segment
- Table: Top 10 products by revenue

## Dashboard Filters

Use slicers for:

- Region
- Customer Segment
- Product Category
- Month

## Business Insight Examples

- Technology generates the highest revenue and strongest profit contribution.
- NSW and WA show strong revenue concentration.
- Discounts should be monitored because high discounting can reduce margin.
- Corporate customers show higher average order value compared with consumer segments.

## Recruiter-Relevant Skills Demonstrated

- Excel reporting
- PivotTable analysis
- KPI dashboarding
- Data validation
- Business performance reporting
- Dashboard documentation
- Stakeholder-ready summaries