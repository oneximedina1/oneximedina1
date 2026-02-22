-- E-Commerce Database Analysis
-- Tables assumed: orders, order_items, products, customers

-- 1. Total revenue per month
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(total_amount)               AS monthly_revenue,
    COUNT(*)                        AS total_orders
FROM orders
WHERE order_status = 'completed'
GROUP BY 1
ORDER BY 1;

-- 2. Top 10 best-selling products by revenue
SELECT
    p.product_name,
    SUM(oi.quantity)              AS units_sold,
    SUM(oi.quantity * oi.price)   AS total_revenue
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_revenue DESC
LIMIT 10;

-- 3. Customer lifetime value (top 20 customers)
SELECT
    c.customer_id,
    c.email,
    COUNT(o.order_id)    AS total_orders,
    SUM(o.total_amount)  AS lifetime_value,
    AVG(o.total_amount)  AS avg_order_value
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
WHERE o.order_status = 'completed'
GROUP BY c.customer_id, c.email
ORDER BY lifetime_value DESC
LIMIT 20;

-- 4. Repeat vs. one-time customers
SELECT
    CASE
        WHEN order_count = 1 THEN 'One-time'
        ELSE 'Repeat'
    END                     AS customer_type,
    COUNT(*)                AS customer_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS pct
FROM (
    SELECT customer_id, COUNT(order_id) AS order_count
    FROM orders
    WHERE order_status = 'completed'
    GROUP BY customer_id
) sub
GROUP BY 1;

-- 5. Month-over-month revenue growth
WITH monthly AS (
    SELECT
        DATE_TRUNC('month', order_date) AS month,
        SUM(total_amount)               AS revenue
    FROM orders
    WHERE order_status = 'completed'
    GROUP BY 1
)
SELECT
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month)                          AS prev_revenue,
    ROUND((revenue - LAG(revenue) OVER (ORDER BY month))
          / NULLIF(LAG(revenue) OVER (ORDER BY month), 0) * 100, 2) AS growth_pct
FROM monthly
ORDER BY month;
