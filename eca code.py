import math
import csv

def huntington_hill_apportionment(total_reps, input_file, output_file):
    
    try:
        with open(input_file, 'r') as file:
            state_data = [line.strip().split(',') for line in file]
    except FileNotFoundError:
        return

    states = [row[0] for row in state_data]
    populations = [int(row[1]) for row in state_data]

    # start each state with 1 rep
    reps = [1] * len(states)
    priorities = [pop / math.sqrt(2) for pop in populations]

    # main apportionment
    for _ in range(total_reps - len(states)):
        
        # find highest priority state
        max_index = priorities.index(max(priorities))
        reps[max_index] += 1

        # update priority value
        reps_current = reps[max_index]
        priorities[max_index] = populations[max_index] / math.sqrt(reps_current * (reps_current + 1))

    # write output
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for state, rep in zip(states, reps):
            writer.writerow([state, rep])

# ask for # of reps
total_reps = int(input("Enter the number of representatives to apportion: "))

huntington_hill_apportionment(
    total_reps=total_reps,
    input_file="state_populations.csv",
    output_file="apportioned_representatives.csv"
)