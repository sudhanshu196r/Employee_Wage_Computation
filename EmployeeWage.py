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