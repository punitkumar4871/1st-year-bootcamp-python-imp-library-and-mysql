# Subqueries

## Definition
A subquery, also known as an inner query or nested query, is a query nested within another SQL statement. It's used to retrieve data necessary for the main query to execute.

## Types of Subqueries

### 1. **Single Row Subquery**
   - Returns only one row of results.
   - Typically used with single-row operators (`=`, `>`, `<`, `IN`, etc.).
   - Example:
     ```sql
     SELECT column1
     FROM table1
     WHERE column2 = (SELECT column3 FROM table2 WHERE condition);
     ```

### 2. **Multiple Row Subquery**
   - Returns multiple rows of results.
   - Used with multiple-row operators (`IN`, `ANY`, `ALL`).
   - Example:
     ```sql
     SELECT column1
     FROM table1
     WHERE column2 IN (SELECT column3 FROM table2 WHERE condition);
     ```

### 3. **Multiple Column Subquery**
   - Returns multiple columns of results.
   - Typically used with comparisons involving multiple columns.
   - Example:
     ```sql
     SELECT column1, column2
     FROM table1
     WHERE (column1, column2) IN (SELECT column3, column4 FROM table2 WHERE condition);
     ```

### 4. **Correlated Subquery**
   - References one or more columns from the outer query.
   - Executes once for each row processed by the outer query.
   - Example:
     ```sql
     SELECT column1
     FROM table1 t1
     WHERE column2 > (SELECT AVG(column3) FROM table2 t2 WHERE t2.related_column = t1.related_column);
     ```

### 5. **Scalar Subquery**
   - Returns a single value.
   - Can be used in places where expressions are expected.
   - Example:
     ```sql
     SELECT column1, (SELECT MAX(column2) FROM table2) AS max_value
     FROM table1;
     ```
