import csv
def write_into_csv(info_list):
    with open("student_indo.csv","a",newline="")as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["name","age","contact number","E-mail"])
        writer.writerow(info_list)
if __name__=="__main__":
    condition =True
    student_num=1
    while(condition):
        std_info=input("Enter the student information in the following format(Name Age Contact Number and Email ID):")

        student_info_list=std_info.split(" ")
        print("entered split list is ",str(student_info_list))
        print(f"name :{student_info_list[0]} \n age{student_info_list[1]}  \n contact number{student_info_list[2]}\n Email{student_info_list[3]}\n")
        choice_check=input("Is the printed info correct")
        if choice_check=="yes":
            write_into_csv(student_info_list)
            condition_check=input("enter (yes or no) if you want to enter information for another student:")
            if condition_check=="yes":

                condition=True
                student_num=student_num+1
            elif condition_check=="no":

                condition=False
        elif choice_check=="no":
            print("\nplease reenter the value!")
