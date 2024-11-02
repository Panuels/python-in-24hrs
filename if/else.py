age = int(input("What's your age? "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor")
    
country = str(input("What is your country of origin? "))
if country == "Kenya" :  #case sensitive when answering on the console
    print("we are country mates! ")
else:
    print("Tell me more about your country? ")
    
drink = input("do you drink alcohol? ")
if drink == "yes":
    print("i have a wine stock.. your welcome to try.")
else:
    print("You should try different soft drink. ")