# Career Suggestion System
# Simple Python Program
print("Career Suggestion System")
# User details
name = input("Enter your name: ")
percentage = float(input("Enter your percentage: "))
# Taking input
coding = input("Do you like coding? (yes/no): ")
maths = input("Do you like mathematics? (yes/no): ")
data = input("Do you enjoy working with data? (yes/no): ")
design = input("Do you like designing websites? (yes/no): ")
writing = input("Do you enjoy writing? (yes/no): ")
# Displaying
print("\nHello", name)
print("Based on your answers, your suggested career is:\n")
# Checking conditions
if coding == "yes" and maths == "yes" and percentage >= 75:
    print("Software Developer")
elif coding == "yes" and data == "yes":
    print("Data Analyst")
elif design == "yes":
    print("Web Designer")
elif writing == "yes":
    print("Content Writer")
elif maths == "yes" and percentage >= 75:
    print("Accountant")
else:
    print("Explore Different Career Options")
# Ending statement
print("\nThank you for using the Career Suggestion System!")
