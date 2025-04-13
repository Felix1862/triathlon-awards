# **************Compulsory Task 1**************
# Create a new Python file in this folder called award.py.
# ● Design a program that determines the award a person competing in a
# triathlon will receive.
# ● Your program should read in the times (in minutes) for all three events of a
# triathlon, namely swimming, cycling, and running, and then calculate and
# display the total time taken to complete the triathlon.
# ● The award a participant receives is based on the total time taken to
# complete the triathlon. The qualifying time for awards is 100 minutes.
# Display the award that the participant will receive based on the following
# criteria:
# -------------------------------------------------|------------------------------------
# |    Total Time                                  |       Award                       |
# -------------------------------------------------|------------------------------------
# |Within qualifying time                          |    Provincial Colours             |
# -------------------------------------------------|------------------------------------
# |Within 5 minutes of qualifying time             |    Provincial Half Colours        |
# -------------------------------------------------|------------------------------------
# |Within 10 minutes of qualifying time            |    Provincial Scroll              |
# -------------------------------------------------|------------------------------------
# |More than 10 minutes off from qualifying time   |    No award                       |
# -------------------------------------------------|------------------------------------

triathlon_qualifying_time = 100
# provincial_half_colours = 5 minutes within the qualifying time more than 100 minutes less than 105 minutes
# provincial_scroll = 10 minutes within the qualifying time more than 105 minutes less than 110
# no_award = more than 10 minutes within the qualifying time

# Indicate the time in minutes
# Ask the user for times.
swimming_event = int(input("Please input swimming event times in minutes here: \n"))
print("{} minutes in the swimming event.".format(swimming_event))
cycling_event = int(input("Please input cycling event times in minutes here: \n"))
print("{} minutes in the cycling event.".format(cycling_event))
running_event = int(input("Please input running event times in minutes here: \n"))
print("{} minutes in the running event.".format(running_event))

# Set qualifying time
# Calculate total time.
triathlon_qualifying_time = 100
triathlon_athlete_time = int(swimming_event + cycling_event + running_event)
print("Total time, {} minutes to complete the triathlon event.".format(triathlon_athlete_time))

PROVINCIAL_COLOURS = 100
HALF_COLOURS = 105
SCROLL = 110

# Award given based on qualifying time
# Determine thresholds
if triathlon_athlete_time <= PROVINCIAL_COLOURS:
    print("You are within the qualifying time and awarded the Provincial Colours.")
elif triathlon_athlete_time <= HALF_COLOURS:
    print("You are awarded the Provincial Half Colours.")
elif triathlon_athlete_time <= SCROLL:
    print("You are awarded the Provincial Scroll.")
else:
    print("Unfortunately you have not qualified, No Award will be given.")