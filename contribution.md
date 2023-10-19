TASK 2: Join, Filter and Aggregate

Story Background:
You are working for a leading e-commerce platform, and your team is tasked with analyzing a
massive dataset in the form of a text file. This dataset contains two tables, one after the other, and
contains crucial information about customer orders and product reviews.
Table 1: Customer Orders
Each line in this table represents a customer order.
Fields: Order ID, Customer ID, Product ID, Quantity, Price per Unit.
Table 2: Product Reviews

Each line in this table represents a product review submitted by customers.
Fields: Review ID, Product ID, Customer ID, Rating (1-5 stars), Review Text.
Objective:
Your goal is to gain valuable insights from this dataset. Specifically, you want to understand the
relationship between product reviews and the number of items sold for each product. You plan to use
a multi-stage Hadoop MapReduce job to join, filter, and aggregate the data to answer the following
question:
Question:
"How can you leverage Hadoop MapReduce to perform a join operation between customer order
data and product review data, filter out low-rated reviews (ratings less than 3), and aggregate the
results to identify products with the most negative reviews and the quantity of those products sold?"
Example:
Input Text File (input.txt):
The file is a text file with Tab-Separated Values(TSV).
Column 1 represents the type of record, i.e. whether it belongs to the Customer Orders Table
("order") or the Product Reviews Table ("review").

order 1 C101 P001 2 20.00
order 2 C102 P002 3 25.00
order 3 C103 P001 1 20.00
order 4 C104 P003 2 30.00
review 101 P001 C101 4 "Great product, very satisfied."
review 102 P002 C102 2 "Not happy with the quality."
review 103 P003 C104 2 "Average product, could be better."
review 104 P001 C103 1 "Terrible, wouldn't recommend."

Expected Output (output.txt):

# Products with Negative Reviews and Quantity Sold - DO NOT PRINT
# Product ID, Quantity Sold - DO NOT PRINT
P002 3
P001 3
P003 2

Explanation:
In the expected output, we have identified products with negative reviews (ratings less than 3) and
calculated the quantity of those products sold. In this example, "P002" had the lowest product rating

(2), and it was sold in a quantity of 3. "P001" also had negative reviews (with one rating of 1 and one
of 4) and was sold in a quantity of 3. "P003" had a rating of 2 (considered average) and was sold in a
quantity of 2.
This output is the result of the Hadoop MapReduce job, which involved joining the customer order
and product review data, filtering out low-rated reviews, and aggregating the quantity sold for each
product with negative reviews.
Workflow Constraints:
1. You are obligated to use exactly three stages to account to this solution. (i.e. three pairs of
Mappers and Reducers)
2. Do not import any external modules. Use modules only available in the default python package.
3. The output should be in TSV format.
Sample Input
dataset_sample.txt
Sample Output
expected_output_dataset_sample.txt

AQJZBDZL45205293 9
BICYGUPD57809078 19
GHIHXNYM43631821 13
HGRUYMDQ86957814 13
JRJRUKLO25747746 13
MAOSEHSQ24182331 19
PZSLAOMX00719228 17

Test Dataset
Test your code with the following dataset once it passes the sample dataset
1. Input: dataset_large.txt
2. Output: expect_output_dataset_large.txt
All the files can be found here.
