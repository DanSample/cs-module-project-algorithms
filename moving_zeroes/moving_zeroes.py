'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # takes an arr of ints and moves each NON-ZERO
    ## int to the left side
    # loop over arr
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            if arr[left] != 0:
                left+=1
            if arr[right] == 0:
                right -= 1
    return arr
    # return the altered arr
    # the order does not matter 


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    moving_zeroes(arr)

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")