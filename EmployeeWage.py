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
    print(check)
    return check


def dailyWage(wage_per_hour, work_hour):
    """Description: 
        Function to calculate daily wage of Employee
    Parameters:
        None
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