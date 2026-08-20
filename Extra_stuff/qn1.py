def get_sum_and_product(n):
    n = abs(n)
    
    if n == 0:
        return 0, 0
        
    digit_sum = 0
    digit_prod = 1
    
    while n > 0:
        digit = n % 10
        digit_sum += digit
        digit_prod *= digit
        n //= 10
        
    return digit_sum, digit_prod

n=int(input("Enter number n :"))
print(get_sum_and_product(n))