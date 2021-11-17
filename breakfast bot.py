#Breakfast Advice
#Created by Penelope Lowenstein

#Intro
print("Hello! I'm here to help you pick your perfect breakfast!")
print("Please answer the questions to discover what you should eat this morning!")
#Beginning of Top of Tree
ans= input("Do you want something sweet or savory?")
if ans== "sweet":
    ans= input("Do you have a big (big) appetite or a small appetite(small)?")
    if ans=="big":
        ans= input("Do you have a larger budget(large)or smaller budget(small)?")
        if ans== "large":
            print("You should have french toast this morning!")
        else:
            print("You should have donuts from Dunkin this morning!")
    if ans=="small":
        ans=input("Do you have a larger budget(large)or smaller budget(small)?")
        if ans=="large":
            print("You should have yogurt and fresh fruit this morning!")
        else:
            print("You should have cereal at home this morning!")
            
    
    
        
        
    
