'''
    @Author: Sudhanshu Kumar
    @Date: 01-10-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 04-10-2024
    @Title : Python program to print the wage of the employee if employee is present or absent

'''

import random

WAGE_HOUR = 20
FULL_WORK = 8
PART_WORK = 4
WORK_DAYS = 20

class Employee:

    def welcome(self):
        print("Welcome to employee Wage Calculation ")

    
    def attendance(self):
        check = random.randint(0,2)
        return check

    def dailyWage(self,wage_per_hour, work_hour):
        """Description: 
            Function to calculate daily wage of Employee
        Parameters:
            wage_per_hour: takes the rate per hour for work
            work_hour: Total work hour
        Returns:
            Daily Wage
        """
        return wage_per_hour*work_hour


    def wageCondition(self,wage_per_hour, full_time_work_hour, part_time_work_hour, working_days):
        """Description: 
            Function to calculate monthly wage of Employee
        Parameters:
            wage_per_hour: takes the rate per hour for work
            work_hour: Total work hour
            working_days: total working days for employee
        Returns:
            Monthly Wage
        """
        att_list = []
        wage_list=[]
        total_hours = 0
        total_wage = 0
        for i in range(1,21):
            if(self.attendance()==0):
                att_list.append("A")
                wage_list.append(0)
            elif self.attendance() ==1:
                total_wage = total_wage+ full_time_work_hour*wage_per_hour
                total_hours = total_hours+full_time_work_hour
                att_list.append("P")
                wage_list.append(full_time_work_hour*wage_per_hour)
                if(total_hours>=100):
                    break
            else:
                total_wage = total_wage+ part_time_work_hour*wage_per_hour
                total_hours = total_hours+part_time_work_hour
                att_list.append("PT")
                wage_list.append(part_time_work_hour*wage_per_hour)
                if (total_hours>=100):
                    break
        print(f"Attendance List of Employee: {att_list}")
        print(f"Daily wage of Employee : {wage_list}")
        return total_wage


def  main():
    emp = Employee()
    emp.welcome()

    print(f"Total Wage of Employee : {emp.wageCondition(WAGE_HOUR,FULL_WORK,PART_WORK,WORK_DAYS)}")

    

if __name__=="__main__":
    main()
        