"""29) Write a Python function to get the largest number, smallest num 
and sum of all from a list."""

def largest_smallest_sum(list):


    largest = max(list)
    smallest = min(list)
    total_sum = sum(list)

    print("Largest number:", largest)
    print("Smallest number:", smallest)
    print("Sum of all numbers:", total_sum)

    return largest, smallest, total_sum

result = largest_smallest_sum([3, 1, 4, 1, 5, 9])

