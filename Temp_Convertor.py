def temprature_convertor(temp,unit):
    '''This function helps to convert the given temperature into Fahrenheit / Celsius '''
    if unit=='C' or unit=='c':
        return temp * 9/5 +32   # to convert to F
    elif unit=='F' or unit=='f':
        return (temp-32)*5/9     #to convert to C
    else:
        return None
temp = int(input("Enter Temprature : "))
unit = str(input("Enter Unit : "))

print("Converted Temp is : ",temprature_convertor(temp,unit))