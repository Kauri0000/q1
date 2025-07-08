# 1. Create an empty dictionary
# 2. Prompt the user for their name, age, and grade
# 3. Prompt the user for a list for their hobbies
# 4. Use a loop to prompt the user for each hobby until they enter 'done'
# 5. Print the dictionary

student = {}

studentName = input("Enter your name:")
student["Name"] = studentName

print(student)

studentAge = input("Enter your age:")
student["Age"] = studentAge
print(student)

studentGrade = input("Enter your grade:")
student["Grade"] = studentGrade
print(student)

hobbies = []
hobbiesInput = input("Enter your hobbies (type 'done' when finished): ").lower()
while hobbiesInput != 'done':
    hobbies.append(hobbiesInput)
    hobbiesInput = input("Enter another hobby (type 'done' when finished): ").lower()

student["Hobbies"] = hobbies
print("Final student profile:", student)




