# Take the following if/elif/else statement
user_name = "Dave"  
if user_name == "Dave":   
    print("Get off my computer Dave!")   
elif user_name == "angela_catlady_87":   
    print("I know it is you, Dave! Go away!")   
elif user_name == "Travis Paul Pyle":   
    print("Access Granted.")   
else:   
    print("Username not recognized.") 
    
# We can achieve the same thing using a match statement as  shown below
user_name = "Dave"  
match user_name:  
    case "Dave":  
        print("Get off my computer Dave!")  
    case "angela_catlady_87":  
        print("I know it is you, Dave! Go away!")   
    case "Travis Paul Pyle":  
        print("Access Granted.")  
    case default:  
        print("Username not recognized.")  