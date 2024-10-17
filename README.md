# Customer Management System

## Overview
This is a Customer Management System that manages customer data, allowing you to add, view, and perform transactions on customer accounts. The program loads customer data from a CSV file and provides various functionalities for managing customer accounts.

## Features
- **Customer Class**: Defines customer attributes and methods for managing customer data.
- **View Balance**: Allows customers to view their current account balance.
- **Add Amount**: Allows adding money to a customer's account.
- **Withdraw**: Allows withdrawing money from a customer's account, ensuring sufficient funds.
- **Load Customers**: Loads customer data from a CSV file for easy management.
- **Data Analysis**: Provides basic data analysis to filter customers by different criteria.

## Installation
1. Ensure you have Python installed on your machine.
2. Create a CSV file named `costomers_data.csv` with the following columns:
   - `name`
   - `age`
   - `job_title`
   - `id`
   - `phone`
   - `bank_account`
   - `balance`
3. Run the script.

## Usage
```python
import csv

class New_Costomer:
    # Class implementation
    ...
    
# Load customers from CSV
New_Costomer.costomers_list("costomers_data.csv")

# Print all customers
print(New_Costomer.all_costomer)

# Filtering examples
# Customers with balance over $5000
new_list = [emp for emp in New_Costomer.all_costomer if emp.balance > "5000"]
# Customers working as Software Engineers
new_list = [emp for emp in New_Costomer.all_costomer if emp.job_title.lower() == "software engineer"]
# Young customers (age 25)
new_list = [emp for emp in New_Costomer.all_costomer if emp.age == "25"]
