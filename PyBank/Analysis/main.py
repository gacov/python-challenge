
import os
import csv

bank_csv = os.path.join("..","Resources","PyBank_data.csv")

with open(bank_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    months = []
    profitspermonth = []
    changesmonth = []
    averagechange = 0
    maxchange = 0
    maxchangedate = ""
    minchange = 0
    minchagedate = ""

    for row in csvreader:
        months.append(row[0])
        profitspermonth.append(int(row[1]))
    
    for x in range(1, len(profitspermonth)):
        changesmonth.append(profitspermonth[x]-profitspermonth[x-1])
        averagechange = sum(changesmonth)/len(changesmonth)

        maxchange = max(changesmonth)
        minchange = min(changesmonth)
                
        maxindex = changesmonth.index(max(changesmonth)) + 1
        minindex = changesmonth.index(min(changesmonth)) + 1

        maxchangedate = str(months[maxindex])
        minchangedate = str(months[minindex])


print(f"Financial Analysis")
print(f"--------------------------")
print(f"Total Months: {(len(months))}")
print(f"Total: ${sum(profitspermonth)}")
print(f"Average Change: ${round(averagechange,2)}")
print(f"Greatest Increase in Profits: {maxchangedate} (${maxchange})")
print(f"Greatest Decrease in Profits: {minchangedate} (${minchange})")


f = open("paybank_analysis.txt","w")
print(f"Financial Analysis", file=f)
print(f"--------------------------", file=f)
print(f"Total Months: {(len(months))}", file=f)
print(f"Total: ${sum(profitspermonth)}", file=f)
print(f"Average Change: ${round(averagechange,2)}", file=f)
print(f"Greatest Increase in Profits: {maxchangedate} (${maxchange})", file=f)
print(f"Greatest Decrease in Profits: {minchangedate} (${minchange})", file=f)






    
  



    
    

  
