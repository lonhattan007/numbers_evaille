import math

def sum_of_n(sum, n, start):
    if n < 1:
        print("Invalid input: No of numbers must be at least 1!")
    elif sum < n*(n-1)/2:
        print("Invalid input: sum can't be made from n different numbers!")
    elif n == 1:
        return [[sum]]
    else:
        result = []
        

        for i in range (start, sum-n+1):
            sub_solution_lst = sum_of_n(sum-i, n-1, start+1)
            sub_solution_lst = list(filter(lambda a: len(a) == n-1, sub_solution_lst))

            if len(sub_solution_lst) == 0:
                pass
            else:
                for sub_solution in sub_solution_lst:
                    sub_solution[-1] -= 1
                    sub_solution.insert(0, i)                
                    result.append(sub_solution)
        
        return result    

solution = sum_of_n(10, 2, 1)

print(solution)