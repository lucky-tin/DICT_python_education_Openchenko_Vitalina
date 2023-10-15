print('Hello! My name is lucky-tin. \n I was created in 2023.')
your_name = input('Please, remind me your name.\n')
print(f'What a great name you have, {your_name}!')
print('Let me guess your age.')
remainder3 = int(input('Enter remainders of dividing your age by 3: \n'))
remainder5 = int(input('Enter remainders of dividing your age by 5: \n'))
remainder7 = int(input('Enter remainders of dividing your age by 7: \n'))
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {your_age}; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')
number = int(input('Enter a positive number:\n'))
for i in range(number + 1):
    print(f'{i}!')
print("Let's check how Ukrainian you are")
print('What is the national dish in Ukraine?')
print('1. Soup')
print('2. Vareniki')
print('3. Borsch')
print('4. Spaghetti')
correct_answer = 3
while True:
    answer = int(input('>'))
    if answer == correct_answer:
        break
    else:
        print('Please, try again.')
print('Completed, have a nice day!')