# guess game

from random import randint

secret_numb = randint(1, 100)
i = 1

print(f'horus {secret_numb}')
answer = input("Try guess number between 1-100: ")

while secret_numb != int(answer):
    if secret_numb > int(answer):
        print("for a small number")
    else:
        print("for large a number")
    i += 1
    answer = input('try again: ')
print(f'You win in {i} times!')



