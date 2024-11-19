# 0x00. MySQL Advanced

## Overview

This project is part of the ALX Software Engineering Program. It's designed to help me understand and implement advanced MySQL concepts. By the end of this project, I should be able to explain various advanced MySQL topics without needing to look them up.

## Learning Objectives

By completing this project, I aim to understand:

- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL

## Requirements

### General

- All files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
- All files should end with a new line
- All SQL queries should have a comment just before (i.e., syntax above)
- All files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A `README.md` file is mandatory
- The length of files will be tested using `wc`

## Key MySQL Advanced Concepts

### Creating Tables with Constraints

Constraints are rules applied to table columns to enforce data integrity. Common constraints include `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, and `CHECK`.

### Optimizing Queries by Adding Indexes

Indexes improve the speed of data retrieval operations on a table at the cost of additional writes and storage space. Common types of indexes include `BTREE`, `HASH`, and `FULLTEXT`.

### Stored Procedures and Functions

- **Stored Procedures**: A set of SQL statements that can be executed as a single unit to perform a specific task.
- **Functions**: Similar to stored procedures, but they return a value and can be used in SQL statements.

### Implementing Views

Views are virtual tables created by a query. They allow users to simplify complex queries, present data in a specific format, and enhance security by restricting access to underlying tables.

### Implementing Triggers

Triggers are sets of SQL statements that automatically execute or fire when specific events occur in the database, such as `INSERT`, `UPDATE`, or `DELETE`.

## Tasks

This project has various tasks to practice and implement the above concepts. Each task will help reinforce the learning objectives and build a strong foundation in advanced MySQL.
