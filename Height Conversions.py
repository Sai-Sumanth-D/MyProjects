#PROJECT ON INCHES VS CMS 

height_in_inches = int(input('HEIGHT : '))
units = input('(C)ms or (I)nch ')

if units.upper() == "I" :
    converted =  height_in_inches * 2.54
    print(f'You are { converted  } cms' )

else  :
    output = height_in_inches / 2.54
    print(f' You are { converted } inches')
