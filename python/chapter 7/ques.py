# # 1. Write a program to print multiplication table of a given number using for loop.
# n = int(input("Enter the number to print multiplication table of a given number : "))
# for i in range (1,11):
#     print(i*n)

# # 2. Write a program to greet all the person names stored in a list 'l' and which starts with S.
# l=["Harry", "Soham", "Sachin", "Rahul"]
# for i in l:
#     if (i == 0):
#         continue
#     if (i == 3):
#         break
#     print("Hello dear ",i)

# # 3. Attempt problem 1 using while loop.
# n = int(input("Enter your number to print multiplication table of a given number : "))
# i = 1
# while(i<11):
#     print(i*n)
#     i +=1

# # 4. Write a program to find whether a given number is prime or not.
# n = int(input("Enter your number to find whether a given number is prime or not : "))
# isPrime = True
# for i in range (2,n):
#     if(n%i==0):
#         isPrime = False
#         break
#     else:
#         isPrime = True
# print(isPrime)

# # 5. Write a program to find the sum of first n natural numbers using while loop.
# n = int(input("Enter your number to get sum of first n natural numbers : "))
# i = 1
# sum = 0
# while(i<=n):
#     sum +=i
#     i +=1
# print(sum)

# 6. Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter your number to calculate the factorial of a given number : "))
for i in range (n):
    fact = n*(n-1)


# 7. Write a program to print the following star pattern.
# ***
# ***** for n=3

# 8. Write a program to print the following star pattern:
# **
# *** for n = 3

# 9. Write a program to print the following star pattern.
# ***
# for n = 3
# ***

# 10. Write a program to print multiplication table of n using for loops in reversed order.