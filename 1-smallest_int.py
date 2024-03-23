def GetSmallestInterger(my_list:int):
    """The function returns the smallest integer in the list
       Function require an argument as the list of integers from the list"""
    
    # iteration in the list starts from index 0
    smallest = my_list[0]
    
    for number in my_list:
        """for loop for ensure traversal of list by searching for the smallest integer
           in given list"""
        if number < smallest:
            
            smallest = number
            
    return smallest

if __name__ == "__main__":
   
    my_list = [5,3,8,1,9,2] #list of integers to be passed to the function
    
    smallest = GetSmallestInterger(my_list)
    
    print(f"The smallest integer in the list is: {smallest}")
    



    

    
