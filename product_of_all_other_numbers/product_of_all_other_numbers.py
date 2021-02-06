import time
start_time = time.time()
'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Numbers returned are the product of all numbers in array except the number at that index
    #check if there is one built in function to multiply all elements in array
    #loop through array to acces each number
    #variable to hold the current index
    
    final_array = []
    for index, number in enumerate(arr): #O(n)
        product = 1
        for index2, number2 in enumerate(arr): #O(n)
            if not index2 == index:
                product = product * arr[index2]
        final_array.append(product)

    return final_array


    # modified_arr = [1]*len(arr)
    # #total of first index myltiplied by the rest of numbers
    # total = 1
    # current = arr[0]
    # temp_left = 1
    # temp_right = 1
    # if len(arr) > 0:
        # for n in arr:
        #     print("original arr:", n)
        #     #multiply all elements
        #     total = total * n
        #     current = current + 1
        #     print("current", current)
        # modified_arr.append(total)
        # print("new array", modified_arr)

        # for i in range(len(arr)-1):
        #     temp_left *= arr[i]
        #     print(temp_left)
        #     temp_right *= arr[-(i*1)]
        #     print("right: ", temp_right)
        #     modified_arr[i+1] * temp_left
        #     print("array")
        #     modified_arr[-(i+2)] *= temp_right
        # return modified_arr
       


    #access the array to get values from left of the current index and the values of the product of the right numbers.
       


    # product = [1]*len(arr)
    # product[0] = 1 
    # for i in range(1, len(arr)):
    #     #access the array's index and assign the product of the left numbers
    #     product[i] = product[i-1] * arr[i-1]
    #     print("first loop: ", product[i])
    # #Now, check the right side 
    # right_product = 1
    # #loop should go through the array
    # for i in range(len(arr)-1, -1, -1):
    #     product[i] = product[i] * right_product
    #     print("second loop: ", product[1], right_product)
    #     #combine right and left
    #     right_product *= product[i]
    # return product      

    # return modified_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    #arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
    end_time = time.time()
    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
    print (f"runtime: {end_time - start_time} seconds")