def collatz(n):
    #Ending the loop if the number reaches '1'
    if n == 1:
        result = [1]
    #Dividing the number by 2 if it is even
    elif n % 2 == 0:
        result = collatz(n // 2) + [n]

    #Multiplying by 3 and adding 1 to the number if it is odd.
    elif n % 2 == 1:
        result = collatz((3 * n) + 1) + [n]
      
    return result

#Number whose sequence you need to output
collatz(100)
