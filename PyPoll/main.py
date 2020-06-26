#import library
import os
import csv
import pandas as pd

#make a deffinination named print and write 
#to print on terminal screen and write the data into a txt file at once

#row = for row
#file = txt file
def printnwrite(row,file):
    print(row)
    print(row,file=file)

#get data path
data_path=os.path.join("Resources/02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

#read csv file as dataframe
data=pd.read_csv(data_path)

#count the total rows
total=len(data)

#group the dataframe by Candiate and count by County then sort descending
result=data.groupby("Candidate")['County'].count().sort_values(ascending=False)

#make a list named order from the one has highest votes to the lowest votes
order=result.index

#make a list named vote containing the number of votes for each candidate
vote=list(result)

#make a list named percentage to contain the got voted rate for each candidate
percentage=[round(vote_count/total*100,4) for vote_count in vote]


#create and open a txt file
with open('analysis/result.txt','w', encoding='utf-8') as file:
    
    #print the analysis/result on terminal screen and write in to the txt file
    printnwrite("Election Results",file)
    printnwrite("-------------------------",file)
    printnwrite(f"Total Votes: {total}",file)
    printnwrite("-------------------------",file)

    #make a loop zipping name, voted number and voted rate
    #make a loop to print the info for each candidate from top to bottom
    for name,voted,percent in zip(order,vote,percentage):
        printnwrite(f"{name}: {percent:.3f}% ({voted})",file)

    printnwrite("-------------------------",file)
    printnwrite(f"Winner: {result.index[0]}",file)
    printnwrite("-------------------------",file)

    

