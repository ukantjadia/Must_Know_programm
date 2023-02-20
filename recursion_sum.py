def sum(num):
    if num <= 1:
        return num 
    else:
        return num + sum(num-1)

def sum_new(num1):
    return num1 if num1 <= 1 else num1 + sum_new(num1-1)

def fact(number):
    return 1 if number <= 1 else number*fact(number-1)

# Count the number of elements in a nested list using recurison 
def count(lst):
    ele=0
    for item in lst:
        if isinstance(item, list):
            ele += count(item)
        else:
            ele += 1
            
    return ele
    

# driver code
def main():
    print(fact(4))
    print(sum(5))
    # print(count([1,1,1,1,1[1,1,[1,1,1],2,3],4,4,5,4,3,[3,3,3],3]))
    print(count(['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']))

if __name__ == "__main__": main()