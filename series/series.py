

def fibonacci(n):
    """
    this is a fibonacci that take argument to n and 
    the function call it self fibonacci(n-1) + fibonacci(n-2)
       
    """
    if n == 0 :
        return 0
    if n == 1 : 
        return 1   
    else : 
        return fibonacci(n -1) + fibonacci(n-2)



def lucas(n) : 
    """
    this is a lucas that take argument to n n1 n2 
    will give u the nth of lucas number  
       
    """
    first = 2 
    sec = 1
    if n == 0 :
        return first
    if n == 1 : 
        return sec     
    else :   
       return sum_series(n-1,first,sec ) + sum_series(n-2,first,sec )  
       
    

def sum_series(n , first=0 , sec=1):
       """
          return whitch mode number series is 
          fibonacci or lucas mode 
       """     
       if first == 2 and sec == 1 : 
           print(" lucas numbers")
           return lucas(n)
       elif first == 0 and sec == 1 : 
           print("fibonacci numbers")
           return fibonacci(n)     
       else :
            if n == 0 :
               return first
            if n == 1 : 
               return sec 
            else : 
                return sum_series(n-1,first,sec ) + sum_series(n-2,first,sec )   
             
             




