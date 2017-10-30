# carbohydrate.py
# python3
# calculates the molecular weight of carbohydrate


def main():
    print("Program calculates the molecular weight of a carbohydate")
    print("based on the number of hydrogen, carbon & oxygen atoms.")
    hydrogen = int(input("Enter the number of hydrogen atoms: ")) * 1.00794
    carbon = int(input("Enter the number of carbon atoms: ")) * 12.0107
    oxygen = int(input("Enter the number of oxygen atoms: ")) * 15.9994
    molecularWeight = hydrogen + carbon + oxygen

    print("The molecular weight is:", molecularWeight)


main()
