import random
import hangman_arts
import hangman_words
# words = ['ardvark', 'second', 'badguti']
chosen_one = random.choice(hangman_words.word_list)

the_shown_ans = []
for _ in range(len(chosen_one)):
    the_shown_ans.append('_')

print(hangman_arts.logo)
print(
    f'Psst, the word is {chosen_one}'
)


def the_process(lives, stages):

    if user_inp in chosen_one:
        for i in range(len(chosen_one)):
            if user_inp == chosen_one[i]:
                the_shown_ans[i] = user_inp
        print("".join(the_shown_ans))
        print(stages[lives])
        return 0

    else:
        print("".join(the_shown_ans))
        lives -=1
        print(stages[lives])
        return 1





result = 0


lives = 6
print(hangman_arts.stages[lives])
while (lives>0):
    if '_' in the_shown_ans:
        user_inp = input('Guess a letter:')
        val = the_process(lives, hangman_arts.stages)
        if val == 1:
            lives-=1

    else:
        print("YOU WIN!!!")
        result = 1
        break

if result != 1:
    print("YOU'RE DEAD")
    

input('press any key to exit...')