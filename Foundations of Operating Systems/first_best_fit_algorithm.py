
# First fit vs best fit simulation

import time

Free_Memory_Blocks = [10,9,22,4,1,2,5,4,1]
Memory_Needed_For_Tasks = [1,4,5,2,1,3,22,9,10]
Taken_Blocks_First = [0,0,0,0,0,0,0,0,0]
Taken_Blocks_Best = [0,0,0,0,0,0,0,0,0]
Best_Fit_Reference = []

start_time_first_fit = time.perf_counter()
fake_task = 0
#first fit

for i in Memory_Needed_For_Tasks:
    iteration_count = 0
    for j in Free_Memory_Blocks:
        iteration_count += 1
        if j >= i and Taken_Blocks_First[iteration_count-1] != 1:
            Taken_Blocks_First[iteration_count-1] = 1
            for k in range(1000):
                fake_task += k
                fake_task = 0
            break

end_time_first_fit = time.perf_counter()

start_time_best_fit = time.perf_counter()
#best fit
for i in Memory_Needed_For_Tasks:
    iteration_count = 0
    Best_Fit_Reference = []
    for j in Free_Memory_Blocks:
        iteration_count += 1
        if(Taken_Blocks_Best[iteration_count-1] != 1):
            if j-i >= 0:
                Best_Fit_Reference.append(j-i)
            else:
                Best_Fit_Reference.append(100)
        else:
            Best_Fit_Reference.append(100)

    minpos = Best_Fit_Reference.index(min(Best_Fit_Reference))
    Taken_Blocks_Best[minpos] = 1
    for k in range(1000):
        fake_task += k
        fake_task = 0

end_time_best_fit = time.perf_counter()

print("First fit: {}".format(end_time_first_fit-start_time_first_fit))
print("\nBest fit: {}".format(end_time_best_fit-start_time_best_fit))

print("\nFirst Fit Missed Tasks: {}".format(9-sum(Taken_Blocks_First)))
print("\nBest Fit Missed Tasks: {}".format(9-sum(Taken_Blocks_Best)))