

def fibonacci(n):
    """
    this is a fibonacci that take argument to n and 
    the function call it self fibonacci(n-1) + fibonacci(n-2)
       
    """
    if n < 2 : 
        return n 
    else : 
        return fibonacci(n -1) + fibonacci(n-2)



def lucas(n) : 
    """
    this is a lucas that take argument to n n1 n2 
    will give u the nth of lucas number  
       
    """
    first = 2 
    sec = 1
    if n < 2 :
        return n
    else :    
      for i in range(1, n):
                Lfib = first + sec
                first = sec
                sec = Lfib
      return Lfib
    

def sum_series(n , first=0 , sec=1):
       """
          return whitch mode number series is 
          fibonacci or lucas mode 
       """     
       if first == 2 : 
           print(" lucas numbers")
           return lucas(n)
       elif first == 0 : 
           print("fibonacci numbers")
           return fibonacci(n)     
       else :
             first1 = first
             sec1 = sec
             for i in range(1, n):
                 Lfib = first1 + sec1
                 first1 = sec1
                 sec1 = Lfib
             return Lfib




