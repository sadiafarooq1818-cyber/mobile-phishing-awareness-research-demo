-- Customer & Revenue Analysis SQL Portfolio Project
-- Dataset: retail_sales_sample.csv loaded into table fact_sales
-- Purpose: Demonstrate SQL analysis for reporting, business intelligence and decision support.

-- 1. Preview dataset
SELECT
    order_id,
    order_date,
    region,
    customer_segment,
    product_category,
    product_name,
    sales,
    quantity,
    discount,
    profit
FROM fact_sales
LIMIT 10;

-- 2. Total sales, profit, quantity and order count
SELECT
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(profit) / NULLIF(SUM(sales), 0), 4) AS profit_margin
FROM fact_sales;

-- 3. Monthly sales and profit trend
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS sales_month,
    ROUND(SUM(sales), 2) AS monthly_sales,
    ROUND(SUM(profit), 2) AS monthly_profit,
    COUNT(DISTINCT order_id) AS orders
FROM fact_sales
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY sales_month;

-- 4. Revenue and profit by region
SELECT
    region,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(profit) / NULLIF(SUM(sales), 0), 4) AS profit_margin
FROM fact_sales
GROUP BY region
ORDER BY total_sales DESC;

-- 5. Product category performance
SELECT
    product_category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    SUM(quantity) AS total_quantity,
    ROUND(AVG(discount), 4) AS average_discount
FROM fact_sales
GROUP BY product_category
ORDER BY total_sales DESC;

-- 6. Customer segment performance
SELECT
    customer_segment,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS orders,
    ROUND(SUM(sales) / NULLIF(COUNT(DISTINCT order_id), 0), 2) AS average_order_value
FROM fact_sales
GROUP BY customer_segment
ORDER BY total_sales DESC;

-- 7. Top 10 products by revenue
SELECT
    product_name,
    product_category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    SUM(quantity) AS total_quantity
FROM fact_sales
GROUP BY product_name, product_category
ORDER BY total_sales DESC
LIMIT 10;

-- 8. Identify high-discount orders for review
SELECT
    order_id,
    order_date,
    region,
    product_category,
    product_name,
    sales,
    discount,
    profit,
    CASE
        WHEN discount >= 0.10 THEN 'High discount - review margin'
        ELSE 'Normal discount'
    END AS discount_flag
FROM fact_sales
WHERE discount >= 0.10
ORDER BY discount DESC, sales DESC;

-- 9. Margin performance by order
SELECT
    order_id,
    product_name,
    sales,
    profit,
    ROUND(profit / NULLIF(sales, 0), 4) AS order_margin,
    CASE
        WHEN profit / NULLIF(sales, 0) >= 0.20 THEN 'Strong margin'
        WHEN profit / NULLIF(sales, 0) >= 0.10 THEN 'Moderate margin'
        ELSE 'Low margin - investigate'
    END AS margin_category
FROM fact_sales
ORDER BY order_margin ASC;

-- 10. Data quality checks
SELECT
    COUNT(*) AS total_rows,
    SUM(CASE WHEN order_id IS NULL OR order_id = '' THEN 1 ELSE 0 END) AS missing_order_id,
    SUM(CASE WHEN order_date IS NULL THEN 1 ELSE 0 END) AS missing_order_date,
    SUM(CASE WHEN sales IS NULL THEN 1 ELSE 0 END) AS missing_sales,
    SUM(CASE WHEN profit IS NULL THEN 1 ELSE 0 END) AS missing_profit,
    SUM(CASE WHEN sales <= 0 THEN 1 ELSE 0 END) AS non_positive_sales
FROM fact_sales;

-- 11. Duplicate order check
SELECT
    order_id,
    COUNT(*) AS row_count
FROM fact_sales
GROUP BY order_id
HAVING COUNT(*) > 1;

-- 12. Region and category cross-tab style summary
SELECT
    region,
    product_category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM fact_sales
GROUP BY region, product_category
ORDER BY region, total_sales DESC;
