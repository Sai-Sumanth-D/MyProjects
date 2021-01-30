# A simple voting system using python.

nominee_1 = input('Enter the name: ')
nominee_2 = input('Enter the name: ')

n_1_votes = 0
n_2_votes = 0

# this is going to be the list of the people who are going to vote and their id's
voters_id_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# to have a basic idea of number of voters
num_voters = len(voters_id_numbers)

while True:
    if voters_id_numbers == []:
        print('Voting Session is Over.')
        if n_1_votes > n_2_votes:
            percent = (n_1_votes/num_voters) * 100
            print(nominee_1, "has won!!!", "with", percent,  "% votes")
        elif n_2_votes > n_1_votes:
            percent = (n_2_votes/num_voters)*100
            print(nominee_2, "has won!!!!", "with", percent, "% votes")

    else:
        # asking the voters thier id to start voting
        task1 = int(input('Please enter your voter id : '))
        if task1 in voters_id_numbers:
            print('You are eligible to vote.')
            # to remove the task1 from voters_id_numbers, to prevent multiple voting
            voters_id_numbers.remove(task1)
            voters_choice = int(input('Enter your choice of vote 1 or 2? '))
            if voters_choice == 1:
                n_1_votes += 1
                print('Thank you!!')
            elif voters_choice == 2:
                n_2_votes += 1
                print('Thank you!!')
            else:
                print('You are not a voter or you have already voted. ')
