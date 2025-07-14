

SELECT
    employee,
    month,
    amount,

    -- 1. Unique row number per employee
    ROW_NUMBER() OVER (PARTITION BY employee ORDER BY month) AS row_num,

    -- 2. Rank with gaps for same amount
    RANK() OVER (PARTITION BY employee ORDER BY amount DESC) AS rank_with_gaps,

    -- 3. Rank without gaps
    DENSE_RANK() OVER (PARTITION BY employee ORDER BY amount DESC) AS dense_rank,

    -- 4. Split rows into 2 equal buckets
    NTILE(2) OVER (PARTITION BY employee ORDER BY amount DESC) AS ntile_2,

    -- 5. Amount in previous month
    LAG(amount) OVER (PARTITION BY employee ORDER BY month) AS prev_amount,

    -- 6. Amount in next month
    LEAD(amount) OVER (PARTITION BY employee ORDER BY month) AS next_amount,

    -- 7. First month's amount for each employee
    FIRST_VALUE(amount) OVER (PARTITION BY employee ORDER BY month) AS first_month_amount,

    -- 8. Last month's amount for each employee
    LAST_VALUE(amount) OVER (PARTITION BY employee ORDER BY month ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_month_amount,

    -- 9. Running total by month
    SUM(amount) OVER (PARTITION BY employee ORDER BY month) AS running_total,

    -- 10. Running average by month
    AVG(amount) OVER (PARTITION BY employee ORDER BY month) AS running_avg

FROM Sales;
