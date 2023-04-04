num = int(input())    
is_prime = True     
if num > 1:   
    for i in range(2,num//2+1):  
        if num % i == 0: 
            is_prime = False  
            break  
    if is_prime==True: 
        print(str(num) +"-is prime")      
    else:                                 
        print(str(num) +"-is composite") 
else:                                     
    print(str(num) +"-is not prime")     
                