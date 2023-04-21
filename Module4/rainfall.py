# Critical Thinking Module 4

# Variable  Definition
rainfall_sum = 0

# Number of Years Input
years_count = int(input("\nPlease enter the amount of years of rainfall data you'd like to input:\n"))

# Loop For each year
for x in range(1, years_count+1):

    # Loop for each month
    for y in range(1,13):

        # Get new input for rainfall
        month_rainfall = int(input("\nPlease enter year {} month {}'s inches of rainfall:\n".format(x,y)))

        # Add to the sum
        rainfall_sum += month_rainfall


# Calculate average rainfall per month
rainfall_per_month = rainfall_sum / (years_count * 12)

print("\nRESULTS:")
print("Total Number of Months: {} months".format(years_count*12))
print("Total Inches of Rainfall: {} inches".format(rainfall_sum))
print("Average Rainfall per Month: {} inches\n".format(rainfall_per_month))



