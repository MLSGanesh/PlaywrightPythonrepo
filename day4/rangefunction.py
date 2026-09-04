# range of number: range(num) (here 0 is the starting point)
# range of starting and stoping points: range(start, stop)
# range of starting point, stoping point and increment/decrement: range(start, stop, inc/dec)

# Example 1: only stoping value
# print(range(10))
# print(list(range(10))) #print(list(range(0,10))) using range without for loop requires list

# Example 2: start and stop values
# print(list(range(5,10))) # 5,6,7,8,9

# Example 3: print even number between 1 to 10
# print(list(range(0,10,2))) # 0,2,4,6,8

# Example 4: print odd number between 1 to 10
# print(list(range(1,10,2))) # 0,2,4,6,8

# Example 5: reverse sequence 10,9,8,7,6.....
# print(list(range(10,0,-1)))

# Example 6:   -10,-9,-8,-7,-6.....
# print(list(range(-10,-5)))

# Example 7:
print(list(range(-10,-5,2)))