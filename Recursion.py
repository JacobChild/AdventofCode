#Recursion.py

#From online https://www.geeksforgeeks.org/recursion-in-python/

# Program to print the fibonacci series upto n_terms

# Recursive function
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

n_terms = 10

# check if the number of terms is valid
if n_terms <= 0:
    print("Invalid input ! Please input a positive value")
else:
    print("Fibonacci series:")
for i in range(n_terms):
    print(recursive_fibonacci(i))


a = 12
b = 2
if (str(a).__contains__(str(b))):
    print("True")
else:
    print("False")
    
#Ping Pong Recursive Function
def PP8s(n, i = 1, k = 1, t = 'u'):
    if i <= n:
        if (str(i).__contains__(str(8)) or i % 8 == 0 and t == 'u'):
            print("second if")
            print(k)
            return PP8s(n, i+1, k-1, t = 'd')
        elif (str(i).__contains__(str(8)) or i % 8 == 0 and t == 'd'):
            print("fourth if")
            print(k)
            return PP8s(n, i+1, k+1, t = 'u')
        elif t == 'u':
            print("first if")
            print(k)
            return PP8s(n, i+1, k+1, t = 'u')
        elif t == 'd':
            print("third if")
            print(k)
            return PP8s(n, i+1, k-1, t = 'd')
        else:
            print("Something went wrong")
    else:
        print("Done, or error")
            

#Calling the function
Whatisthis = PP8s(30)
print(Whatisthis) #! it was none
#? I guess this means two things, I am not actually returning anything, and the built in return statements I have are returning the nth+1 term, not the nth?
print(PP8s(10)) #! still none