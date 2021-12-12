import math

def sum_of_n(sum, n, start):
    """This function find all the combinations of n different number whose sum equals the given number"""
    
    if n < 1:
        raise Exception("Invalid input: No of numbers must be at least 1!")
    elif sum < n*(n-1)/2:
        raise Exception("Invalid input: sum can't be made from n different numbers!")
    elif n == 1:
        return [[sum]]
    else:
        result = []

        for i in range (start, math.ceil(sum/n)):
            sub_solution_lst = sum_of_n(sum-i, n-1, i+1)
            sub_solution_lst = list(filter(lambda a: len(a) == n-1, sub_solution_lst))
            sub_solution_lst = list(filter(lambda a: i not in a, sub_solution_lst))

            if len(sub_solution_lst) == 0:
                pass
            else:
                for sub_solution in sub_solution_lst:
                    sub_solution.insert(0, i)                
                    result.append(sub_solution)
        
        return result    
