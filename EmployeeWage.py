'''

    @Author: Sudhanshu Kumar
    @Date: 01-10-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 04-10-2024
    @Title : Write a Python program to print if Employee is Present, part time or full time and Wage of Employee

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




def main():
    welcome()
    print(attendance())

if __name__=="__main__":
    main()