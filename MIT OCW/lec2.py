#
# ###################
# # EXAMPLE: while loops
# # Try expanding this code to show a sad face if you go right
# # twice and flip the table any more times than that.
# # Hint: use a counter
# ###################
# n = input("You are in the Lost Forest\n"
#           "****************\n****************\n "
#           ":)\n****************\n****************\n"
#           "Go lefsdt or right? ")
#
# t = 0
#
# while n == "right" or n == "Right":
#    t += 1
#    if t == 2:
#       n = print("You are in the Lost Forest\n****************\n"
#              "******       ***\n :( :( :(\n****************"
#              "\n****************\nGo left or right? ")
#    else:
#       n = input("You are in the Lost Forest\n****************\n"
#              "******       ***\n  (╯°□°）╯︵ ┻━┻\n****************"
#              "\n****************\nGo left or right? ")
#
# print("\nYou got out of the Lost Forest!\n\o/")





###################
# EXAMPLE: perfect squares
###################
ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
   neg_flag = True

if neg_flag == False:
   while ans**2 < x:
      ans = ans + 1
   if ans**2 == x:
      print("Square root of", x, "is", ans)
   else:
      print(x, "is not a perfect square")
elif neg_flag:
   while ans ** 2 < -x:
      ans = ans + 1
      if ans ** 2 == -x:
            print("Square root of", x, "is", ans)


###################
# TEST YOURSELF!
# Modify the perfect squares example to print
# imaginary perfect sqrts if given a negative num.
###################