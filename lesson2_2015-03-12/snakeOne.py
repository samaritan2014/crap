#This is my second python script
# The objective of this script is to remind myself what the snake can do
# Ok, less talk, more typing

#Declare the variable name which store the value of the users name
name = raw_input("What is your name? ")

# Declare a variable yearOfBirth which stores the year the user was born
yearOfBirth = input("What year were you born in? ")

# This variable stores the value of the users age after calculating based on the users ans
age = (2015-yearOfBirth)

#This variable stores the gender of the user
gender = raw_input("What is your gender? ")

print "Hello %s" %(name)
print "You are "+ str(age)+" years old!"

if gender.lower() == "male":
	print "I guess you have a penis between your legs!"
elif gender.lower() == "female":
	print "Mmmmmh...will I ever taste your cookie? #justWondering "
else:
	print "I don't care about your gender. I'm just a machine after all! :)"

