# temperature-conversion
# Author: Brscn0

while True:
    tempature_type= int(input("""
    -------------------------------
    1-)Celsius to Fahrenheit   2-)Fahrenheit to Celsius
    3-)Celsius to Kelvin       4-)Kelvin to Celsius
    5-)Fahrenheit to Kelvin    6-)Kelvin to Fahrenheit
                7-)Exit
    -------------------------------
    [*]Select: """))

    if tempature_type == 1:
        while True:
            c = float(input("[*]Please Entet Celsius Degree: "))
            if c < -273.15:
                print("! Value Cannot Be Lower Than -273.15 Celsius !  ")
            else:
                f = (c * 1.8) +32
                print(f,"Fahrenheit")
                break

    if tempature_type == 2:
        while True:
            f = float(input("[*]Please Enter Fahrenheit Degree: "))
            if f < -459.66999999999996:
                print("! Value Cannot Be Lower Than -459.669 Fahrenheit !  ")
            else:
                c = (f-32)/1.8
                print(c,"Celsius")
                break

    if tempature_type == 3:
        while True:
            c = float(input("[*]Please Enter Celsius Deegree: "))
            if c < -273.15:
                print("! Value Cannot Be Lower Than -273.15 Celsius !")
            else:
                k = (c + 273.15)
                print(k,"Kelvin")
                break

    if tempature_type == 4:
        while True:
            k = float(input("[*]Please Enter Kelvin Degree: "))
            if k< 0 :
                print("! Value Cannot Be Lower Than 0 Kelvin ! ")
            else:
                c = (k -273.15)
                print(c,"Celsius")
                break

    if tempature_type == 5:
        while True:
            f = float(input("[*]Please Enter Fahrenheit Degree: "))
            if f < -459.66999999999996:
                print("! Value Cannot Be Lower Than -459.669 Fahrenheit ! ")
            else:
                k = (f + 459.669) * 5/9
                print(k,"Kelvin")
                break

    if tempature_type == 6:
        while True:
            k = float(input("[*]Please Enter Kelvin Degree: "))
            if k < 0:
                print("! Value Cannot Be Lower Than 0 Kelvin ! ")
            else:
                f = 1.8 * (k - 273.15) +32
                print(f,"Fahrenheit")
                break
    
    if tempature_type == 7:
        break