# list_with_tuples = eval(input("Enter a list of tuples (e.g. [(1, 2), (3, 4)]): "))
# #list_with_tuples = [(1,2),(2,5),(5,6),(1,5),(1,7),(2,9),(4,0),(1,2)]
# k = 1
# t = 0
# final =[]
# for i in list_with_tuples:
#         count = 0
#         for j in list_with_tuples:
#             if i[0] == j[0]:
#                 count+=1
#         if count > 1:
#             final.append(i)
# print(final)

i = input("enter num1: ")
j = input("enter num2: ")
k = input("enter num3: ")
try:
    num1 = int(i)
    num2 = int(j)
    num3 = int(k)
    print(num1 + num2)
    
except ValueError:
    print("Invalid input")
    
def even_odd(num):
    if int(num) % 2 == 0:
        return "Even"
    else:    return "Odd"

print(even_odd(num1))
print(even_odd(num2))
print(even_odd(num3))

def largest(*args):
    return max(args)
print(largest(num1, num2, num3))
    
def swap(a,b):
    return b, a
print(swap(num1, num3))
print (num1, num2, num3)

def factorial(n):
    if n ==0 or n==1:
        return 1
    else:
        return n * factorial(n-1) 
print(factorial(num1))
print(factorial(num2))
print(factorial(num3))      

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")
multiplication_table(num1)
multiplication_table(num2)
multiplication_table(num3)    

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

print(sum_of_digits(num1))
print(sum_of_digits(num2))
print(sum_of_digits(num3))

def reverse_number(n):
    return int(str(n)[::-1])

print(reverse_number(num1))
print(reverse_number(num2))
print(reverse_number(num3))

def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(prime_number(num1))
print(prime_number(num2))
print(prime_number(num3))
k = input("Enter a string: ")
def reverse_string(k):
    return k[::-1]

print(reverse_string(k))

def palindrome_string(k):
    if k == k[::-1]:
        return "Palindrome"
    else:
        return "Not a palindrome"
print(palindrome_string(k))  

def count_vowels(k):
    vowels = "aeiouAEIOU"
    count = 0
    for char in k:
        if char in vowels:
            count += 1
    return count
print(count_vowels(k))

def count_consonants(k):
    vowels = "aeiouAEIOU"
    count = 0
    for char in k:
        if char.isalpha() and char not in vowels:
            count += 1
    return count
print(count_consonants(k))

def count_words(k):
    words = k.split()
    return len(words)
print(count_words(k))

def count_characters_frequency(k):
    frequency = {}
    for char in k:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency
print(count_characters_frequency(k))
