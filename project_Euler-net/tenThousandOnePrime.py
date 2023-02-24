"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. What is the 10001st prime number?
"""
def find(num):
    for i in range(2,num):
        if (num % i) == 0:
            num = i

    return num


if __name__ == '__main__':
    num=6
    print(find(num))