
def solution():
    result =0
    for i in range(1,100):
        if i % 3 == 0 or i % 5 == 0:
            result += i

    return result   
        

if __name__ == "__main__": 
    print(solution())