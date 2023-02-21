
def summer(n,x):
    if n == 0 :
        return n
    if n == 1 and x == 0:
        return 1
    if n == 0 and x == 0:
        return 0
    else:
        # return n**x
        res = n**x
        su = 0
        while(res!=0):
            su += res%10
            res = res//10
        
        return su
            
# assum that input only a power to the 2         
def solution(power):
    num = 2**power 
    string_num = str(num)
    list_num = list(string_num)
    sum_of_num = 0
    for i in list_num:
        sum_of_num += int(i)
    
    return sum_of_num


if __name__ == "__main__":
    print(summer(2,15))
    print(solution(15))