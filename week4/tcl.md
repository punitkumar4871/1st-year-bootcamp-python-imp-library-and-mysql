```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);

CREATE TABLE salary_changes (
    change_id INT PRIMARY KEY,
    employee_id INT,
    new_salary DECIMAL(10, 2),
    change_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
```

#### Transaction

```sql
-- Start the transaction
BEGIN;

-- Update the salary of an employee
UPDATE employees
SET salary = 50000.00
WHERE employee_id = 101;

-- Insert a record into salary_changes
INSERT INTO salary_changes (change_id, employee_id, new_salary, change_date)
VALUES (1, 101, 50000.00, CURRENT_DATE);

-- Savepoint created before another update
SAVEPOINT before_second_update;

-- Update another employee's salary
UPDATE employees
SET salary = 60000.00
WHERE employee_id = 102;

-- Checkpoint: Commit the changes so far
COMMIT;
```

#### Rollback

```sql
-- Start the transaction
BEGIN;

-- Update the salary of an employee
UPDATE employees
SET salary = 55000.00
WHERE employee_id = 101;

-- Insert a record into salary_changes
INSERT INTO salary_changes (change_id, employee_id, new_salary, change_date)
VALUES (2, 101, 55000.00, CURRENT_DATE);

-- Error occurs or decision to rollback
ROLLBACK;
```


### Summary

- **COMMIT**: Used to permanently save all changes made during a transaction (`BEGIN; ... COMMIT;`).
- **ROLLBACK**: Used to undo all changes made during a transaction and restore the database to its state before the transaction started (`BEGIN; ... ROLLBACK;`).
- **SAVEPOINT**: Allows you to set points within a transaction to which you can later roll back without affecting the entire transaction (`SAVEPOINT savepoint_name; ... ROLLBACK TO SAVEPOINT savepoint_name;`).

