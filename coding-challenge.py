# Print out all of the numbers in the following array that are divisible by 3:
# [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# The expected output for the above input is:
# 27
# 81
# 9
# 27
# 99
# 63
# 42
# You may use whatever programming language you wish.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

#UPER
#Understanding problem

#Planning
#for loop - if %3 == 0 print 
#Execute

a = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

for item in a: #O(n)
  if (item %3 == 0): #O(1)
    print(item) #O(1)

#Reflect
#O(n) is worst case
#could not have found better solution for this problem