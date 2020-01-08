#======================================================================================================
#[0] Setup
#======================================================================================================

import os
import csv
file = 'GT-ATL-DATA-PT-12-2019-U-C/Homework/03-Python/Instructions/PyBank/Resources'
csvpath = os.path.join('..','..', file, 'budget_data.csv')

#======================================================================================================
#[1] Loop
#======================================================================================================

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    month_ct = 0
    total = 0
    month = 867884
    month_nm = ""
    change = 0
    total_change = 0
    avg_change = 0
    month_ct2 = 0
    grt_inc = 0
    grt_inc_month = ""
    grt_dec = 0
    grt_dec_month = ""
    for row in csvreader:
        month_ct += 1
        total += int(row[1])
        if change > grt_inc:
            grt_inc = change
            grt_inc_month = month_nm
        if change < grt_dec:
            grt_dec = change
            grt_dec_month = month_nm
        change = int(row[1]) - month
        total_change += change
        month = int(row[1])
        month_nm = str(row[0])
    month_ct2 = (month_ct - 1)
    avg_change = total_change / month_ct2

#======================================================================================================
#[2] Print to terminal
#======================================================================================================

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {month_ct}")
    print(f"Total: ${total}")
    print(f"Average Change: ${float(round(avg_change, 2))}")
    print(f"Greatest Increase in Profits: {grt_inc_month} (${grt_inc})")
    print(f"Greatest Decrease in Profits: {grt_dec_month} (${grt_dec})")

#======================================================================================================
#[3] Print to .txt file
#======================================================================================================

    output_path = os.path.join("financial_analysis.txt")
    with open(output_path, 'w', newline='') as txtfile:
        txtfile.write("Financial Analysis\n")
        txtfile.write("----------------------------\n")
        txtfile.write(f"Total Months: {month_ct}\n")
        txtfile.write(f"Total: ${total}\n")
        txtfile.write(f"Average Change: ${float(round(avg_change, 2))}\n")
        txtfile.write(f"Greatest Increase in Profits: {grt_inc_month} (${grt_inc})\n")
        txtfile.write(f"Greatest Decrease in Profits: {grt_dec_month} (${grt_dec})\n")
        txtfile.close()