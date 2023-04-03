
num_candidates = int(input("Enter the number of candidates: "))
candidates = []
for i in range(num_candidates):
    name = input("Enter the name for candidate " + str(i+1) + ": ")
    candidates.append({'name': name, 'votes': 0})

num_voters = int(input("Enter the number of voters: "))
for i in range(num_voters):
    vote = input("Voter " + str(i+1) + ", who do you vote for? ")
    for candidate in candidates:
        if vote == candidate['name']:
            candidate['votes'] += 1

winner = max(candidates, key=lambda x: x['votes'])
print("The winner is " + winner['name'] + " with " + str(winner['votes']) + " votes.")
print("Results:")
for candidate in sorted(candidates, key=lambda x: x['votes'], reverse=True):
    print(candidate['name'] + ": " + str(candidate['votes']) + " votes")
