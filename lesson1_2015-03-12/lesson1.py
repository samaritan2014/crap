name = raw_input("What is your name?")

age = input("What year were you born?")

gender = raw_input("What is your gender?")

print "Hello %s! Nice to meet you!"%(name)


if age == int:
	ageGuess = 2015 - age
else:
	print "Please enter a number for the year Bitch!"

print "I guess you are str(ageGuess) years old."

if gender.lower() == "male":
	print ("So you have a penis! Haha!")
elif gender.lower() == "female":
	print ("Mmmmh...will I ever get to eat your cookie? #justThinking")
else:
	print ("It's ok to be transgender too. After all I'm just a computer with no feelings! :) ")	




