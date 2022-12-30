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

class TransactionAnalyzer:
    def __init__(self):
        self.customerIDMap = {}

    def analyzeFile(self, filename):
        #open the csv file
        with open(filename) as csvfile:
            rowreader = csv.reader(csvfile, delimiter=' ')
            
            #iterate through each row and store the customerId, date, and amount
            for row in rowreader:

                #if row is empty then skip it
                if row == []: 
                    continue

                customerID, date, amount = row[0].split(',')
                month, day, year = date.split('/')
                shortDate = month + '/' + year
                
                if customerID not in self.customerIDMap:
                    self.customerIDMap[customerID] = {}  

                if shortDate not in self.customerIDMap[customerID]:
                    self.customerIDMap[customerID][shortDate] = [int(amount), int(amount), int(amount)] #[minBalance, maxBalance, endingBalance]
                else:
                    self.customerIDMap[customerID][shortDate][2] += int(amount)
                    self.customerIDMap[customerID][shortDate][0] = min(self.customerIDMap[customerID][shortDate][2], self.customerIDMap[customerID][shortDate][0])
                    self.customerIDMap[customerID][shortDate][1] = max(self.customerIDMap[customerID][shortDate][2], self.customerIDMap[customerID][shortDate][1])

    def printOutput(self):
        for customerID, transactionData in self.customerIDMap.items():
           for date, balances in transactionData.items():
            print(customerID + " " + date + " " + str(balances[0]) + " " + str(balances[1]) + " " + str(balances[2]))

#this is the main function of the program where the program execution begins
if __name__ == "__main__":
    ta = TransactionAnalyzer()
    
    filesInput = input("Enter the name of the files you want to analayze (comma seperated): ")
    filenames = filesInput.split(',')
    for filename in filenames:
        ta.analyzeFile(filename.strip())
    
    ta.printOutput()
    

        

    









