# SQL Command Cheat Sheet

## Table of Contents

1. [Database Operations](#database-operations)
2. [Table Operations](#table-operations)
3. [Data Manipulation](#data-manipulation)
4. [Querying Data](#querying-data)
5. [Joins](#joins)
6. [Aggregate Functions](#aggregate-functions)
7. [Subqueries](#subqueries)
8. [Indexes](#indexes)
9. [Views](#views)
10. [Transactions](#transactions)
11. [User and Privileges](#user-and-privileges)

---

## Database Operations

- **Create Database**: Creates a new database.

  ```sql
  CREATE DATABASE database_name;
  ```

- **Drop Database**: Deletes an existing database
  ```sql
  DROP DATABASE database_name;
  ```

## Table Operations

- **Create Table**: Creates a new table with specified columns and data types.

  ```sql
  CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
  );
  ```

- **Drop Table**: Deletes an existing table.

  ```sql
  DROP TABLE table_name;
  ```

- **Alter Table**: Modifies an existing table.

  - **Add Column:** Adds a new column to an existing table.

    ```sql
    ALTER TABLE table_name ADD column_name dataype;
    ```

  - **Drop Column:** Removes a column from an existing table.

    ```sql
    ALTER TABLE table_name DROP COLUMN column_name;
    ```

  - **Modify Column:** Changes the data type of an existing column.
    ```sql
    ALTER TABLE table_name MODIFY COLUMN column_name datatype;
    ```

## Data Manipulation

- **Insert Data:** Adds new rows of data to a table.

  ```sql
  INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
  ```

- **Update Data:** Modifies existing data in a table.

  ```sql
  UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
  ```

- **Delete Data:** DELETE FROM table_name WHERE condition;
  ```sql
  DELETE FROM table_name WHERE condition;
  ```

## Querying Data

- **Select All Data:** Retrieves all columns from a table.

  ```sql
  SELECT * FROM table_name;
  ```

- **Select Data:** Retrieves specific columns from a table.

  ```sql
  SELECT column1, column2, ... FROM table_name WHERE condition;
  ```

- **Select Disctint Data:** Retrieves unique values from a column.

  ```sql
  SELECT DISTINCT column1 FROM table_name;
  ```

- **Where Clause:** Filters records that meet a specified condition.

  ```sql
  SELECT column1, column2, ... FROM table_name WHERE condition;
  ```

- **Order By Clause:** Sorts the result set in ascending or descending order

  ```sql
  SELECT column1, column2, ... FROM table_name ORDER BY column1 [ASC|DESC];
  ```

- **Limit Clause:** Specifies the number of records to return.
  ```sql
  SELECT column1, column2, ... FROM table_name LIMIT number;
  ```

## Joins

- **Inner Join:** Retrieves records that have matching values in both tables.

  ```sql
  SELECT columns FROM table1 INNER JOIN table2 ON table1.column = table2.column;
  ```

- **Left Join:** Retrieves all records from the left table, and the matched records from the right table.

  ```sql
  SELECT columns FROM table1 LEFT JOIN table2 ON table1.column = table2.column;
  ```

- **Right Join:** Retrieves all records from the right table, and the matched records from the left table.

  ```sql
  SELECT columns FROM table1 RIGHT JOIN table2 ON table1.column = table2.column;
  ```

- **Full Join:** Retrieves all records from the right table, and the matched records from the left table.
  ```sql
  SELECT columns FROM table1 FULL OUTER JOIN table2 ON table1.column = table2.column;
  ```

## Aggregate Functions

- **Count:** Returns the number of rows that matches a specified criterion.

  ```sql
  SELECT COUNT(column) FROM table_name;
  ```

- **Sum:** Returns the total sum of a numeric column.

  ```sql
  SELECT SUM(column) FROM table_name;
  ```

- **Average:** Returns the average value of a numeric column.

  ```sql
  SELECT AVG(column) FROM table_name;
  ```

- **Max:** Returns the largest value of the selected column.

  ```sql
  SELECT MAX(column) FROM table_name;
  ```

- **Min:** Min: Returns the smallest value of the selected column.
  ```sql
  SELECT MIN(column) FROM table_name;
  ```

## Subqueries

- **Subquerry in Select:** A subquery within the SELECT statement.

  ```sql
  SELECT column, (SELECT column FROM table_name WHERE condition) AS alias FROM table_name;
  ```

- **Subquerry in WHERE:** A subquery within the WHERE clause.
  ```sql
  SELECT column FROM table_name WHERE column = (SELECT column FROM table_name WHERE condition);
  ```

## Indexes

- **Create Index:** Creates an index on a table.

  ```sql
  CREATE INDEX index_name ON table_name (column1, column2, ...);
  ```

- **Show Index:** List all created indexes

  ```sql
  SHOW INDEXES FROM table_name;
  ```

- **Drop Index:** Creates an index on a table.
  ```sql
  DROP INDEX index_name ON table_name;
  ```

## Views

- **Create View:** Creates a virtual table based on the result set of an SQL statement.

  ```sql
  CREATE VIEW view_name AS SELECT column1, column2, ... FROM table_name WHERE condition;
  ```

- **Drop View:** Deletes a view.
  ```sql
  DROP VIEW view_name;
  ```

## Transactions

- **Begin Transaction:** Starts a transaction.

  ```sql
  BEGIN;
  ```

- **Comit Transaction:** Saves the changes made in the transaction.

  ```sql
  COMMIT;
  ```

- **Rollback Transaction:** Reverts the changes made in the transaction.
  ```sql
  ROLLBACK;
  ```

## User and Priviledges

- **Create User:** Creates a new user.

  ```sql
  CREATE USER 'username'@'host' IDENTIFIED BY 'password';
  ```

- **Grant Privileges:** Grants privileges to a user.

  ```sql
  CREATE USER 'username'@'host' IDENTIFIED BY 'password';
  ```

- **Revoke Privileges:** Revokes privileges from a user.

  ```sql
  CREATE USER 'username'@'host' IDENTIFIED BY 'password';
  ```

- **Drop User:** Deletes a user.
  ```sql
  DROP USER 'username'@'host';
  ```

## More

[SQL Commands Cheat Sheet](SQL-Commands-Cheat-Sheet.pdf)
