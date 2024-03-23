def FindFirstOccurance(my_list:int,num:int):
    """This function will be working for printing the first occurrence interger in the list
       function will have one argument of list type with the collection of intergers"""
    
    for i in range (len(my_list)):
        """for loop for iterating over the list"""
        
        if my_list[i] ==num:
            """if condition for checking first occurence of interger from list"""
            return i
    return -1

if __name__ == "__main__":
    
    my_list = [5,3,7,1,9,2,8] # defined list type with intergers
    num = 9
    index = FindFirstOccurance(my_list, num)
    if index != -1:
        print(f"The first occurance of {num} in the list is at index {index}.")
    else:
        print(f"{num} is not in the list.")