from random import *
#  Functions


def ifint(d):
    nums = [int(s) for s in str.split(d) if s.isdigit()]
    return(str(nums) + ' ' + str(len(nums)))

#Sayings / Responces
StudySub = ['Eng. Lang.', 'Eng. Lit.', 'Math', 'Chemistry', 'Physics', 'Biology', 'Computer Science', 'Geography', 'History']
Greet = ['Hello.', 'How are you?', 'Hey!', 'Hi.']
MathReq = ['What is','what is', 'add', 'subtract', 'multiply', 'divide']

#Randoms - varName + 'Rand' eg.
GreetRand = randint(0, len(Greet))
StudySubRand = randint(0, len(StudySub))

"""
=======================================================================================================================================================================================================================================================================================================
Conversation ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
=======================================================================================================================================================================================================================================================================================================
"""
#Instructions
print('Please only use lower-case letters and numbers. No upper-case letters nor special symbols. ')

#Start Variables - varName + 'Stt' eg.
GreetStt = input(Greet[GreetRand])


#Checking for commands
i = 0
if IfInt(GreetStt):
    print()
        
# Response
input('Press ENTER when you are finished.')
