# Power BI DAX Measures

These measures can be used in Power BI after importing the retail sales dataset.

## Core Measures

```DAX
Total Sales = SUM(fact_sales[sales])
```

```DAX
Total Profit = SUM(fact_sales[profit])
```

```DAX
Total Quantity = SUM(fact_sales[quantity])
```

```DAX
Total Orders = DISTINCTCOUNT(fact_sales[order_id])
```

```DAX
Profit Margin = DIVIDE([Total Profit], [Total Sales])
```

```DAX
Average Order Value = DIVIDE([Total Sales], [Total Orders])
```

```DAX
Average Discount = AVERAGE(fact_sales[discount])
```

## Time Intelligence Measures

```DAX
Sales MTD = TOTALMTD([Total Sales], dim_date[Date])
```

```DAX
Sales YTD = TOTALYTD([Total Sales], dim_date[Date])
```

```DAX
Previous Month Sales =
CALCULATE(
    [Total Sales],
    DATEADD(dim_date[Date], -1, MONTH)
)
```

```DAX
Sales Growth % =
DIVIDE(
    [Total Sales] - [Previous Month Sales],
    [Previous Month Sales]
)
```

## Performance Measures

```DAX
High Margin Flag =
IF([Profit Margin] >= 0.20, "High Margin", "Review Required")
```

```DAX
Discount Risk =
IF([Average Discount] > 0.10, "High Discount", "Normal")
```

## Suggested Visual Mapping

- KPI Cards: Total Sales, Total Profit, Profit Margin, Total Orders
- Line Chart: Total Sales by Month
- Bar Chart: Total Sales by Region
- Column Chart: Profit by Product Category
- Matrix: Product Category x Region
- Table: Top Products by Sales
- Slicers: Region, Customer Segment, Product Category, Month

## Documentation Notes

Each KPI should include a definition so business users understand what the metric means. This supports data governance, consistency and stakeholder trust.