# python program to print all the positive numbers from a given list
list = []
element = int(input("enter the number of element you want to add in the list\n"))
for i in range(element):
    ele = int(input("enter the element\n"))
    list.append(ele)
print("the list is:", list)
print("Therefore All positive numbers of the list is : ")
for val in list:
    if val >= 0:
        print(val,end = " ")
