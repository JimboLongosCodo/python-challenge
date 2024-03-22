csvpath = os.path.join("Resources", "election_data.csv")


candidates =[]
votecount =[]
percentage =[]
maxvote = 0
totalvotes = 0
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)  # skip the headers
    for row in csvreader:
        totalvotes = totalvotes + 1
        if row[2] not in candidates:
            candidates.append(row[2])
            votecount.append(0)  
            percentage.append(0)                   
        for i in range(len(candidates)):
            # print(row[2])
            # print(candidates[i])
            if row[2]==candidates[i]:
                votecount[i]=int(votecount[i])+1
    for i in range(len(candidates)):
        percentage[i]=str(round(votecount[i]/totalvotes*100,3)) + "%"
        if int(votecount[i])>maxvote:
            maxvote = int(votecount[i])
            winner = candidates[i]

output_file = os.path.join("Analysis","analysis_results.csv")
clean = list(zip(candidates,percentage,votecount))

#  Open the output file
with open(output_file, "w", newline='') as datafile:
     writer = csv.writer(datafile)

     writer.writerow(["Election Results"])
     writer.writerow(["---------------------------------"])
     writer.writerow(["Total Votes:",totalvotes])
     writer.writerow(["---------------------------------"])
     writer.writerows(clean)     
     writer.writerow(["---------------------------------"])
     writer.writerow(["Winnter:",winner])   
