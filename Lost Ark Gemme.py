# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 16:30:31 2022

@author: Hokli
"""

from random import *
from statistics import *

# Loop over a single iteration
for iteration in range(1):
    # Set the probability limit
    probability_limit = 25 + (10 * iteration)
    # Initialize empty lists to store the values and absolute values of the differences between successes on lines 1 and 2 and successes on line 3
    value_list = []
    value_abs_list = []
    # Loop over 10 sets of simulations
    for set in range(10):   
        # Loop over 100,000 simulations
        for sim in range(100000):
            # Initialize counters for successes and attempts on each line
            successes_1 = 0
            attempts_1 = 0
            successes_2 = 0
            attempts_2 = 0
            successes_3 = 0
            attempts_3 = 0
            # Set the initial probability
            probability = 75
            # Set the maximum number of attempts on each line
            max_attempts = 4
            
            # Loop over 12 steps in the game
            for step in range(12):
                # If the probability is above the limit and there are still attempts remaining on either line 1 or 2, or all attempts on line 3 have been used up
                if (probability >= probability_limit and (attempts_1 < max_attempts or attempts_2 < max_attempts)) or attempts_3 == max_attempts:
                    # If there are still attempts remaining on line 1
                    if attempts_1 < max_attempts:
                        # Generate a random number between 0 and 100
                        try_forge = randint(0,100)
                        # If the random number is less than or equal to the current probability, increment the number of successes and attempts on line 1 and adjust the probability
                        if try_forge <= probability:
                            probability -= 10
                            successes_1 += 1
                            attempts_1 += 1
                            # Clamp the probability at a minimum value of 25
                            if probability < 25:
                                probability = 25
                        # If the random number is greater than the current probability, increment the number of attempts on line 1 and adjust the probability
                        else:
                            probability += 10
                            attempts_1 += 1
                            # Clamp the probability at a maximum value of 75
                            if probability > 75:
                                probability = 75
                        
                    # If there are still attempts remaining on line 2
                    elif attempts_2 < max_attempts:
                        # Generate a random number between 0 and 100
                        try_forge = randint(0,100)
                        # If the random number is less than or equal to the current probability, increment the number of successes and attempts on line 2 and adjust the probability
                        if try_forge <= probability:
                            probability -= 10
                            successes_2 += 1
                            attempts_2 += 1
                            # Clamp the probability at a minimum value of 25
                            if probability < 25:
                                                                probability = 25
                        # If the random number is greater than the current probability, increment the number of attempts on line 2 and adjust the probability
                        else:
                            probability += 10
                            attempts_2 += 1
                            # Clamp the probability at a maximum value of 75
                            if probability > 75:
                                probability = 75
                        
                        
                # If there are still attempts remaining on line 3
                elif attempts_3 < max_attempts:
                    # Generate a random number between 0 and 100
                    try_forge = randint(0,100)
                    # If the random number is greater than or equal to the current probability, increment the number of successes and attempts on line 3 and adjust the probability
                    if try_forge >= probability:
                        probability -= 10
                        successes_3 += 1
                        attempts_3 += 1
                        # Clamp the probability at a minimum value of 25
                        if probability < 25:
                            probability = 25
                    # If the random number is less than the current probability, increment the number of attempts on line 3 and adjust the probability
                    else:
                        probability += 10
                        attempts_3 += 1
                        # Clamp the probability at a maximum value of 75
                        if probability > 75:
                            probability = 75
                        
                    
            
            # Calculate the value as the difference between the successes on lines 1 and 2 and the successes on line 3
            value = (successes_1 + successes_2) - successes_3
            # Calculate the absolute value as the total successes on lines 1 and 2
            value_abs = successes_1 + successes_2
            
            # Add the value and absolute value to the respective lists
            value_list.append(value)
            value_abs_list.append(value_abs)
            # Reset the value to 0
            value = 0

    
    # Calculate the overall mean value and standard deviation of the values in the value list
    overall_value = mean(value_list) 
    value_deviation = stdev(value_list)
    # Calculate the overall mean absolute value and standard deviation of the values in the absolute value list
    overall_value_abs = mean(value_abs_list) 
    value_abs_deviation = stdev(value_abs_list)
    # Print the overall value, value range, overall absolute value, and absolute value range
    print("Value:")
    print(overall_value) 
    print("Expected Range:")
    print(str(overall_value - value_deviation) + " ~~~~ " + str(overall_value + value_deviation) )
    print("Expected Absolute Range:")
    print(str(overall_value_abs - value_abs_deviation) + " ~~~~ " + str(overall_value_abs + value_abs_deviation) )
    print("Probability:")
    print(probability_limit)
    print("----------------")
    #import seaborn as sns
    #test = sns.distplot(value_list)



   


        
    
    





    
