import os
import csv

budget_data_csv=os.path.join('Resources', 'budget_data.csv')
#Stating variables
total_months=0
pl_total=0
change_list=[]
average_change=0
change_month=[]
previous_change=0
change=0
increase_amount=0
increase_date=[""]
decrease_amount=99999
decrease_date=[""]
#Open cvs file
with open(budget_data_csv) as csvfile:
    csvreader=csv.reader(csvfile)
    csv_header=next(csvreader)      


    for row in csvreader:
#Total months
        total_months+=1
#Net total of profit/losses       
        pl_total=pl_total+int(row[1])       

#Average change in Profit/Losses over entire period
        change=float(row[1])-previous_change
        previous_change=float(row[1])
        change_list=change_list+[change]
        change_month=[change_month]+[row[0]]


#Greatest increase in profits:date and amount

        if change > increase_amount:
            increase_amount=round(change)
            increase_date=row[0]

#Greatest decrease in losses: date and amount

        if change < decrease_amount:
            decrease_amount=round(change)
            decrease_date=row[0]
change_list.pop(0)
average_change=round(sum(change_list)/len(change_list),2)


#Print budget summary
budget_summary=(
f"Financial Analysis\n"

f"--------------------------------------\n"

f"Total months: {total_months}\n" 

f"Total: ${pl_total}\n" 

f"Average change: $ {average_change}\n"

f"Greatest Increase in Profits: {increase_date}   (${increase_amount})\n"

f"Greatest Decrease in Profits: {decrease_date}   (${decrease_amount})\n")

print(budget_summary)

#Create and write text file
text_path="pybank_output.txt"

with open(text_path,'w') as f:
        f.write(budget_summary)
       