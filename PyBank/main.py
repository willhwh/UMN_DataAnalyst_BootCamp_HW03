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
    count=0
    total=0
    max=0
    maxdate=" "
    min=0
    mindate=" "
    

    #get the reminding rows which contain the data for date and profit/loss
    for row in csvreader:

        #count the total number of rows without header
        count=count+1

        #calculate the total profit/loss
        total=total +int(row[1])

        #figure out the max profit and the date that happened
        if max<int(row[1]):
            max=int(row[1])
            maxdate=row[0]
        
        #figure out the max loss and the date that happened
        if min>int(row[1]):
            min=int(row[1])
            mindate=row[0]

    #calculate the average
    average=total/count

#print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {count}")
print(f"Total: ${total}")
print(f"Average  Change: ${average}")
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
    csvwriter.writerow([f"Average  Change: ${average}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {maxdate} (${max})"])
    csvwriter.writerow([f"Greatest Increase in Profits: {mindate} (${min})"])