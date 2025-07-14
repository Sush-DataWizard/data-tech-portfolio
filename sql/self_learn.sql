


/*

Input

    col1|col2|col3

    one | aa | 1
    one | aa | 2
    two | bb | 3
    two | bb | 4
    two | bb | 5

Output

    col1|col2|col3_list

    one | aa | [1, 2]
    two | bb | [3, 4, 5]

*/

SELECT
    col1,
    col2,
    COLLECT_LIST(col3) AS col3_list
FROM
    input_table
GROUP BY
    col1, col2


------------------------------------------------------------------------------------------------------------

-- SQL - top 5 customer from each country based on orderamount in last 6 month


-- customers

--     customerid
--     country

-- orders

--     ordered
--     customerid
--     orderamount
--     orderdate




with customer_ta as (
    SELECT 
        c.customerid,
        c.country,
        sum(o.orderamount) as total_amount
    FROM customers c
    join order o on c.customerid = o.customerid
    WHERE o.orderdate >= DATE_SUB(current_date() - INTERVAL 6 MONTH)
    group by c.customerid, c.country
),
ranked_customer as (
    select 
        customerid,
        country,
        rank() over (PARTITION BY country order by total_amount) as recs
    FROM customer_ta
)
SELECT * from ranked_customer where recs <= 5