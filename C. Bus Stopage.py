Score: 1
  
CPU: 1s
Memory: 2048MB

Bus service of Dhaka is life saving for many people. It’s the cheapest way of travel among the city, and it’s even cheaper for the students due to half fare. So many students ride the bus to go to their institutions (schools, colleges or universities).

Government of Bangladesh wants this to be even cheaper for the students. That’s why they are starting a special bus service for school students. This bus service will start from the start of the city and will go to the end (I know it seems weird, but try to imaging Dhaka as a linear city). There are N stoppages among this route and in every stoppage few gets on the bus and few people gets off. This number is always fixed because students don’t change home or school that often. Now the authority has one problem and that is determining the size of the bus. The bus should be as big as that it can accommodate the students at every stoppage. Let’s see an example. Suppose there are 4 stoppages. In first stoppage 5 people gets on the bus. In the second stoppage 4 people gets on and 2 gets off. So when leaving the second stoppage there are in total 7 people in the bus. In the third stoppage 3 people gets on and 4 gets off. So while leaving the third stoppage there are 6 people in the bus and the bus reaches to fourth and final stoppage with these 6 people. So the bus size must be 7 or higher because otherwise it won’t be able to accommodate all the students from the second stoppage.

Given the information about the stoppages, you need to find the minimum size of the bus that’s needed to accommodate all the students.


#Input
Input will start with an integer, T, the number test cases. Each case will start with N (2<=N<=20000). Next there will be N-1 lines each with two integers A and B (0<=A,B<=20000), where in the ith line A is the number of people gets on bus and B is the number of people gets off at ith stoppage.


#Output
Output a line for each case, “Case T: Size” where T is the case number and Size is the minimum required size of the bus.


Sample:
Input	
2
4
5 0
4 2
3 4
2
4 0

Output
Case 1: 7
Case 2: 4
  
  
##################
##   Solution   ##
##################

T = int(input())

for x in range(T):
    total = 0
    highest = 0
    N = int(input())
    for y in range(N-1):
        temp = input()
        temp1 =temp.split()
        a = int(temp1[0])
        b = int(temp1[1])
        total = (total+a)-b
        if(total>highest):
            highest = total

    print("Case " + str(x+1) +": "+str(highest))
  
