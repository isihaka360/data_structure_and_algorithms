def PrintRightTriangle(height:int):
    assert height != 0
    """FindFirstOccurance as function will return triangled patterns
       The function accepts parameter as height parameter
       once it's called must be called with an argument value"""
    
    for i in range(1, height+1):
        """for loop for iteration """
        print('*' * i)

if __name__ == "__main__":
    height = 5
    PrintRightTriangle(height)

