class employee:

     company ="Google"
    # address ="narayan nagar"
     def getsalary(self,signature):
       print(f"Salary for this employee working in  {self.company} is {self.Salary}\n{signature}")

     @staticmethod
     def greet():
        print("good morning, sir")


     @staticmethod
     def time():
          print("the time is 9 am in the morning")


komal = employee()
komal.Salary = 100000

komal.getsalary("Thanks!")#Employee.getsalary(komal)
komal.greet()
komal.time()