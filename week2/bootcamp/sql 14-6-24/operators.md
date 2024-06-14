### SQL Operators with Examples

**1. Operator:**
   - An operator is a symbol that tells the compiler to perform specific mathematical, relational, or logical operations to produce a desired result.
   - Example: In the expression `5 + 3`, `+` is the operator.

**2. Operand:**
   - An operand is an object which is operated upon by any operator to produce a result.
   - Example: In the expression `5 + 3`, `5` and `3` are operands.

**3. Expression:**
   - An expression is a combination of one or more operators and operands which together produce a meaningful result.
   - Example: `5 + 3` is an expression that evaluates to `8`.

There are four main types of operators in SQL:
   - Arithmetic Operators
   - Comparison Operators
   - Bitwise Operators
   - Logical Operators

### A) Arithmetic Operators

Arithmetic operators are used for mathematical calculations. There are five types:

1. **Addition (+):** Adds two operands.
   - Example:
     ```sql
     SELECT 7 + 2; -- Result: 9
     ```

2. **Subtraction (-):** Subtracts the second operand from the first.
   - Example:
     ```sql
     SELECT 10 - 4; -- Result: 6
     ```

3. **Multiplication (*):** Multiplies two operands.
   - Example:
     ```sql
     SELECT 6 * 3; -- Result: 18
     ```

4. **Division (/):** Divides the first operand by the second.
   - Example:
     ```sql
     SELECT 15 / 3; -- Result: 5
     ```

5. **Modulo (%):** Returns the remainder of the division of the first operand by the second.
   - Example:
     ```sql
     SELECT 10 % 4; -- Result: 2
     ```

### B) Comparison Operators

Comparison operators are used to compare the operands and return a result in true or false. There are six types:

1. **Equals To (=):** Checks if two operands are equal.
   - Example:
     ```sql
     SELECT 8 = 8; -- Result: True
     ```

2. **Greater Than (>):** Checks if the left operand is greater than the right operand.
   - Example:
     ```sql
     SELECT 9 > 6; -- Result: True
     ```

3. **Less Than (<):** Checks if the left operand is less than the right operand.
   - Example:
     ```sql
     SELECT 4 < 5; -- Result: True
     ```

4. **Greater Than or Equals To (>=):** Checks if the left operand is greater than or equal to the right operand.
   - Example:
     ```sql
     SELECT 7 >= 3; -- Result: True
     ```

5. **Less Than or Equals To (<=):** Checks if the left operand is less than or equal to the right operand.
   - Example:
     ```sql
     SELECT 4 <= 6; -- Result: True
     ```

6. **Not Equals To (<> or !=):** Checks if two operands are not equal.
   - Example:
     ```sql
     SELECT 5 != 3; -- Result: True
     ```

### C) Bitwise Operators

Bitwise operators perform bit-level operations on the operands. There are three types:

1. **Bitwise AND (&):** Performs a bitwise AND operation.
   - Example:
     ```sql
     SELECT 10 & 7; -- Result: 2
     ```

2. **Bitwise OR (|):** Performs a bitwise OR operation.
   - Example:
     ```sql
     SELECT 5 | 3; -- Result: 7
     ```

3. **Bitwise XOR (^):** Performs a bitwise XOR operation.
   - Example:
     ```sql
     SELECT 9 ^ 5; -- Result: 12
     ```

### D) Logical Operators

Logical operators connect two or more boolean expressions to produce a true or false result. Commonly used types are:

1. **AND:** Returns true if all conditions separated by AND are true.
   - Example:
     ```sql
     SELECT 1 = 1 AND 2 > 1; -- Result: True
     ```

2. **OR:** Returns true if any of the conditions separated by OR is true.
   - Example:
     ```sql
     SELECT 2 > 3 OR 4 > 2; -- Result: True
     ```

3. **NOT:** Returns true if the condition is false.
   - Example:
     ```sql
     SELECT NOT 3 < 2; -- Result: True
     ```

4. **LIKE:** Returns true if the operand matches a pattern.
   - Example:
     ```sql
     SELECT 'Database' LIKE '%base'; -- Result: True
     ```

5. **BETWEEN:** Returns true if the operand is within a specified range.
   - Example:
     ```sql
     SELECT 8 BETWEEN 5 AND 10; -- Result: True
     ```
