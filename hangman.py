import os
import random

words = ['python', 'code', 'insight', 'program', 'helloween']
word = random.choice(words)
chances = len(word * 2)
print('You have {:d} chance to guess the word'.format(chances))
output = " _" * len(word)
print(output)
while output.find('_') != -1 and chances > 0:
    guess = input("Alphabet : ").lower()
    chances -= 1
    if guess in word:
        os.system("cls")
        i = 1
        for c in word:
            if guess == c:
                output = output[0:i] + c + output[i + 1:]
            i += 2
        print(output)
    print("Remeaning chances : {:d}".format(chances))
if output.find('_') == -1:
    print('You Won !')
else:
    print('You Lose and got hanged :(')
os.system("pause")
