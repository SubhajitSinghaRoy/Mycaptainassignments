# Program to display the Fibonacci numbers up to n-th term
count = 0
n = int(input("How many terms do you want to print the fibonaaci numbers?\n"))
n1, n2 = 0, 1
print("Fibonacci sequence is:")
while count<n:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count=count+1