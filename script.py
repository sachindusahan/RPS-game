import random

user_score = None
computer_score = None
start = None

def control(select):
    if select == 1:
        print('waiting code...')


while start != 'no':
    tools = ['1.Rock', '2.Paper', '3.Scissor']
    for tool in tools:
        print(tool)

    check = int(input('Enter your choice: '))

    # Call to the control function
    control(check)