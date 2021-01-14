# My first ever game project using python#

print('Welcome to the Game!')
name = input('Please enter your name: ')
age = int(input('Can I know your Age please? '))


if age >= 18:
    print('Okay, Are you ready for this? ')

    want_to_play = input(" yes/no: ")
    if want_to_play.upper() == "YES":
        print(" Let's get started then. ")
        Health = 100
        print('You are starting with', Health, 'health')
        print('So, You have been to an adventure trip for the holidays and have to decide the direction in the middle of the forest')

        first_choice = input('First Choice.. Left or Right (Left/Right): ')
        if first_choice.upper() == "LEFT":
            ans = input(
                ' Nice, You better follow the path upto a Lake.. You can swim right? (Yes/No): ')

            if ans.upper() == "YES":
                print(
                    'Alright, Hope you reach the other end safe as there are a few sharks in there...'
                    'OOPS!!!! You got bit by a shark and lost half of your health. ')

                choice = input(
                    'You are hurt now..You can see a path and a Hut to take rest. What would you choose?(Path or Hut): ')
                if choice.upper() == "HUT":
                    print(
                        " As you don't have any medical supplies,", "And there is a severe blood loss from your wound", " Your health is zero now",
                        "You lost the game choosing to stay at the Hut :( ")

                else:
                    print(
                        'Maybe you made a good decision choosing the path to proceed forward.')
                    help_choice = input(
                        ' You can now see a road and a car parked to the side of the road, which one do you choose now? (Car/Road)?: ')
                    if help_choice.upper() == "CAR":
                        print(
                            ' As the car is not yours, You wasted a lot of time trying to unlock it and lost your health. You lost the game :( ')
                    else:
                        print(
                            ' As you now chose to walk along the road, You have found a small village with a hospital, You saved your life, saving your game :) ')

                        exit_choice = input(
                            'As you are now treated and good to leave the village to your house. Do you choose leaving to your House?(Yes/No):  ')

                        if exit_choice.upper() == "YES":
                            print(
                                ' Well you made it safe to your House and good to have your normal life. ')
                        else:
                            print(
                                'Well then, You can stay here for sometime relax and then leave.')

            else:
                print(
                    " As you can't swim, you lost the game as you failed to reach the other end ! ")

        else:
            print(' You fell Down, Lost the Game :( ')

    else:

        print('Okay byee!')


else:
    print(' You are not old enough to play')
