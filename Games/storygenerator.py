from random import randint as ran
#user inputs
print("Welcome! This is a story generator!\n")
name, pronoun, profession, action, hometown, building =\
    input("Enter your character's name."),\
    input("Choose a pronoun."),\
    input("A profession."),\
    input("And an action as well, in past tense."),\
    input("Name the hometown of our character."),\
    input("Finally, a building or structure.")


#dictionary for choices
choices={'c1':["genius","dastardly","amazing","evil"],
         'c2':["loved","ignored","killed","paid"],
         'c3':["cruel","astounding","shameless","thoughtful"],
         'c4':["the school","the office","the town square","the riverside"],
         'c5':["tender","flavourful","mouth-watering","constipation-causing"],}


print(f"Presenting a story of your creation!\n \n \
    {name} was a {choices['c1'][ran(0,3)]} {profession}. \
Really, {pronoun} was {choices['c2'][ran(0,3)]} by all of {hometown}. \
One day, {pronoun} did something {choices['c3'][ran(0,3)]}, that would never be forgotten. \
{pronoun} {action} at {choices['c4'][ran(0,3)]}, and it was so \
{choices['c5'][ran(0,3)]}, that the people of {hometown} \
built a {building} in {name}'s name.")

input("Press enter to exit.")
