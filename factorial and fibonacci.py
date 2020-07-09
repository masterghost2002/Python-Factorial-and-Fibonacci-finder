##################################### Python-Programm To calculate Fibonacci and Factorial #############################

######## 0 1 1 2 3 5 8 13...etc these are fibonacci number the next number is the sum of first two number  #############

###################### creating function of Fibonacci number ###########################################################
def fibonacci(n):                           ###### n bcz fibonaci are of natural number, now by seeing fibonaci series#
     if n == 1:
         return 0                            ######### as first term in fibonacci series is 0 ##########################
     elif n == 2:
         return 1                            ######## as 2nd term in fibonacci series is 1    ##########################
     else:
         return fibonacci(n-1) + fibonacci(n-2)   ## for any other other value of n expcet 1 or 2 it will add first two fibonaccci no#


############### Now we can create factorial finder by two methods by iterative method and resursive method ############

############## iterative function method  ############################################################################
def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)      ########## here i start for 0 so we enter (i+1) so it will not zero for every value of n#
    return fac

######################## recursive method ##############################################################################

def factorial_resursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_resursive(n-1)

########################################################################################################################
print("Select Operation as 1,2 and 3\n")
select_operation = int(input("1.Fibonacci Finder\n2.Factorial Calculator\n3.For quit\n"))
while select_operation != 3:
    if select_operation == 1:
        number = int(input("Enter which fibonacci you want to find\n"))
        print(f"The {number} fibonacci number is: ", fibonacci(number))
    elif select_operation == 2:
        number = int(input("Enter the number of which factorial you want to find\n"))
        print(f"The factorial of {number} is: ", factorial_iterative(number))
    else:
        print("Thank You For Using\n")
####################### Rakesh Dhariwal ###############################################################################

a = input()  ############ I use this command to prevent exit while we convert py to exe file ########################
