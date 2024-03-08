#Import our Class students to the main program
from Students import Students

#Print login messagee
print("Welcome in Humber College")

# initialize variables 
applicants = []
neng, nbus, nlaw, nace = 0, 0, 0, 0 

#Password validation function
def pwval(pw):
    count = 1 
    while count < 4:
        digits, capital, symbol  = [], [], []

        for i in pw:
            if i.isdigit():
                digits.append(i)
            elif i.isupper():
                capital.append(i)
            elif not i.isalnum():
                symbol.append(i)
                
        if len(pw) >= 10 and len(capital) >= 1 and (len(digits) == 2 or len(digits) == 3) and len(symbol) == 1:
            print("Password correct")
            return True
        elif count < 3:
            print("Password incorrect, please try again")
            pw = input("Please enter your password. You have " + str(3 - count)+ " attempts left")
            count += 1
        else:
            print("You have tried 3 attempts. Exiting the programme")
            exit(0)
    return False

#Function to check students GPA
def std_GPA():
    std_count = 1
    #Ask the user tp input the number of students 
    while std_count < 4: 
        std = int(input("Enter the no. of students (1-50): "))
        if std_count == 3 and (std < 1 or std > 50): 
            print("Maximum attempts exceeded.")
            exit(0)
        elif std < 1 or std > 50 and std_count < 3:
            print("Enter a value between 1 and 50. You have " + str(3 - std_count)+ " attempts left")
            std_count += 1
        else: break

    for i in range(std):
        #User will input student name and grades
        name = input("Enter the student's name: ")
        mat = float(input("Input your mark in Math: "))
        sci = float(input("Input your mark in Science: "))
        lan = float(input("Input your mark in Language: "))
        dra = float(input("Input your mark in Drama: "))
        mus = float(input("Input your mark in Music: "))
        bio = float(input("Input your mark in Biology: "))
        gpa = (mat * 4 + sci * 5 + lan * 4 + dra * 3 + mus * 2 + bio * 4) / 22

        #Determine which school is the student going
        global neng, nbus, nlaw, nace

        if gpa >= 90 and gpa <=100:
            sch = "School of Engineering"
            neng += 1
        elif gpa >= 80 and gpa <90:
            sch = "School of Business"
            nbus += 1
        elif gpa >= 70 and gpa <80:
            sch = "Law School"
            nlaw += 1
        else:
            sch = "Not Accepted"
            nace += 1
            
        applicants.append(Students(name, mat, sci, lan, dra, mus, bio, gpa, sch))

#Ask the user to input their password
pw = input("Please enter your password. You have 3 attempts:")

if pwval(pw) == True:
    std_GPA()

#Report 1: Student Name, School Name
print("Report No. 1:")
for i in range(len(applicants)):
    print("Student no.", i + 1, applicants[i].r1())

#Report 2: Distribution per School
print("Report No. 2:")
print("No. of students accepted in School of Engineering:", neng)
print("No. of students accepted in School of Business:", nbus)
print("No. of students accepted in Law School:", nlaw)

# print Report 3: No. Students Not Accepted
print("Report No. 3:")
print("No. of students who got rejected:", nace)

# print Report 4: Percentage of students selected in different schools and percentage of students rejected
print("Report No. 4:")
print("percentage of Students accepted in School of Engineering:", (neng/(nace + neng + nbus + nlaw))*100)
print("percentage of Students accepted in School of Business:", (nbus/(nace + neng + nbus + nlaw))*100)
print("percentage of Students accepted in Law school:", (nlaw/(nace + neng + nbus + nlaw))*100)
print("percentage of Students Rejected:", (nace/(nace + neng + nbus + nlaw))*100)