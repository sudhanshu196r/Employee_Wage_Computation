'''
    @Author: Sudhanshu Kumar
    @Date: 01-10-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 04-10-2024
    @Title : Python program to print the wage of the employee if employee is present or absent

'''

import random


def welcome():
    """
    Description: 
        Function to display welcome message
    Parameters:
        None
    Returns:
        None
    """

    print("Welcome to Employee Wage Computation")


def attendance():
    """
    Description: 
        Function to check employee is present or absent
    Parameters:
        None
    Returns:
        Present or Absent
    """
    check = random.randint(0,2)
    print(check)
    return check


def dailyWage(wage_per_hour, work_hour):
    """Description: 
        Function to calculate daily wage of Employee
    Parameters:
        wage_per_hour: rate of wage per hour
        work_hour : total hour of work done
    Returns:
        Daily Wage
    """
    return wage_per_hour*work_hour




def main():
    welcome()
    wage_per_hour = 20
    fulltime_work = 8
    part_time_work = 4
    if(attendance==0):
        print("Absent")
    elif attendance==1:
        print("Present")
        print(f"Daily wage of Full Time Employee is {dailyWage(wage_per_hour,fulltime_work)}")
    else:
        print("Present")
        print(f"Daily wage of Part Time Employee is {dailyWage(wage_per_hour,part_time_work)}")

    

if __name__=="__main__":
    main()