import os 
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# define variable for calculating the total number of votes cast
ballots = []
# define variable for determining candidates who received votes
candidates = []

# perfrom  chocolate cake recipe to bring in csv file
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    # loop through rows of csv file
    for row in csvreader:
        
        # this will be used to simply calculate the length of the list to determine number of votes cast
        ballots.append(row)

        # determine unique candidates with if statement. if the name appears in list already, then nothing happens, else if its not in the list yet, append the list to include
        if row[2] in candidates:
            candidates = candidates
        else:
            candidates.append(row[2])

total_ballots = len(ballots)
total_candidates = len(candidates)

# perfrom  chocolate cake recipe again to be able to perform another for loop
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)  

    # create three trackers to count the total votes for each candidate
    tracker_1 = 0
    tracker_2 = 0
    tracker_3 = 0
    
    # loop through rows of csv file to calculate number of votes each candidate received   
    for row in csvreader:

        if row[2] == candidates[0]:
            tracker_1 += 1        
        elif row[2] == candidates[1]:
            tracker_2 += 1
        elif row[2] == candidates[2]:
            tracker_3 += 1

# print(tracker_1)
# print(tracker_2)
# print(tracker_3)
# print(tracker_1 + tracker_2 + tracker_3)
print("A total of " + str(total_ballots) + " votes were cast this year.")
print(candidates[0] + " received %" + str(round((tracker_1/total_ballots)*100, 2)) + " of the votes with " + str(tracker_1) + " total votes.")
print(candidates[1] + " received %" + str(round((tracker_2/total_ballots)*100, 2)) + " of the votes with " + str(tracker_2) + " total votes.")
print(candidates[2] + " received %" + str(round((tracker_3/total_ballots)*100, 2)) + " of the votes with " + str(tracker_3) + " total votes.")

if (tracker_1 > tracker_2) and (tracker_1 > tracker_3): 
    print("Winner: " + candidates[0])
elif (tracker_2 > tracker_1) and (tracker_2 > tracker_3): 
    print("Winner: " + candidates[1])
elif (tracker_3 > tracker_1) and (tracker_3 > tracker_2): 
    print("Winner: " + candidates[2])

# create text file to display results

txtpath = os.path.join('Analysis', 'election_results.txt')

with open(txtpath, 'w') as txtfile:

    # write text to election_results.txt file
    txtfile.write("ELECTION RESULTS")
    txtfile.write('\n')
    txtfile.write("-------------------------------")
    txtfile.write('\n')
    txtfile.write("A total of " + str(total_ballots) + " votes were cast this year.")
    txtfile.write('\n')
    txtfile.write(candidates[0] + " received %" + str(round((tracker_1/total_ballots)*100, 2)) + " of the votes with " + str(tracker_1) + " total votes.")
    txtfile.write('\n')
    txtfile.write(candidates[1] + " received %" + str(round((tracker_2/total_ballots)*100, 2)) + " of the votes with " + str(tracker_2) + " total votes.")
    txtfile.write('\n')
    txtfile.write(candidates[2] + " received %" + str(round((tracker_3/total_ballots)*100, 2)) + " of the votes with " + str(tracker_3) + " total votes.")
    txtfile.write('\n')
    if (tracker_1 > tracker_2) and (tracker_1 > tracker_3): 
        txtfile.write("Winner: " + candidates[0])
    elif (tracker_2 > tracker_1) and (tracker_2 > tracker_3): 
        txtfile.write("Winner: " + candidates[1])
    elif (tracker_3 > tracker_1) and (tracker_3 > tracker_2): 
        txtfile.write("Winner: " + candidates[2])