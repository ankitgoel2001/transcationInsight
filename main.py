import csv
import collections

"""
This class is to calculate the analayze the transcation of a deposit in a bank account,
and calculate the minimum, maximum, and ending balances for each month.
"""
class TransactionAnalyzer:

    """
    This is the constructor class that initializes the customerID map
    """
    def __init__(self):
        """
        This is how the customerID map stores the data
        {
            customer ID1: {
                date1: [minBalance, maxBalance, endingAmount],
                date2: [minBalance, maxBalance, endingAmount]
            },
            customer ID2: {
                date1: [minBalance, maxBalance, endingAmount],
                date2: [minBalance, maxBalance, endingAmount]
            }
        }
        """
        self.customerIDMap = {} 

    """
    This function is to parse through the csv file and perform the credit calculation,
    and store the value in the customerID map
    """
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
                    self.customerIDMap[customerID][shortDate][2] += int(amount) #update ending balance
                    
                    #update the minimum and maximum balances
                    self.customerIDMap[customerID][shortDate][0] = min(self.customerIDMap[customerID][shortDate][2], self.customerIDMap[customerID][shortDate][0])
                    self.customerIDMap[customerID][shortDate][1] = max(self.customerIDMap[customerID][shortDate][2], self.customerIDMap[customerID][shortDate][1])

    """
    This function is to print the output of the transaction data from the customerID map
    """
    def printOutput(self):
        for customerID, transactionData in self.customerIDMap.items():
           for date, balances in transactionData.items():
            print(customerID + " " + date + " " + str(balances[0]) + " " + str(balances[1]) + " " + str(balances[2]))

""""
This is the main function of the program where the program execution begins
"""
if __name__ == "__main__":
    ta = TransactionAnalyzer() #instance of the class
    
    #get the filename as a comma separated list
    filesInput = input("Enter the name of the files you want to analayze (comma seperated): ")
    filenames = filesInput.split(',') #split the filename list into an array

    #pass in every file name to perform the analysis
    for filename in filenames:
        ta.analyzeFile(filename.strip()) #strip function to remove extra spaces between file names
    
    ta.printOutput() #print the formatted output
    

        

    









