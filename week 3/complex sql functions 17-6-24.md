# Advanced SQL Functions and Concepts

## ROW_NUMBER()

### Definition
- **ROW_NUMBER()** is an analytic function that assigns a unique sequential integer to each row within a partition of a result set.

### Syntax
```sql
ROW_NUMBER() OVER (PARTITION BY partition_expression ORDER BY sort_expression)
```

### Example
```sql
SELECT
    ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank_in_dept,
    employee_id,
    salary,
    department_id
FROM
    employees;
```

## RANK()

### Definition
- **RANK()** is an analytic function that assigns a rank to each row within a partition of a result set, with gaps in the ranking where there are ties.

### Syntax
```sql
RANK() OVER (PARTITION BY partition_expression ORDER BY sort_expression)
```

### Example
```sql
SELECT
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank_in_dept,
    employee_id,
    salary,
    department_id
FROM
    employees;
```

## DENSE_RANK()

### Definition
- **DENSE_RANK()** is an analytic function that assigns a rank to each row within a partition of a result set, without any gaps in the ranking where there are ties.

### Syntax
```sql
DENSE_RANK() OVER (PARTITION BY partition_expression ORDER BY sort_expression)
```

### Example
```sql
SELECT
    DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dense_rank_in_dept,
    employee_id,
    salary,
    department_id
FROM
    employees;
```
## CUME_DIST()

### Definition
- **CUME_DIST()** is an analytic function in SQL that calculates the cumulative distribution of a value within a group of rows.

### Syntax
```sql
CUME_DIST() OVER (PARTITION BY partition_expression ORDER BY sort_expression)
```

### Example
```sql
SELECT
    employee_id,
    salary,
    department_id,
    CUME_DIST() OVER (PARTITION BY department_id ORDER BY salary DESC) AS cumulative_distribution
FROM
    employees;
```

## LEAD()

### Definition
- **LEAD()** is an analytic function in SQL that provides access to a value on a subsequent row in the result set.

### Syntax
```sql
LEAD(expression, offset [, default]) OVER (PARTITION BY partition_expression ORDER BY sort_expression)
```

### Example
```sql
SELECT
    employee_id,
    salary,
    department_id,
    LEAD(salary, 1) OVER (PARTITION BY department_id ORDER BY salary DESC) AS next_salary
FROM
    employees;
```


```
