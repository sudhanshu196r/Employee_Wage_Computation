'''

    @Author: Neelesh Rawat
    @Date: 12-03-2022
    @Last Modified by: Neelesh Rawat
    @Last Modified time: 12-03-11
    @Title : Write a Python program to get a list, sorted in increasing order by the last
             element in each tuple from a given list of non-empty tuples.

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
    return check


def dailyWage(wage_per_hour, work_hour):
    """Description: 
        Function to calculate daily wage of Employee
    Parameters:
        wage_per_hour: takes the rate per hour for work
        work_hour: Total work hour
    Returns:
        Daily Wage
    """
    return wage_per_hour*work_hour

def monthlyWage(wage_per_hour, work_hour, working_days):
    """Description: 
        Function to calculate monthly wage of Employee
    Parameters:
        wage_per_hour: takes the rate per hour for work
        work_hour: Total work hour
        working_days: total working days for employee
    Returns:
        Monthly Wage
    """
    return wage_per_hour*work_hour*working_days


def main():
    welcome()
    wage_per_hour = 20
    fulltime_work = 8
    part_time_work = 4
    working_days = 20
    if(attendance()==0):
        print("Absent")
    elif attendance() ==1:
        print("Present")
        print(f"Daily wage of Full Time Employee is {dailyWage(wage_per_hour,fulltime_work)}")
        print(f"Monthly wage of Full Time Employee is {monthlyWage(wage_per_hour,fulltime_work,working_days)}")
    else:
        print("Present")
        print(f"Daily wage of Part Time Employee is {dailyWage(wage_per_hour,part_time_work)}")
        print(f"Monthly wage of Part Time Employee is {monthlyWage(wage_per_hour,part_time_work,working_days)}")
    

if __name__=="__main__":
    main()