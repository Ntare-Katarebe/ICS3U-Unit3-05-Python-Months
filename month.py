#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program tells you the month
#    with numbers inputted from the user


def main():
    # This function get the month

    # input
    integer = int(input("Enter the number of month: "))
    print("")

    # process/output
    if integer == 1:
        print("January")
    elif integer == 2:
        print("February")
    elif integer == 3:
        print("March")
    elif integer == 4:
        print("April")
    elif integer == 5:
        print("May")
    elif integer == 6:
        print("June")
    elif integer == 7:
        print("July")
    elif integer == 8:
        print("August")
    elif integer == 9:
        print("Setember")
    elif integer == 10:
        print("October")
    elif integer == 11:
        print("November")
    elif integer == 12:
        print("December")
    else:
        print("Not a month")
    print("\nDone.")


if __name__ == "__main__":
    main()
