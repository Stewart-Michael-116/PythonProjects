# Ask user for charge
total_before = 0

for i in range(0,4):

    total_before += float(input('\nPlease put the another meal charge for your Restaurant Bill:\n'))

# calculate 7 percent sales tax
total_sales = total_before * 1.07

# add 18% tip
# This adds the tip amount on the post tax amount

total = total_sales * 1.18

# Print Values

print('\nSubtotal: $'.rstrip(), "{:.2f}".format(total_before))
print('Subtotal with Sales Tax: $'.rstrip(), "{:.2f}".format(total_sales))
print('Total with 18% Tip Post Tax: $'.rstrip(), "{:.2f}".format(total), '\n')