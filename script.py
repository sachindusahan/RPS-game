import random

start = None
user_score = 0
computer_score = 0
def control(select):
    global user_score
    global computer_score
    if select == 1:
        generate = random.randint(1, 3)
        if generate == 1:
            print('YOU: Rock  SCORE: ', user_score)
            print('FRIEND: Rock  SCORE: ', computer_score)
        elif generate == 2:
            computer_score += 10
            print('YOU: Rock  SCORE: ', user_score)
            print('FRIEND: Paper  SCORE: ', computer_score)
        else:
            user_score += 10
            print('YOU: Rock  SCORE: ', user_score)
            print('FRIEND: Scissor  SCORE: ', computer_score)

    elif select == 2:
        generate = random.randint(1, 3)
        if generate == 1:
            user_score += 10
            print('YOU: Paper  SCORE: ', user_score)
            print('FRIEND: Rock  SCORE: ', computer_score)
        elif generate == 2:
            print('YOU: Paper  SCORE: ', user_score)
            print('FRIEND: Paper  SCORE: ', computer_score)
        else:
            computer_score += 10
            print('YOU: Paper  SCORE: ', user_score)
            print('FRIEND: Scissor  SCORE: ', computer_score)

    elif select == 3:
        generate = random.randint(1, 3)
        if generate == 1:
            computer_score += 10
            print('YOU: Scissor  SCORE: ', user_score)
            print('FRIEND: Rock  SCORE: ', computer_score)
        elif generate == 2:
            user_score += 10
            print('YOU: Scissor  SCORE: ', user_score)
            print('FRIEND: Paper  SCORE: ', computer_score)
        else:
            print('YOU: Scissor  SCORE: ', user_score)
            print('FRIEND: Scissor  SCORE: ', computer_score)
    else:
        print('input Error')


while start != 'no':
    tools = ['1.Rock', '2.Paper', '3.Scissor']
    for tool in tools:
        print(tool)
    check = int(input('Enter your choice: '))

    # Call to the control function
    control(check)
    if computer_score == 100:
        print('You lose')
        start = input('Are you want to replay(yes/no)')
    elif user_score == 100:
        print('You won')
        start = input('Are you want to replay(yes/no)')
    