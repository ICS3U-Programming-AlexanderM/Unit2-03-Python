# Created by: Alexander Matheson
# Created on: Nov 29, 2021
# This program asks the user for the radius of a circle.
# It then calculates and displays the circumference using tau.
import constants


def main():
    # input
    radius = float(input("Enter the radius of the circle (mm): "))

    # process
    circumference = constants.TAU * radius

    # output
    print("")
    print("Circumference = {} mm".format(circumference))


if __name__ == "__main__":
    main()
