import random

start = None

def control(select):
    user_score = None
    computer_score = None

    if select == 1:
        generate = random.randint(1, 3)
        if generate == 1:
            user_score += 0
            computer_score += 0
            print('YOU: Rock  SCORE: ')
            print('FRIEND: Rock  SCORE: ' )

while start != 'no':
    tools = ['1.Rock', '2.Paper', '3.Scissor']
    for tool in tools:
        print(tool)

    check = int(input('Enter your choice: '))

    # Call to the control function
    control(check)