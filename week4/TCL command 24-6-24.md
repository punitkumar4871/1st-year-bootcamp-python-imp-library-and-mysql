# Transaction Control Language (TCL) Commands

## 1. **COMMIT**

- **Definition**: Saves all changes made during the current transaction to the database.
- **Syntax**: 
  ```sql
  COMMIT;
  ```
- **Usage**: Typically used when you want to permanently save the changes made by the transaction.

## 2. **ROLLBACK**

- **Definition**: Undoes all changes made during the current transaction and restores the database to its state before the transaction began.
- **Syntax**: 
  ```sql
  ROLLBACK;
  ```
- **Usage**: Used to discard changes if something unexpected occurs or if the transaction needs to be canceled.

## 3. **SAVEPOINT**

- **Definition**: Sets a point within a transaction to which you can later roll back.
- **Syntax**: 
  ```sql
  SAVEPOINT savepoint_name;
  ```
- **Usage**: Allows you to create a savepoint within a transaction so that you can later roll back to that point without rolling back the entire transaction.


### Notes:

- **Transactions**: TCL commands are essential for managing transactions in SQL, ensuring data consistency and integrity.
- **Atomicity**: TCL commands help maintain the ACID properties (Atomicity, Consistency, Isolation, Durability) of transactions.
- **Usage**: Always consider the impact of TCL commands on your database operations, ensuring that transactions are managed effectively to maintain data reliability.
