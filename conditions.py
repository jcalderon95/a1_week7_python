print("Rules that govern the state of water")

# let the  user pick a temp, see what happens to water (conditional statements)
# current temp is the temperature varieable (user inputs this)
current_temp = False

while current_temp is False:
    # user input -this changes temp on every iteration
    current_temp = input("Enter a temperature: \n")
    print(current_temp)

    # if it's below 0, obvi it's frozen
    if(int(current_temp) < 0) or (int(current_temp) == 0):
        print("water is a solid. icy!")
        current_temp = False

    # if it's between 0 and 100, it's liquid
    elif (int(current_temp) < 100):
        print("water is a liquid. profit!")  
        current_temp = False

    # if it's above 100, obvi it's a gas    
    elif (int(current_temp) > 100) or (int(current_temp) == 100):
         print("water is a vapor, cuz it's HOT") 
         current_temp = False
