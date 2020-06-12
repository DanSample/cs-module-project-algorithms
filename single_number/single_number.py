from collections import Counter
'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Takes in a non-empty array
    # create a temp dict with Counter, this will count all the
    ## elements and assign them as keys and the values as the 
    ### the amount of times it appears in the arr  
    temp = Counter(arr) 
    # loop through the dict and check to see which value == 1
    for value in temp:
        if temp[value] == 1:
            # return the number
            return value


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    single_number(arr)

    print(f"The odd-number-out is {single_number(arr)}")