### Data Types in SQL

#### Numeric Data Types
1. **INT(size)**: An integer. Size parameter specifies the maximum display width.
   - **Example**: `INT(11)`
2. **BIGINT(size)**: A large integer.
   - **Example**: `BIGINT(20)`
3. **FLOAT(size, d)**: A floating-point number. Size specifies the total number of digits, and d specifies the number of digits after the decimal point.
   - **Example**: `FLOAT(7,2)`
4. **DOUBLE(size, d)**: A double precision floating-point number.
   - **Example**: `DOUBLE(15,5)`
5. **DECIMAL(size, d)**: A decimal number. Size specifies the total number of digits, and d specifies the number of digits after the decimal point.
   - **Example**: `DECIMAL(10,2)`

#### Date and Time Data Types
1. **DATE**: Stores date values in `YYYY-MM-DD` format.
   - **Example**: `DATE`
2. **DATETIME**: Stores date and time values in `YYYY-MM-DD hh:mm:ss` format.
   - **Example**: `DATETIME`
3. **TIME**: Stores time values in `hh:mm:ss` format.
   - **Example**: `TIME`
4. **YEAR**: Stores year values in `YYYY` format.
   - **Example**: `YEAR`

#### String Data Types
1. **CHAR(size)**: Fixed-length string. Size defines the string length.
   - **Example**: `CHAR(10)`
2. **VARCHAR(size)**: Variable-length string. Size defines the maximum string length.
   - **Example**: `VARCHAR(255)`
3. **TEXT**: A large variable-length string.
   - **Example**: `TEXT`
