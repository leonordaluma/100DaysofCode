def prime_checker(number):
    if number != 1 and not number < 1:
       if number % number == 0 and number % 1 == 0:
          print("It's a prime number.")
       else:
        print("It's a composite number.")
    else:
        print("It's not a prime number.")
    
    

n = int(input("Check this number: "))
prime_checker(number = n)