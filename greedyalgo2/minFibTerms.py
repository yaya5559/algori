#given a number k the task is to find the min number of 
#Fibonaci terms whose sum equal k 

##greedy startegy always take the leargets fib number
# less than k
#the real reason it works : Zeckendorf’s Theorem
# Every + integer can be written uniquely as a sum of non-consecutive
#fibonaci numbers time complexity O(logk)

def minFibTerms(number):
    

    array = [1, 1]


    while array[-1]<=number:
        array.append(array[-1]+array[-2])

    array.pop() # # remove the one that exceeded k
    print(array)

    index = len(array)-1
    result =0
    while number >0:
        
        if (number - array[index]) >=0:
            
            number-=array[index]
            result+=1
        else:
            index= index-1


    return result


print(minFibTerms(7))