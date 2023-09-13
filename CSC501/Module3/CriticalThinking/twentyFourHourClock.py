# Alarm Clock

# Ask the user for time in hours

current_time = int(input("\nWhat is the current time in hours?\n"))

# Ask the user for the number of hours to wait for the alarm

alarm_wait_time = int(input('\nHow long will your alarm be for in hours?\n'))

# Output what time will be on the 24 hour clock when the alarm goes off
answer = (alarm_wait_time + current_time) % 24

print('\nThe time will be {} when the alarm goes off.\n'.format(answer))
