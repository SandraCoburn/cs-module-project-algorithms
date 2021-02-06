'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # check the array for zeroes
    #if the number is not zero move it to the left
    #returned an altered array
    #create a variable to hold current value and an array for arranged list
    current = 0
    new_arr = []
    for n in arr:
        #check that number is not zero and not float
        if isinstance(n, int) and n != 0:
            current = n
            new_arr.insert(0, current)
            current = current + 1
            print("current", current)
        #move zeroes to the end of array
        else:
            new_arr.append(n)
            
            print("zeroes",n)
    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")