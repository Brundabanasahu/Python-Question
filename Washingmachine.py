value=int(input())
if value<0:
    print("Invalid input")
elif value==0:
    print("Time Estimated : 0 Minutes")    
elif value<=2000:
    print("Time Estimated : 25 Minutes") 

elif value<=4000:
    print("Time Estimated : 35 Minutes")     

elif  value<=7000:
    print("Time Estimated : 45 Minutes")  

else:
    print("overloaded")           