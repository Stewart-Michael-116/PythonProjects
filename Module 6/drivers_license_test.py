# Driver's License Test
right_answers_list = []
student_answers_list = []
incorrect_answers = []
incorrect_counter = 0

# Read each of the files into the two empty lists
with open('answers.txt', 'r') as student_answers_file:
    [student_answers_list.append(line.strip()) for line in student_answers_file.readlines()]

with open('right_answers.txt', 'r') as right_answers_file:
    [right_answers_list.append(line.strip()) for line in right_answers_file.readlines()]


# compare each element of the list and add the incorrect answer.
for i in range(len(right_answers_list)):
    if right_answers_list[i] != student_answers_list[i]:
        incorrect_counter += 1
        incorrect_answers.append(i+1)

# Find test score as percentage
test_score = (1-incorrect_counter/20)*100

# Print results based on the test score
print('\nThe Student\'s test resulting in a {}/20. This is a {}%\n'.format((20-incorrect_counter),test_score))

print('\n{} Incorrect Answers:'.format(incorrect_counter), incorrect_answers,'\n')

if(test_score >= 75):
    print("\nStudent has passed.\n")
else:
    print("\nStudent did not pass.\n")

# Debug print statements
#print(student_answers_list)
#print(right_answers_list)