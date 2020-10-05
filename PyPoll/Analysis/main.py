
import os
import csv

poll_csv = os.path.join("..","Resources","PyPoll_data.csv")

with open(poll_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    voters = []
    candidates = []
    votespercandidate = []
    percentagepercandidate = 0

    for row in csvreader:
        voters.append(row[0])
        candidates.append(row[2])
        
    
    from collections import Counter
    conteo = Counter(candidates)
        

    

print(f"Election Results")
print(f"--------------------------")
print(f"Total Votes: {(len(voters))}")
print(f"--------------------------")
for x in conteo:
    print (f"{x}: {conteo[x]/len(voters):.3%} ({conteo[x]})")
print(f"--------------------------")
print(f"Winner: {max(conteo, key=lambda k: conteo[k])}")
print(f"--------------------------")


f = open("pypoll_analysis.txt","w")
print(f"Election Results", file=f)
print(f"--------------------------", file=f)
print(f"Total Votes: {(len(voters))}", file=f)
print(f"--------------------------", file=f)
for x in conteo:
    print (f"{x}: {conteo[x]/len(voters):.3%} ({conteo[x]})", file=f)
print(f"--------------------------", file=f)
print(f"Winner: {max(conteo, key=lambda k: conteo[k])}", file=f)
print(f"--------------------------", file=f)




