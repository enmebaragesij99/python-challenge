import os
import csv

election_data_csv=os.path.join('Resources','election_data.csv')
#Stating variables
cast_total=0
candidate_options=[]
total_votes_count=0
Charles_count=0
Diana_count=0
Raymon_count=0
Charles_percent=0
Diana_percent=0
Raymon_percent=0
#Open csv file
with open(election_data_csv) as csvfile:
    csvreader=csv.reader(csvfile)
    csv_header=next(csvreader)

    for row in csvreader:
#List of candidates who received votes
        candidate_name=row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
#Total number of votes cast
        total_votes_count +=1
#Total number of votes each candidate won
        if row[2]=="Charles Casper Stockham":
            Charles_count +=1
        elif row[2]=="Diana DeGette":
            Diana_count +=1
        elif row[2]=="Raymon Anthony Doane":
            Raymon_count +=1
    vote_counter={"Charles Casper Stockham":Charles_count,"Diana DeGette":Diana_count,"Raymon Anthony Doane":Raymon_count}
 #Total percentage of votes each candidate won
    Charles_percent=round((Charles_count/total_votes_count)*100,3)
    Diana_percent=round((Diana_count/total_votes_count)*100,3)
    Raymon_percent=round((Raymon_count/total_votes_count)*100,3)

#Winner of election baseed on popular vote

Winner=max(vote_counter, key=vote_counter.get)

#Print election results    
election_summary=(
    f"Election Results\n"

    f"--------------------------------------\n"

    f"Total Votes: {total_votes_count}\n"

    f"--------------------------------------\n"

    f"Charles Casper Stockam: {Charles_percent}%  ({Charles_count})\n"

    f"Diana DeGette: {Diana_percent}%  ({Diana_count})\n"

    f"Raymon Anthony Doane: {Raymon_percent}%  ({Raymon_count})\n"

    f"--------------------------------------\n"

    f"Winner: {Winner}\n"

    f"--------------------------------------\n" )

print(election_summary)

#Create and write text file
text_path="pypoll_output.txt"

with open(text_path,'w') as f:
        f.write(election_summary)
        
        
        
    