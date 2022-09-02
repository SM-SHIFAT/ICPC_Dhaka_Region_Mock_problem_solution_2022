CPU: 1s
Memory: 2048MB


Theorem: If you drop the last digit d of an integer n (n 10), subtract 5d from the remaining integer, then the difference is a multiple of 17 if and only if n is a multiple of 17.

For example, 34 is a multiple of 17, because 3-20=-17 is a multiple of 17; 201 is not a multiple of 17, because 20-5=15 is not a multiple of 17.

Given a positive integer n, your task is to determine whether it is a multiple of 17.


#Input
There will be at most 10 test cases, each containing a single line with an integer n ( 1<= n <= 10^12). The input terminates with n = 0, which should not be processed.


#Output
For each case, print 1 if the corresponding integer is a multiple of 17, print 0 otherwise.

Sample:
  
Input
34
201
2098765413
17171717171718
0

Output
1
0
1
0

#####################
#Here is the solution
#####################
Soluation:
a = int(input())
if(a!=0):
    while (True):
        if (a == 0):
            break
        else:
            b=int(a/10)
            c= int(a%10)
            c= c*5
            b = b - c
            d = b % 17
            if(d==0):
                print("1")
            else:
                print("0")

        a = int(input())
