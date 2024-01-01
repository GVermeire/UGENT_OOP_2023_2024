#Invoer
jaar = int(input())

# Berkening + ouput
if jaar % 4 == 0 and (int(jaar/100)*100) % 400 == 0:
    print("schrikkeljaar")
else:
    print("geen schrikkeljaar")


##STef zijn versie
#jaar = float(input())

#if jaar % 4 ==  0 and jaar % 100 != 0:
    print("schrikkeljaar")
#if jaar % 4 == 0 and jaar % 100 == 0 and jaar % 400 == 0:
 #   print("schrikkeljaar")
#if jaar % 4 == 0 and jaar % 100 == 0 and jaar % 400 != 0:
#   print("geen schrikkeljaar")
#if jaar % 4 != 0:
    print("geen schrikkeljaar")