

import psycopg2

# Database connection setup
# Establishing connection to PostgreSQL database with specified credentials
conn = psycopg2.connect(
    dbname="yourdatabase",  # Database name
    user="username",        # Username
    password="password",    # Password
    host="localhost",       # Host
    port="5432"             # Port number
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# 1. SELECT with WHERE Clause
# Query to select specific columns from customers table where marital status is 'married'
select_query = """
SELECT id, age, job, marital, education, balance
FROM customers
WHERE marital = 'married';
"""
cur.execute(select_query)  # Execute the SELECT query
rows = cur.fetchall()  # Fetch all results
print("SELECT with WHERE Clause:")
for row in rows:
    print(row)  # Print each row

# 2. JOIN Operation
# Query to perform an inner join between customers and departments tables on job and department_name
join_query = """
SELECT c.id, c.age, c.job, d.department_name
FROM customers c
JOIN departments d
ON c.job = d.department_name;
"""
cur.execute(join_query)  # Execute the JOIN query
rows = cur.fetchall()  # Fetch all results
print("\nJOIN Operation:")
for row in rows:
    print(row)  # Print each row

# 3. INSERT INTO Table
# Query to insert a new row into the departments table
insert_query = """
INSERT INTO departments (department_name)
VALUES ('Sales');
"""
cur.execute(insert_query)  # Execute the INSERT query
conn.commit()  # Commit the transaction to save changes
print("\nINSERT INTO Table: Completed")

# 4. UPDATE Operation
# Query to update the balance of a customer with id 1
update_query = """
UPDATE customers
SET balance = 5000
WHERE id = 1;
"""
cur.execute(update_query)  # Execute the UPDATE query
conn.commit()  # Commit the transaction to save changes
print("\nUPDATE Operation: Completed")

# 5. DELETE Operation
# Query to delete a customer with id 1 from the customers table
delete_query = """
DELETE FROM customers
WHERE id = 1;
"""
cur.execute(delete_query)  # Execute the DELETE query
conn.commit()  # Commit the transaction to save changes
print("\nDELETE Operation: Completed")

########################################################################################################

# 1. SELECT with Comparison Operators
# Query to select customers with balance greater than 1000
select_query_comparison = """
SELECT id, age, balance
FROM customers
WHERE balance > 1000;  -- Greater than operator
"""
cur.execute(select_query_comparison)
rows = cur.fetchall()
print("SELECT with Comparison Operators (balance > 1000):")
for row in rows:
    print(row)

# 2. SELECT with Logical Operators
# Query to select customers with balance greater than 1000 and age less than 50
select_query_logical = """
SELECT id, age, job, balance
FROM customers
WHERE balance > 1000 AND age < 50;  -- AND operator
"""
cur.execute(select_query_logical)
rows = cur.fetchall()
print("\nSELECT with Logical Operators (balance > 1000 AND age < 50):")
for row in rows:
    print(row)

# 3. SELECT with LIKE Operator
# Query to select customers with job titles starting with 'tech'
select_query_like = """
SELECT id, age, job, balance
FROM customers
WHERE job LIKE 'tech%';  -- Matches any value starting with 'tech'
"""
cur.execute(select_query_like)
rows = cur.fetchall()
print("\nSELECT with LIKE Operator (job LIKE 'tech%'):")
for row in rows:
    print(row)

# 4. SELECT with IN Operator
# Query to select customers with job titles 'technician', 'admin', or 'services'
select_query_in = """
SELECT id, age, job, balance
FROM customers
WHERE job IN ('technician', 'admin', 'services');  -- Matches any value in the list
"""
cur.execute(select_query_in)
rows = cur.fetchall()
print("\nSELECT with IN Operator (job IN ('technician', 'admin', 'services')):")
for row in rows:
    print(row)

# 5. SELECT with BETWEEN Operator
# Query to select customers with balance between 1000 and 5000
select_query_between = """
SELECT id, age, balance
FROM customers
WHERE balance BETWEEN 1000 AND 5000;  -- Between range
"""
cur.execute(select_query_between)
rows = cur.fetchall()
print("\nSELECT with BETWEEN Operator (balance BETWEEN 1000 AND 5000):")
for row in rows:
    print(row)

# 6. Aggregate Functions
# Query to get the average and total balance of all customers
select_query_aggregate = """
SELECT AVG(balance) AS average_balance, SUM(balance) AS total_balance
FROM customers;
"""
cur.execute(select_query_aggregate)
row = cur.fetchone()
print("\nAggregate Functions (AVG and SUM):")
print(row)

# 7. GROUP BY Clause
# Query to count and average balance of customers grouped by job
select_query_group_by = """
SELECT job, COUNT(*) AS num_customers, AVG(balance) AS avg_balance
FROM customers
GROUP BY job;
"""
cur.execute(select_query_group_by)
rows = cur.fetchall()
print("\nGROUP BY Clause (group by job):")
for row in rows:
    print(row)

# 8. HAVING Clause
# Query to filter groups with average balance greater than 2000
select_query_having = """
SELECT job, COUNT(*) AS num_customers, AVG(balance) AS avg_balance
FROM customers
GROUP BY job
HAVING AVG(balance) > 2000;  -- Filter groups
"""
cur.execute(select_query_having)
rows = cur.fetchall()
print("\nHAVING Clause (having AVG(balance) > 2000):")
for row in rows:
    print(row)

# 9. ORDER BY Clause
# Query to select customers and sort them by balance in descending order
select_query_order_by = """
SELECT id, age, balance
FROM customers
ORDER BY balance DESC;  -- Sort by balance in descending order
"""
cur.execute(select_query_order_by)
rows = cur.fetchall()
print("\nORDER BY Clause (order by balance DESC):")
for row in rows:
    print(row)

# 10. LIMIT Clause
# Query to select top 5 customers sorted by balance in descending order
select_query_limit = """
SELECT id, age, balance
FROM customers
ORDER BY balance DESC
LIMIT 5;  -- Limit results to top 5
"""
cur.execute(select_query_limit)
rows = cur.fetchall()
print("\nLIMIT Clause (limit to top 5 results):")
for row in rows:
    print(row)

# 11. Subqueries
# Query to select customers with balance greater than the average balance
select_query_subquery = """
SELECT id, age, balance
FROM customers
WHERE balance > (SELECT AVG(balance) FROM customers);  -- Subquery to get customers with above average balance
"""
cur.execute(select_query_subquery)
rows = cur.fetchall()
print("\nSubqueries (balance > average balance):")
for row in rows:
    print(row)

# 12. Common Table Expressions (CTEs)
# Query using CTE to select customers with balance greater than the average balance
select_query_cte = """
WITH avg_balance_cte AS (
    SELECT AVG(balance) AS avg_bal
    FROM customers
)
SELECT id, age, balance
FROM customers, avg_balance_cte
WHERE customers.balance > avg_balance_cte.avg_bal;  -- CTE to get customers with above average balance
"""
cur.execute(select_query_cte)
rows = cur.fetchall()
print("\nCommon Table Expressions (CTEs) (balance > average balance):")
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()  # Close the cursor
conn.close()  # Close the database connection
