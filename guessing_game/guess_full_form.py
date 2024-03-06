print("Do you want play ? ")
answer =input()

answer_message = {"corr":"correct","incorr":"your answer was worng"}
score = 0

if answer != 'yes':
    quit()

print('let start...')

answer=input('what is the fullform of CPU ? ')
if answer == 'central processing unit':
    print(answer_message["corr"])
    score+=1
else:
    print(answer_message["incorr"])

answer=input('what is the fullform of RAM ? ')
if answer == 'random access memory':
    print(answer_message["corr"])
    score+=1
else:
    print(answer_message["incorr"])


answer=input('what is the fullform of ROM ? ')
if answer == 'read only memory':
    print(answer_message["corr"])
    score+=1
else:
    print(answer_message["incorr"])


answer=input('what is the fullform of HDD ? ')
if answer == 'hard disk drive':
    print(answer_message["corr"])
    score+=1
else:
    print(answer_message["incorr"])


answer=input('what is the fullform of OS ? ')
if answer == 'operating system':
    print(answer_message["corr"])
    score+=1
else:
    print(answer_message["incorr"])

print("Score : "+ str(score))
print("you got : "+str((score/5)*100)+"%")