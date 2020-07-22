'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    #check if there is any python built in method to check for duplicates
    # check arr for index of numbers and single out the one that only shows up once
    #variable to hold the current number in array
    #current = arr[0]
    #variable to hold the numbers that doesn't repeat

    for n in arr:
        #conditional to check if number is repeated
        current = arr.count(n)
        if current == 1:
            duplicate = n
    return duplicate

    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")