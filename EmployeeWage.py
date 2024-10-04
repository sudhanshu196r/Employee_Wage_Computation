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
    ans = ''
    if check==0:
        ans = 'Absent'
    else:
        ans='Present'

    return ans


def dailyWage():
    """Description: 
        Function to calculate daily wage of Employee
    Parameters:
        None
    Returns:
        Daily Wage
    """
    wage_per_hour = 20
    work_hour = 8
    return 20*8



def main():
    welcome()
    print(attendance())
    print(f"Daily wage of Employee is {dailyWage()}")

if __name__=="__main__":
    main()