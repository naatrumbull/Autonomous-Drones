weight = float(input("Weight: "))
measurementType = input("(K)g pr (L)bs: ")
if measurementType == "K" or measurementType == "k":
    print("Weight in lbs: " + str(weight * 2.205))
elif measurementType == "L" or measurementType == "l":
    print("Wight in Kg: " + str(weight * .454))
