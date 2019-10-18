#Part_1 of Frantz Lecesne Assignment_1
message = 'The class starts at 6pm' #Initial string value for message
print(message)
message = 'Class sessions begin Friday'#New changed value for variable message 
print(message)

#Part_2
print("""Richard Feynman once said, "You can know the name of a bird in all the languages of the world, but when you're finished, you'll know absolutely nothing whatever about the bird... So let's look at the bird and see what it's doing — that's what counts." """) 

#Part_3
best = 23
print("I don't believe there can be an argument that " + str(best) + " is not the best number.")

#Part_4
rv = """Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore,
While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door.
'Tis some visitor, I muttered, tapping at my chamber door;
Only this and nothing more."""
num_chars = len(rv) #num_chars is now equal to the total length 

#Part_5
print('How many miles did you travel on your last tank of gas?')
miles = input() #This is the user input for miles anticipated as a float
print('How many gallons of gas did you use?')
gallon = input() #This is the user input for gallon anticipated as a float
print('The MPG of your last trip was ' + str(float(miles) / float(gallon)))
