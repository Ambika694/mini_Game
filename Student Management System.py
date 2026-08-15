print("===============================")
print(" 🎓 STUDENT MANAGEMENT SYSTEM")
print("===============================")

print("1. Add stunent")
print("2.View All Students")
print("3. Search stunent")
print(" 4. update stunent")
print(" 5.  Delete Student")
print( "6.   view Average Marks")
print(" 7 . View Top Student")
print(" 8   Exit")

student = []
while True:
    option = input("Enter your choice:")
    if option == "1":
        Name = input("Enter student name")
        Roll = int(input("Enter roll number"))
        Age  = int(input("Enter age:"))
        Course = input("Enter course")
        Marks = int(input("Enter marks"))
        
    
    
        new_student = {
        "name": Name,
        "roll_no": Roll,
        "age": Age,
        "course": Course,
        "marks": Marks
        }
        
        student.append(new_student)
        
        print("Student added successfully!")
    elif option == "2":
        if not student:
            print("No students yet.")
        else:
            for i, stu in enumerate(student, start=1):
             print(f"{i}. Name: {stu['name']} | Roll No: {stu['roll_no']} | Age: {stu['age']} | Course: {stu['course']} | Marks: {stu['marks']}")
    
    
    elif option == "3":
        found =False
        if not student:
            print("No students yet")
        else:
            search = int(input("Enter roll number to search"))
            for stu in student:
              if search == stu["roll_no"]:
                print("Student Found!")
                print(f"Name: {stu['name']}")
                print(f"Roll No: {stu['roll_no']}")
                print(f"Age: {stu['age']}")
                print(f"Course: {stu['course']}")
                print(f"Marks: {stu['marks']}")
                found = True

        if not found:
          print("❌ Student not found.")
    
    
    elif option == "4":
        if not student:
            print("No students yet")
        else:
            found = False
            roll_update = int(input("Enter roll number to update"))
            new_name = input("enter the name ")
            new_age  = int(input("enter the Age"))
            new_course = input("enter the course")
            new_marks = int(input("Enter the marks :"))
            for stu  in student:
              if  roll_update == stu["roll_no"]:
                
                stu["name"] = new_name
                stu["age"] = new_age
                stu["course"] = new_course
                stu["marks"] = new_marks
                found = True
                print("✅ Student updated successfully!")
              
            if not found:
             print("❌ Student not found.")
                       
    elif option == "5": 
        found = False 
        if not student:
            print("No students yet")
        else:
            delete =  int(input("Enter roll number to delete: "))
            for stu in student:
                if delete == stu["roll_no"]:
                 student.remove(stu)
                print("✅ Student deleted successfully!")
                found = True
                break
              
            if not found:
                 print("❌ Student not found.")
            
    elif option == "6":
        if not student:
            print("No students yet.")
        else:
            total = sum( stu['marks']for  stu in student)
            avg = total/len(student)
            print(f"Average Marks: {avg}")
       
    elif option == "7":
        if not student:
            print("No students yet.")
        else:
            
            top_student = max(student, key=lambda stu: stu["marks"])
            print("🏆 Top Student:")
            
          
            print(f"Name: {top_student['name']}")
            print(f"Roll No: {top_student['roll_no']}")
            print(f"Age: {top_student['age']}")
            print(f"Course: {top_student['course']}")
            print(f"Marks: {top_student['marks']}")
            
    elif option == "8":
        print("Goodbye! Thanks for using Student Management System.")
        break
           

           
                
                    
            