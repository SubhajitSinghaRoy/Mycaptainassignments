#python program to find the circumference of the circle
PI=3.14
radius=float(input("enter the radius to find the area of the circle\n"))
area = PI * radius * radius
print("the area of the circle is:",area)


filename = input("Input the Filename: ")
file_extension = filename.split(".")
#print(file_extension)
if file_extension[1]=="py":
    print("python")
if file_extension[1] =="c":
    print("c language")
if file_extension[1]=="java":
    print("java file")
if file_extension[1]=="docx":
    print("word file")
if file_extension[1] == "xlsx":
    print("excel file")
if file_extension[1] == "csv":
    print("Comma-separated values file")
