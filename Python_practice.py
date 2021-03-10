counties = ["Arapahoe","Denver","Jefferson"]
counties    
counties[0]
print(counties[2])
print(counties[-1])
len(counties)
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict
counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.get("Denver")
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data

   counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
     for voters in counties_dict.values():
    print(voters)

voting_data = [{f"county":"Arapahoe", "registered_voters": 422829:,},
                {f"county":"Denver", "registered_voters": 463353:,},
                {f"county":"Jefferson", "registered_voters": 432438:,}]

for county_dict in voting_data:
    print(county_dict)



 counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
 print(f"{county} county has {voters:,} registered voters.")

 candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)