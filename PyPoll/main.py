#======================================================================================================
#[0] Setup
#======================================================================================================

import os
import csv
file = 'GT-ATL-DATA-PT-12-2019-U-C/Homework/03-Python/Instructions/PyPoll/Resources'
csvpath = os.path.join('..','..', file, 'election_data.csv')

#======================================================================================================
#[1] 1st Loop & Print Values to terminal
#======================================================================================================

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total_votes = 0
    candidate_nms = []
    candidate_winner = ""
    candidate_votes = 0
    candidate_winner_votes = 0
    vote_sum = 0
    for row in csvreader:
        total_votes += 1
        if len(candidate_nms) > 0:
            if any(i["name"] == row[2] for i in candidate_nms):
                for x in candidate_nms:
                    if(x["name"] == row[2]):
                        x["votes"] = x["votes"] + 1
            else:
                candidate_nms.append({"name": row[2], "votes": 1})
        else:
            candidate_nms.append({"name": row[2], "votes": 1})

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

#======================================================================================================
#[2] 2nd Loop & Print Values to terminal
#======================================================================================================

    for candidate in candidate_nms:
        if candidate_winner_votes < candidate['votes']:
            candidate_winner_votes = candidate['votes']
            candidate_winner = candidate['name']
        print(f"{candidate['name']}: {round((candidate['votes'] / total_votes)*100, 2)}% ({candidate['votes']})")

    print("-------------------------")
    print(f"Winner: {candidate_winner}")
    print("-------------------------")

#======================================================================================================
#[3] Print Values to .txt
#======================================================================================================

    output_path = os.path.join("election_results.txt")
    with open(output_path, 'w', newline='') as txtfile:
        txtfile.write("Election Results\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Total Votes: {total_votes}\n")
        txtfile.write("-------------------------\n")
        for candidate in candidate_nms:
            txtfile.write(f"{candidate['name']}: {round((candidate['votes'] / total_votes)*100, 2)}% ({candidate['votes']})\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Winner: {candidate_winner}\n")
        txtfile.write("-------------------------\n")
        txtfile.close()