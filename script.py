import random
import time


end_c = '\033[0;0m'
red = '\033[2;31;40m'
green = '\033[2;32;40m'

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
        print(f'{red}input Error{end_c}')


while start != 'no':
    tools = ['1.Rock', '2.Paper', '3.Scissor']
    for tool in tools:
        print(tool)
    check = int(input('Enter your choice: '))

    # Call to the control function
    control(check)
    prompt = f'Are you want to replay({green}yes{end_c}/{red}no{end_c}): '
    if computer_score == 100:
        print('You lose')
        start = input(prompt)
        time.sleep(0.2)
        print(f'{red}-{end_c}', end="")
    elif user_score == 100:
        print('You won')
        start = input(prompt)
        time.sleep(0.2)
        print(f'{red}-{end_c}', end="")