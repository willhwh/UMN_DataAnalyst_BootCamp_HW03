import os
import csv
import pandas as pd

data_path=os.path.join("Resources/02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")
data=pd.read_csv(data_path)
total=len(data)

result=data.groupby("Candidate")['County'].count().sort_values(ascending=False)
order=result.index
vote=list(result)
percentage=[round(vote_count/total*100,4) for vote_count in vote]




print("Election Results")
print("-------------------------")
print(f"Total Votes: {total}")
print("-------------------------")
for name,voted,percent in zip(order,vote,percentage):
    
    print(f"{name}: {percent:.3f}% ({voted})")
print("-------------------------")
print(f"Winner: {result.index[0]}")
print("-------------------------")


with open('analysis/result.txt','w') as file:
    print("Election Results",file=file)
    print("-------------------------",file=file)
    print(f"Total Votes: {total}",file=file)
    print("-------------------------",file=file)
    for name,voted,percent in zip(order,vote,percentage):
        
        print(f"{name}: {percent:.3f}% ({voted})",file=file)
    print("-------------------------",file=file)
    print(f"Winner: {result.index[0]}",file=file)
    print("-------------------------",file=file)
    

