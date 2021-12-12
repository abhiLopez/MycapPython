#Project School Administration 
import csv

def write_into_csv(info_list):
    with open('student_info_csv','a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact","E-Mail"])
            
        writer.writerow(info_list)
if __name__ == '__main__':
    condition= True
    student_num = 1
    
    while(condition):
        student_info=input("Enter some Student Information for student #{} in the Following Format--(Name Age Contact E-Mail): ".format(student_num))
        #print("Entered Information: "+ student_info)
        #split
        student_info_list = student_info.split(' ')
        
        print("Entered Split up Information is: "+str(student_info_list))
        print("\nThe Entered information is-\nName:{}\nAge{}\nContact:{}\nE-mail:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check= input("Is the Information Correct?(Yes/No): ")
        
        if choice_check=="yes":
            write_into_csv(student_info_list)
            
            condition_check =input("Enter (Yes/No) if For Entering Information for another student: ")
            if condition_check=="yes":
                condition = True
                student_num = student_num +1
            elif condition_check == "no":
                condition = False
        elif choice_check == "no":
            print("\nPlease Re-Enter Values!")
        
print("\t\tEND OF PROGRAM\n")   
        