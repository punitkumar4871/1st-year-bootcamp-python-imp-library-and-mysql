### Data Definition Language (DDL) Commands

DDL commands are used to define and manage database schema and structure.

#### Creating a Database and Tables
```sql
CREATE DATABASE example_db;
USE example_db;

CREATE TABLE employees (
    id INT(3) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    position VARCHAR(50),
    salary DECIMAL(10,2)
);
```

#### Altering a Table
```sql
-- Adding a new column
ALTER TABLE employees ADD COLUMN phone VARCHAR(15);

-- Modifying an existing column
ALTER TABLE employees MODIFY COLUMN salary FLOAT(10,2);

-- Dropping a column
ALTER TABLE employees DROP COLUMN phone;
```

#### Dropping a Table
```sql
DROP TABLE employees;
```

#### Truncating a Table
```sql
TRUNCATE TABLE employees;
```

### Data Manipulation Language (DML) Commands

DML commands are used to manage data within schema objects.

#### Inserting Data
```sql
INSERT INTO employees (id, name, position, salary)
VALUES (1, 'John Doe', 'Software Engineer', 75000.00);
```

#### Updating Data
```sql
UPDATE employees
SET salary = 80000.00
WHERE id = 1;
```

#### Deleting Data
```sql
DELETE FROM employees
WHERE id = 1;
```

#### Selecting Data
```sql
SELECT * FROM employees
WHERE salary > 50000.00;
```

### Data Control Language (DCL) Commands

DCL commands control access to data within the database.

#### Granting Privileges
```sql
GRANT SELECT, INSERT, UPDATE ON example_db.employees TO 'username'@'localhost';
```

#### Revoking Privileges
```sql
REVOKE SELECT, INSERT, UPDATE ON example_db.employees FROM 'username'@'localhost';
```

### Practical Implementation Example

#### Step 1: Creating and Using a Database
```sql
CREATE DATABASE amazon;
USE amazon;
```

#### Step 2: Creating Tables
```sql
CREATE TABLE products (
    pid INT(3) PRIMARY KEY,
    pname VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT(5),
    location VARCHAR(30) CHECK(location IN ('Mumbai','Delhi'))
);

CREATE TABLE customer (
    cid INT(3) PRIMARY KEY,
    cname VARCHAR(30) NOT NULL,
    age INT(3),
    addr VARCHAR(50)
);

CREATE TABLE orders (
    oid INT(3) PRIMARY KEY,
    cid INT(3),
    pid INT(3),
    amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (cid) REFERENCES customer(cid),
    FOREIGN KEY (pid) REFERENCES products(pid)
);

CREATE TABLE payment (
    pay_id INT(3) PRIMARY KEY,
    oid INT(3),
    amount DECIMAL(10,2) NOT NULL,
    mode VARCHAR(30) CHECK(mode IN('upi','credit','debit')),
    status VARCHAR(30),
    FOREIGN KEY (oid) REFERENCES orders(oid)
);
```

#### Step 3: Inserting Data
```sql
INSERT INTO products VALUES (1, 'HP Laptop', 50000.00, 15, 'Mumbai');
INSERT INTO customer VALUES (101, 'Ravi', 30, 'Delhi');
INSERT INTO orders VALUES (1001, 101, 1, 50000.00);
INSERT INTO payment VALUES (1, 1001, 50000.00, 'upi', 'completed');
```

#### Step 4: Updating Data
```sql
UPDATE products SET price = 45000.00 WHERE pid = 1;
```

#### Step 5: Deleting Data
```sql
DELETE FROM customer WHERE cid = 101;
```

#### Step 6: Selecting Data
```sql
SELECT * FROM products WHERE location = 'Delhi';
```

### Constraints

#### Adding Constraints
```sql
ALTER TABLE customer MODIFY COLUMN age INT(2) NOT NULL;
ALTER TABLE customer ADD CONSTRAINT UNIQUE (addr);
ALTER TABLE payment ADD CONSTRAINT CHECK (status IN ('pending', 'cancelled', 'completed'));
```

#### Examples of DML with Constraints
```sql
-- Insert valid data
INSERT INTO customer (cid, cname, age, addr) VALUES (102, 'Rahul', 25, 'Mumbai');

-- Insert invalid data (age constraint violation)
-- This will fail because age is less than 18
INSERT INTO customer (cid, cname, age, addr) VALUES (103, 'Simran', 17, 'Delhi');
```

