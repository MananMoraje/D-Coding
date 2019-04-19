

class LoopVars:
    i = 0
    j = 0


aim = input('What is the target number?     ')
if aim.isalpha():
    print('That is not entirely numbers.')
nums = input('What are the option numbers? (Separate with spaces)      ')
n = []
num = []
if len(nums) > 9:
    print('To many digits/spaces')
while LoopVars.j < len(nums):
    n.append(nums[LoopVars.j])
    LoopVars.j += 1
while LoopVars.i <= len(n):
    if n[LoopVars.i] != ' ':
        num.append(int(n[LoopVars.i]))

print('The target number is: ' + aim)
print('The numbers I can use are ', str(nums))
c = input('Confirmation. If the information above is correct, type\'yes\' else, type\'no\' ')
#  def getnum(target, numbers):
input('Press ENTER to exit')
