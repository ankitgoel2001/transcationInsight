# TRANSACTION ANALYSIS

## How to run

To run the program please type `py main.py`

## Summary

This program is to perform the transaction analaysis of money deposited from a 
customer over a period of month either a credit or debit, by displaying the 
minimum, maximum and ending balances. Thus, we are calculating balances 
for each customer for each month.

## Implementation

I implemented this with the help of object-oriented programming through the use of 
a `TransactionAnalyzer ` class. There is a `customerID` HashMap I used for storing
data, which stores another HashMap within it that is the "date" key, and the value
is a list in the format [minBalance, maxBalance, endingBalance].

The reason I made a nested HashMap, meaning another map for each date is since the same
customer could deposit for another month. And we have to track the balance for each 
month by the customer. 

I made sure the program works for reading with multiple csv files. So, this means the
end output produced will be the analysis after reading through multiple csv files.

I used data structures like a class since it makes it really easy to visualize, and store
elements of data, and reuse certain functions under the same belt.

## Testing

I tested my program with those files: `data.csv` and `data2.csv`. 
