'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # takes an arr of ints and moves each NON-ZERO
    ## int to the left side
    # init 2 variables 1 at the start and 1 at the end
    left = 0
    right = len(arr) - 1
    # while the left is left of right
    while left <= right:
        #if the left is 0 and the right is not 0
        if arr[left] == 0 and arr[right] != 0:
            #swap
            arr[left], arr[right] = arr[right], arr[left]
        else:
            # if left not 0, increment left
            if arr[left] != 0:
                left+=1
            # if right is 0, decrement right
            if arr[right] == 0:
                right -= 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    moving_zeroes(arr)

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")