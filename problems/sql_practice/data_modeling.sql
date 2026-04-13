/*
customr compute total revenue

orders(order_id, customer_id, order_date, revenue)

- Need to include customers with 0 orders as well


select 
    c.customer_id,
    coalesce(sum(revenue), 0) as total_rev
from customers c
left join orders o on c.customer_id = o.customer_id
group by c.customer_id
order by customer_id


For each campaign, count distinct exposed customers.

Exposed Customer? 


select 
    campaign_id,
    count(distinct customer_id) as dist_customers
from campaign_exposure
group by campaign_id

*/


/*
For each campaign, find the first exposure date per customer.



select 
    campaign_id,
    customer_id,
    min(exposure_date) as index_date
from campaign_exposure
group by campaign_id, customer_id
order by campaign_id, customer_id

*/

/*
For each exposed customer, compute revenue within 30 days after first exposure.

- Join exposed customer and orders table



with exposed_cte as (
    select 
    campaign_id,
    customer_id,
    min(exposure_date) as index_date
from campaign_exposure
group by campaign_id, customer_id
order by campaign_id, customer_id
)

select 
    exposed.campaign_id,
    exposed.customer_id,    
    exposed.index_date,
    COALESCE(sum(revenue), 0) as total_revenue
from exposed_cte exposed
left join orders ord on exposed.customer_id = ord.customer_id
where ord.order_date >= index_date and ord.order_date < index_date + INTERVAL '30 DAYS'
group by 1, 2, 3
order by 1, 2

*/


/*

customers, orders, campaign_exposure

For each campaign, build the control cohort (customers NOT exposed to that campaign).

- Customers not exposed to that campaign - meaning we are tryiing to find all customers not in the campaign exposure table

- Customers in a different campaign + customer in no campaign - For each campaign, get all the customers and check which are not in that campaign

- select all customers not in campaign A

*/

with exposed_cte as 
    (select 
        campaign_id,
        customer_id,
        min(exposure_date) as index_date
    from campaign_exposure
    group by 1, 2
    order by 1, 2
)
, campaign_anchor AS (
  SELECT campaign_id, MIN(index_date) AS anchor_date
  FROM exposed_cte
  GROUP BY 1
)
select 
    anchor.campaign_id,
    c.customer_id,
    anchor_date
from campaign_anchor anchor
cross join customers c
left join exposed_cte exposed
    on exposed.campaign_id = anchor.campaign_id
    and exposed.customer_id = c.customer_id
where exposed.customer_id is NULL
order by 1, 2 

