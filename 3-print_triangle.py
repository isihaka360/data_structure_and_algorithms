def print_right_triangle(height):
    # print a  right-angled triangle with a given height using(*)
    for i in range(1, height+1):
        print('*' * i)

if __name__ == "__main__":
    height = 5
    print_right_triangle(height)

