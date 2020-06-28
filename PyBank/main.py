#import library
import os
import csv

#get data path
data_path=os.path.join("Resources/02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

#open and read data
with open(data_path,'r') as file:

    #read csv file with delimiter = ,
    csvreader=csv.reader(file, delimiter=',')
    
    #get the header
    header=next(csvreader)

    #give default value:
    count=0 #how many months in the dataset
    total=0 #totl profit/loss
    max=0   #max profit/loss
    maxdate=" "
    min=0   #min profit/loss
    mindate=" "
    present=0  
    previous=0
    change=0 #total exchange in profit/loss

    #get the reminding rows which contain the data for date and profit/loss
    for row in csvreader:

        #count the total number of rows without header
        count=count+1

        #calculate the total profit/loss
        total=total +int(row[1])

        #calculate the exchange profit/loss
        previous=present
        present=int(row[1])
        if count >1:
            change=change+present-previous

        #figure out the max profit and the date that happened
        if max<int(row[1]):
            max=int(row[1])
            maxdate=row[0]
        
        #figure out the max loss and the date that happened
        if min>int(row[1]):
            min=int(row[1])
            mindate=row[0]

    #calculate the average
    exchange=count-1 #total exchange times
    average=change/exchange

#print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {count}")
print(f"Total: ${total}")
print(f"Average  Change: ${average:.2f}")
print(f"Greatest Increase in Profits: {maxdate} (${max})")
print(f"Greatest Decrease in Profits: {mindate} (${min})")


#create and open a txt file
with open ("analysis/result.txt","w", encoding='utf-8') as file:
    #set , as the delimiter
    csvwriter=csv.writer(file,delimiter=",")

    #write the analysis into the txt file
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {count}"])
    csvwriter.writerow([f"Total: ${total}"])
    csvwriter.writerow([f"Average  Change: ${average:2f}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {maxdate} (${max})"])
    csvwriter.writerow([f"Greatest Increase in Profits: {mindate} (${min})"])