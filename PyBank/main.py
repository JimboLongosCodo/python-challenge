import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

total=0
min = 0
max = 0
prevamount = 0
cleandata =[]
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)  # skip the headers
    for row in csvreader:
        if row[0] not in cleandata:
            cleandata.append(row)
            amount = float(row[1])
            change = (amount-prevamount)
            total = total + amount
            if change>max:
                max = change
                maxmonth = row[0]
            if change<min:
                min = change
                minmonth = row[0]
            prevamount = amount


months = len(cleandata)
average = (float(cleandata[months-1][1])-float(cleandata[0][1]))/(months-1)


output_file = os.path.join("Analysis","analysis_results.csv")

#  Open the output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Financial Analysis"])
    writer.writerow(["---------------------------------"])
    writer.writerow(["Total Months:",months])
    writer.writerow(["Total:",total])
    writer.writerow(["Average Change:",average])
    writer.writerow(["Greatest Increase in Profits:",maxmonth,max])
    writer.writerow(["Greatest Decrease in Profits:",minmonth,min])
