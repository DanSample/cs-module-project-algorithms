'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # takes in an integer
    # cookies can be eaten 1, 2, or 3 at a time
    # deal with base case(s):
    ## if n is 0 or negative return 0
    if n <= 0:
        return 0
    ## if there is only 1 cookie return 1
    elif n == 1:
        return 1    
    # deal with case: 2 cookies
    # deal with case: 3 cookies
    # deal with case: 3+ cookies
    # return the number of ways all the cookies can be eaten

    pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
