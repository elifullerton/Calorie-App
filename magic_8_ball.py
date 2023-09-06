import random

question = input("Question: ")

random_number = random.randint(1, 9)

# The if/elif/else statement starts here

if random_number==1:
  print("Magic 8 Ball:  Yes, - definitely.")
elif random_number==2:
  print("Magic 8 Ball:  It is decidedly so.")
elif random_number==3:
  print("Magic 8 Ball:  Without a dobut")
elif random_number==4:
  print("Magic 8 Ball:  Reply hazy, try again")
elif random_number==5:
  print("Magic 8 Ball:  Ask again later.")
elif random_number==6:
  print("Magic 8 Ball:  Better not tell you now.")
elif random_number==7:
  print("Magic 8 Ball:  My sources say no.")
elif random_number==8:
  print("Magic 8 Ball:  Outlook not so good.")
else:
  print("Magic 8 Ball:  Very doubtful.")