#PROJEC-1 WEIGHT CONVERTER

weight= int(input('WEIGHT : '))
units = input("(L)bs or (K)gs:  ")

if units.upper() == "L":
    converted_weight = weight * 0.45
    print(f' You are { converted_weight } kilos ')
else units.upper() == "K" :
    converted_weight = weight / 0.45
    print(f' You are {converted_weight} lbs ')
