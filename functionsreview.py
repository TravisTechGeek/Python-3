# Alright, this is it. We are going to use all of our knowledge of functions to build out TripPlanner V1.0.
# First, like in our previous exercises, we want to make sure to welcome our users to the application.
# Create a function called trip_planner_welcome() that takes one parameter called name. The function should use print() to output a message like this:

def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0" + name)
trip_planner_welcome(", Travis ")

def estimated_time_rounded(estimated_time):
# Next, we are going to define a function called estimated_time_rounded() that will allow us to calculate a rounded time value based on a decimal for our user’s trip.
# Define the function estimated_time_rounded() with a single parameter estimated_time. The function should do two things:

# Create a variable called rounded_time that is the result of calling the round() built-in function on the parameter estimated_time.
# Return rounded_time.
  rounded_time = round(estimated_time)
  return rounded_time
estimate = estimated_time_rounded(2.43)
# Next, we are going to generate messages for a user’s planned trip
# Create a function called destination_setup() that will have four parameters in this exact order: origin, destination, estimated_time, mode_of_transport
# Give the parameter mode_of_transport a default value of "Car". The program will error out if we run it since we have not defined a function body yet. Don’t worry we will do that in the next step.
def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")
destination_setup("Thailand", "Japan", estimate, "car")