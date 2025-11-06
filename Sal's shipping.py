# First things first, define a weight variable and set it equal to any number.
weight = 4.8 #package weight in lbs
# Next, we need to know how much it costs to ship a package of given weight by normal ground shipping based on the “Ground shipping” table above.
# Write a comment that says “Ground Shipping”.
# Create an if/elif/else statement for the cost of ground shipping. It should check for weight, and print the cost of shipping a package of that weight.

# Ground Shipping 
if weight <= 2: #2 lbs or less
  cost_ground = weight * 1.50 + 20.00 #calculates cost
elif weight <= 6: # over 2 lbs, but less than or equal to 6 lbs
  cost_ground = weight * 3.00 + 20.00 # calculates cost
elif weight <= 10: # over 6 lbs, but less than or equal to 10 lbs
  cost_ground = weight * 4.00 + 20.00 #calculates cost
else: # packages over 10 lbs
  cost_ground = weight * 4.75 + 20.00 # calculates cost
# A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping.
# Test that your ground shipping calculation gets the same value.
print() # leave empty, used for asthetic purposes only
print('Ground Shipping: ' + str(cost_ground)) # calculates the cost of ground shipping and prints it, str() needs to be used to veiw float
# We’ll also need to make sure we include the price of premium ground shipping in our code.
# Create a variable for the cost of premium ground shipping.
cost_ground_premium = 125.00 # this value does not change with package weight
# Print it out for the user just in case they forgot!
print("Ground Shipping Premium $", cost_ground_premium)


# Write a comment for this section of the code, “Drone Shipping”.
# Create an if/elif/else statement for the cost of drone shipping. This statement should check against weight and print the cost of shipping a package of that weight.
# Drone shipping 
if weight <= 2: # 2 lbs or less
  cost_drone = weight * 4.50 + 0.00 # calculates cost
elif weight <= 6: # 6 lbs or less
  cost_drone = weight * 9.00 + 0.00 # calculates cost
elif weight <= 10: # 10 pounds or less
  cost_drone = weight * 12.00 + 0.00 #calculates cost
else: # packages over 10 lbs
  cost_drone = weight * 14.25 + 0.00 #calculates cost
# A package that weighs 1.5 pounds should cost $6.75 to ship by drone.
# Test that your drone shipping calculation gets the same value.
print() # leave empty, used for asthetic purposes only
print('Drone Shipping: ' + str(cost_drone)) # calculates the cost of ground shipping and prints it, str() needs to be used to veiw float

cheapest = min(cost_ground, cost_ground_premium, cost_drone)
if cheapest == cost_ground:
    print('The cheapest option is Ground Shipping at $' + str(cheapest))
elif cheapest == cost_ground_premium:
    print('The cheapest option is Ground Shipping Premium at $' + str(cheapest))
else:
    print('The cheapest option is Drone Shipping at $' + str(cheapest))