#python program to find how many times the letters occur in the word
random_list = input("enter the word to find the frequency of the letters:\n")
frequency = {}
for item in random_list:
   if item in frequency:
    frequency[item] += 1
   else:
    frequency[item] = 1
print(frequency)
