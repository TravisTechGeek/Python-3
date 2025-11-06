data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)
# Click Run to print out the list.
# It looks like we have an overlap with our computer science curriculum for the topic of "Python 3".
# Let’s remove the topic from the list of data_science_topics using our newly learned .pop() method.
# Print data_science_topics to see your result.

# Checkpoint 2
data_science_topics.pop()
print(data_science_topics)
# Looks like there is overlap on the "Algorithms" topic as well. Let’s use .pop() to remove it as well.
#Print data_science_topics to see the changes.
# Checkpoint 3
data_science_topics.pop(3)
print(data_science_topics)



