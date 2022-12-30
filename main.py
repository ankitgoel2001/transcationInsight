"""
Problem:

Justworks wants to generate insight from a list of banking transactions occurring in customer accounts. 
We want to generate minimum , maximum and ending balances by month for customers. You can assume starting balance at begining 
of month is 0. You should read transaction data from csv files and produce output in the format mentioned below. 

Please apply credit transactions first to calculate balance on a given day.  
Please write clear instructions on how to run your program on a local machine. 
Please use dataset in Data Tab to test your program. You do not need to add Column Header in output. please assume input file does not have header row.

Input CSV Format:
CustomerID, Date, Amount, Credit/Debit

Output Format:
CustomerID, MM/YYYY, Min Balance, Max Balance, Ending Balance
"""

import csv
import collections

#open the csv file
with open('data.csv') as csvfile:
    rowreader = csv.reader(csvfile, delimiter=' ')
    customerIDMap = {}
    
    #iterate through each row and store the customerId, date, and amount
    for row in rowreader:

        #if row is empty then skip it
        if row == []: 
            continue

        customerID, date, amount = row[0].split(',')
        month, day, year = date.split('/')
        shortDate = month + '/' + year
        
        if customerID not in customerIDMap:
            customerIDMap[customerID] = {}  

        if shortDate not in customerIDMap[customerID]:
            customerIDMap[customerID][shortDate] = [int(amount), int(amount), int(amount)] #[minBalance, maxBalance, endingBalance]
        else:
            customerIDMap[customerID][shortDate][2] += int(amount)
            customerIDMap[customerID][shortDate][0] = min(customerIDMap[customerID][shortDate][2], customerIDMap[customerID][shortDate][0])
            customerIDMap[customerID][shortDate][1] = max(customerIDMap[customerID][shortDate][2], customerIDMap[customerID][shortDate][1])

print(customerIDMap)







