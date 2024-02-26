#Offsets the mean of a given array to match a given value
import numpy as np

def offset(originalArr, givenMean):
    originalMean = np.mean(originalArr)
    print(originalMean)
    offset = givenMean - originalMean
    print(offset)
    offsetArr = originalArr + offset
    return offsetArr


    