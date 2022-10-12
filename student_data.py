
# create a dictionary student_data
student_data={"first_name":"Meghana","last_name":"Aenugu","dob":"13/10/1992","course":"DevOps","hobbies":"badminton"}
# iterate through the dict
for i in student_data:
    print(i)
#print all the keys
print(student_data.keys())
# print all the values
print(student_data.values())
# print key with matching value name ="Meghana"
for i in student_data:
 if student_data[i]=="Meghana":
    print(i)