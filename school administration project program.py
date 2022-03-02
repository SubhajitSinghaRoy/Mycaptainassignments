import csv


def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact number", "Email-ID"])

        writer.writerow(info_list)


if __name__ == '__main__':
    condition = True
    studentnumber=1

    while (condition):
        print("***WELCOME TO THE SCHOOL ADMINISTRATION PROJECT***")
        student_info = input("Enter details of the student number:{} in the format Name Age phone_number Email-ID: ".format(studentnumber))
        student_info_list = student_info.split(' ')
        print("Check if the given details are correct\nName: {}\nAge: {}\nphone Number: {}\nEmail-ID: {}"
                    .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        check=input("Enter 'yes' if the details you have entered is correct or else type 'no' if not!!\n")

        if check=="yes":
            write_into_csv(student_info_list)

            choice = input("Do you want to add some more entries?(yes/no): \n")
            if choice == "yes":
                condition = True
                studentnumber=studentnumber+1
            elif choice == "no":
                condition = False
                print("*******Thank you for using the school administration program!!*******")
        elif check=="no":
            print("Please RE-enter the values again!!\n")