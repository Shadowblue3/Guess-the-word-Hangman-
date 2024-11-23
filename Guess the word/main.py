import random
import words

print("Hello!! Welcome to the Word guessing game")
#Game variables
level = input("Please select the difficulty: \n >> Easy(10 guess)\n >> Medium(7 guess)\n >> Hard(4 guess)\n:")
guess = -1
temp = random.randint(0, len(words.d))
word = ""
user_guess = ""
ans_list = []

while(guess == -1):
    if(level.lower() == "easy"):
        guess = 7
    elif(level.lower() == "medium"):
        guess = 4
    elif(level.lower() == "hard"):
        guess = 1
    else:
        print("Invalid choice!! please type any of the 3 dificulties")
        level = input("Please select the difficulty: \n >> Easy(7 attempts)\n >> Medium(4 attempts)\n >> Hard(1 attempts)\n:")
        guess = -1

for key in words.d:
    word = key
    temp -= 1
    if(temp == 0):
        break
# print(word, words.d[word])

#Game functions
def modify_answer_list(ans_list, user_guess, word, guess):
    temp = 0
    if(user_guess in word.lower()):
        for i in range(len(word)):
            if(user_guess.lower() == word[i].lower()):
                ans_list[i] = word[i]
        return ans_list, guess
    else:
        print("The letter is not present")
        guess -= 1
        print(f"Remaining attempt: {guess}\n")
        return ans_list, guess

#making the answer list
answer = ""
for i in range(len(word)):
    answer += "-"
print(answer)

for i in answer:
    ans_list.append(i)

while(answer != word and guess != 0):
    print(f"Try guessing the word, catagory: {words.d[word]}")
    user_guess = input(f"Try guessing   Remaining attempt: {guess}\n")
    if(len(user_guess) > 1):
        print("Warning! One letter at a time")
        print(answer)
        print()
        continue
    else:
        ans_list, guess = modify_answer_list(ans_list, user_guess, word, guess)
        answer = "".join(ans_list)
        print(answer)
        print()
    
if(guess == 0):
    print(f"The word is {word}...Better luck next time")
if(guess != 0):
    print("Congrats!!!")