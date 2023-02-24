"""

Both 169 and 961 are the square of a prime. 169 is the reverse of 961.

We call a number a reversible prime square if:

1.    It is not a palindrome, and
2.    It is the square of a prime, and
3.    Its reverse is also the square of a prime.

169 and 961 are not palindromes, so both are reversible prime squares.

Find the sum of the first 50 reversible prime squares.
"""

"""
map :
- check its prime or not 
    - use is prime function 
- store the prime and reverse it 
    - 
- squart root the reversed number 
    - 
- check if that prime or not(step 1)
- check if store number or reversed number is palindrome or not
- 
"""
## Checking for condition 1 palindrom or not
def is_palindrome(num):
    num1 = is_prime(num)
    sqr1, rsqr = squareRoot(num1)
    if num1 == rsqr:
        return False
    return True

## Checking for condition 2 reversed number is prime or not
def reversedPrime(num):
    return is_prime(num)



## 
def squareRoot(num):
    square = num**2
    reverseSquare = int(str(square)[::-1])
    return square,reverseSquare


## Checking for prime number
def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
            break
    else:
        return True


## reversing number 
def num_reverse(num):
    revers_num = 0
    while num !=0:
        num_digit = num%10
        revers_num = revers_num*10 + num_digit
        num = num//10 
    return revers_num

if __name__ == '__main__':
    num = 13
    print(is_prime(num))