### SQL Queries and Joins

You've covered different types of SQL joins:

1. **Inner Join**: Retrieves records that have matching values in both tables.

   ```sql
   SELECT customer.cid, cname, products.pid, pname, orders.oid 
   FROM orders
   INNER JOIN products ON orders.pid = products.pid
   INNER JOIN customer ON orders.cid = customer.cid;
   ```

2. **Left Outer Join**: Retrieves all records from the left table and the matched records from the right table.

   ```sql
   SELECT products.pid, pname, amt, orders.oid 
   FROM products
   LEFT JOIN orders ON orders.pid = products.pid;
   ```

3. **Right Outer Join**: Retrieves all records from the right table and the matched records from the left table.

   ```sql
   SELECT * FROM payment 
   RIGHT JOIN orders ON orders.oid = payment.oid;
   ```

4. **Full Outer Join**: MySQL does not directly support `FULL OUTER JOIN`, so you've used `UNION` to achieve similar results.

   ```sql
   SELECT orders.oid, products.pid, pname, amt, price, stock, location FROM orders
   LEFT JOIN products ON orders.pid = products.pid
   UNION
   SELECT orders.oid, products.pid, pname, amt, price, stock, location FROM orders
   RIGHT JOIN products ON orders.pid = products.pid;
   ```

5. **Self Join**: Joins a table to itself, useful for hierarchical queries like finding managers and their employees.

   ```sql
   SELECT e1.ename AS Employee, e2.ename AS Manager 
   FROM employee e1
   INNER JOIN employee e2 ON e1.manager_id = e2.eid;
   ```

6. **Cross Join**: Produces the Cartesian product of two tables, useful for generating all possible combinations.

   ```sql
   SELECT customer.cid, cname, orders.oid, amt 
   FROM customer
   CROSS JOIN orders ON customer.cid = orders.cid
   WHERE amt > 3000;
   ```

### Practice Questions

You've also provided practice questions along with their corresponding SQL queries, such as displaying orders from a specific location (`Mumbai`), orders with payment mode `UPI`, and more complex queries involving conditions on customer age and payment mode.

### Markdown Format

To make notes like this in a `.md` file, structure your content similarly to how it's organized here:

```markdown
### Questions

1. Display details of all orders which were delivered from "Mumbai":

   ```sql
   SELECT * FROM orders 
   LEFT JOIN products ON orders.pid = products.pid
   WHERE location = "Mumbai";
   ```

2. Display details of all orders whose payment was made through "UPI":

   ```sql
   SELECT * FROM orders
   RIGHT JOIN payment ON orders.oid = payment.oid
   WHERE mode = "UPI";
   ```

3. Display `oid`, `amt`, `cname`, `payment mode` of orders made by people below 30 years:

   ```sql
   SELECT orders.oid, cname, amt, mode FROM orders
   INNER JOIN payment ON orders.oid = payment.oid
   INNER JOIN customer ON orders.cid = customer.cid
   WHERE age < 30;
   ```
 
