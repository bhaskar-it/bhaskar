import random
word=['apple','ball','cat','dog','parato','letter','banana']
chosen=random.choice(word)
lives=len(chosen)
display=[]
for i in range(len(chosen)):
    display += '-'
print(display)
game=False
while not game:
    guess_word=input("guess a letter:").lower()
    for position in range(len(chosen)):
        letter=chosen[position]
        if letter == guess_word:
            display[position]=guess_word
    print(display)
    if guess_word not in chosen:
        lives -= 1
    if lives == 0:
        game=True
        print("you lose.....")
if '-' not in display:
    game=True
    print("you win....")
