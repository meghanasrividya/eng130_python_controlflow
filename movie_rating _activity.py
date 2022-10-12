#  age restriction for movie
# create a condition for 18 & above
# 16 & above
# universal
# pg
# 12a
# 15 & above
# if nothing matched inform the user to enter their age again
# max user must not be allowed to enter over 117 years

age=int(input("Please , enter your age:"))

if age >= 18 and age <= 117:
    print("You are allowed to watch all the movies")
elif age >= 16 :
    print("These movies are only for 16 years and above ")
elif age >= 15 :
    print("These movies are only for 15 years and above")
elif age >= 12 :
    print("These movies are only for 12 and above")
elif age > 117:
    print("Please enter the correct age")
else:
    print("please enter only digits")