import time
start_time = time.time()
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

    # for n in arr:
    #     #conditional to check if number is repeated
    #     current = arr.count(n)
    #     if current == 1:
    #         duplicate = n
    # return duplicate

    #alternate solution:
    
    s = set() #o(1)

    for x in arr: #O(n)
        if x in s:
            s.remove(x) #O(1)
        else:
            s.add(x) #O(1)
    return list(s)[0] #O(1)
    
    '''
    Space complexiyy: measures how memory-usage scales
    Any data structures that are  passed into a function don't count towards space complexity
    it only caresa about any additional data structures that are initilized during an algorithm's execution
    '''


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    end_time = time.time()
    print(f"The odd-number-out is {single_number(arr)}")
    print (f"runtime: {end_time - start_time} seconds")