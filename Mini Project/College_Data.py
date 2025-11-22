from termcolor import colored
class student:
    num_students=0
    details=[]
    def __init__(self,name,age,result,year=2025):
        self.name=name
        self.age=age
        self.result=result
        self.year=year
        student.num_students=0
        student.num_students1=0
        student.details.append(self)
    def passed_result(self):
        if self.result>=35:
            student.num_students+=1
            print(colored(f"{self.name} was Passed With {self.result} Marks in {self.year} ","blue"))
    def fail(self):
        if self.result<35:
            student.num_students1+=1
            print(colored(f"{self.name} Failed with the result {self.result} in {self.year}","blue"))
s1=student("Jack",19,40)
s2=student("John",22,35)
s3=student("Deol",23,22)
s4=student("Danny",21,10)
s5=student("Rose",14,12)
print(colored("----DETAILS OF ACADEMIC PASSED AND FAILED STUDENTS--","black"))
print(colored("\n-----PASSED STUDENTS-----","black"))
for st in student.details :
    st.passed_result()

print(colored("\nFAILED STUDENTS","black"))
for st in student.details:
    st.fail()
print("         ")
print(colored(f"The Number Of Students Passed--{student.num_students}","green"))
print(colored(f"The Number of Failed Students---{student.num_students1}","red"))




        