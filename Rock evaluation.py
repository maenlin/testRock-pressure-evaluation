 #Rock grade evaluation
 
from math import pow
from math import sqrt
from math import log
from numpy import array


p=input('Please input the rock pressure (kPa):       ', )
r=input('Please input the rock unit weight (kN/m^3):       ', )
B=input('Please input the tunnel width (m):       ', )
p=float(p)
r=float(r)
B=float(B)

a=input('choice of formula (5,6,7,8,9)：   ', )
a=int(a)

if B<5:
    W=1+0.2*(B-5)
else:
    W=1+0.1*(B-5)

print ("\n\n\n")     



if a==5:
    print ('formula (5)')
    print ('————————————————————————————————————')

    d=1
    k=0
    x0=3
    list1=(0,3)
    list1=list(list1)

    while abs(d)>=0.00005:
        x=1+log(p/sqrt(1+0.01*pow(2,2*x0-6))/0.45/r/W)/log(2)  
        list1.append(x)
        d=x-x0                 
        print ("x=",x)     # Output the result of each interation 
        x0=x                     # Replace x0 with x, preparing for the next time 
        k=k+1
    
    print ("\n")          
    print ("Result")
    print ("——————————————————————————————")

    
    print ("The surrounding rock grade is",x)   # Output the final result
    print ("The interation times is",k)  # Output the interation times
    print (list1)
    print ("\n\n\n\n\n\n")    





if a==6:
    print ('formula (6)')
    print ('————————————————————————————————————')

    d=1
    k=0
    x0=3
    list1=(0,3)
    list1=list(list1)
    
    while abs(d)>=0.1:
        x=(log(p*p/((0.45*pow(2,x0-1)*r*W)*(0.45*pow(2,x0-1)*r*W))-0.01*pow(2,4*x0-8))/log(2)+2)/2   
        list1.append(x)
        d=x-x0              
        print ("x=",x)           # Output the result of each interation 
        x0=x                     # Replace x0 with x, preparing for the next time 
        k=k+1
    
    print ("\n\n")      
    print ("Result")
    print ("——————————————————————————————")

  
    print ("The surrounding rock grade is",x)   # Output the final result
    print ("The interation times is",k)  # Output the interation times 

    print ("\n\n\n")     





if a==7:
    print ('formula (7)')
    print ('————————————————————————————————————')

    d=1
    k=0
    x0=3

    while abs(d)>=0.1:
        x=(log((p*p/((0.45*pow(2,x0-1)*r*W)*(0.45*pow(2,x0-1)*r*W))-pow(2,2*x0-2))*100)/log(2)+8)/4   
        d=x-x0              
        print ("x=",x)           # Output the result of each interation 
        x0=x                     # Replace x0 with x, preparing for the next time 
        k=k+1
    
    print ("\n\n\n")      
    print ("Result")
    print ("——————————————————————————————")

  
    print ("The surrounding rock grade is",x)   # Output the final result
    print ("The interation times is",k)  # Output the interation times 

    print ("\n\n\n")      




if a==8:

    print ('formula (8)')
    print ('————————————————————————————————————')


    d=1
    k=0
    x0=3

    while abs(d)>=0.1:
        x=(log((p**2/((0.45*pow(2,x0-1)*r*W)*(0.45*pow(2,x0-1)*r*W))-1)*100)/log(2)+6)/2    
        d=x-x0              
        print ("x=",x)           # Output the result of each interation 
        x0=x                     # Replace x0 with x, preparing for the next time 
        k=k+1
    
    print ("\n\n")      
    print ("Result")
    print ("——————————————————————————————")
    print ("The surrounding rock grade is",x)   # Output the final result
    print ("The interation times is",k)  # Output the interation times
    print ("\n\n\n")    






if a==9:
    print ('formula (9)')
    print ('————————————————————————————————————')
    d=1
    k=0
    x0=3

    while abs(d)>=0.1:
        x=((0.45*pow(2,x0-1)*r*W)*(0.45*pow(2,x0-1)*r*W))*(1+0.01*pow(2,2*x0-6))+x0-p*p   
        d=x-x0              
        print ("x=",x)           # Output the result of each interation 
        x0=x                     # Replace x0 with x, preparing for the next time 
        k=k+1
    
    print ("\n\n\n")    
    print ("Result")
    print ("——————————————————————————————")

    print ("The surrounding rock grade is",x)   # Output the final result
    print ("The interation times is",k)  # Output the interation times 



