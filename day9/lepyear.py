#leapyear
year=int(input("year:"))
if year%400==0:
   print(f"{year}is a leap year!")
elif year%4==0:
     print(f"{year}is a leap year!")
else:
    print("{year} is not a leap year!")