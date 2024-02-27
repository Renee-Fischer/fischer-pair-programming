#Offsets the mean of a given array to match a given value
import numpy as np

def offset(originalArr, givenMean):
    originalMean = np.mean(originalArr)
    print(originalMean)
    offset = givenMean - originalMean
    print(offset)
    offsetArr = originalArr + offset
    return offsetArr

# I Like how your function is compact and doesn't have a lot to it, which makes it easy to follow. Variable names are descriptive so I can see what each line of code does based on the variable names. It also works! If you wanted, you could maybe add a docstring so something pops up when you run "offset?", or you could add an assert statement at the beginning to make sure only arrays are taken as inputs.

def offset_test(lower, upper, size, val):
    '''Test the offset function using a random array of chosen range and size. Choose value to become new mean and offset the original array.
    Input: lower: float, lower bound of testing array.
           upper: float, uppwer bound of testing array.
           size: int, number of elements in testing array
           val: float: what you want the new mean to be
    Returns: nothing returned, but prints test results'''
    
    test = np.random.randint(lower, upper, size) # generate random array of ints
    print('Generated random array')
          
    mean_old = np.mean(test)
    test_offset = offset(test, val) # offset array to change the mean
    mean_new = np.mean(test_offset)
          
    print('Old mean: ' + str(mean_old)) # print old and updated means
    print('New mean: ' + str(mean_new))
    
    upper_bound = val + abs(1e-6 *val) # create error bounds; abs is used so the error bounds work with negative numbers
    lower_bound = val - abs(1e+6 *val) 
    
    if (mean_new > lower_bound and mean_new < upper_bound): # print test results (is the new mean within the error bounds)
        print('Test successful')
    else:
        print('Test unsuccessful')
        
# test offset function with differently sized and arrays
offset_test(0, 100, 50, 321.8)
offset_test(-10, 10, 23, -5.64)