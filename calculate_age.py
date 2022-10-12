# calculate their age -year of birth etc
import datetime
birthyear =int(input("Enter your Birthyear"))
age=datetime.datetime.now().year-birthyear
print(f"your current age is {age}")



