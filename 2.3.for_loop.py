# for i in range(1,10000):
#     print(i)
# a=int(input("enter a number to print its multiplication table: "))
# for i in range(1,11):
#     print(a*i)


# for j in [0,1,2]:
#     print("Meowww")  
    #  or
    
# for j in range(3):
#     print("mew")

#or 

# for _ in range(3):
#     print("mew")



#or 

# print("mew\n"*3,end="")



# s=str(input("enter no :"))
# for i in range (5,0,-1):
#     print(s*i)\
    
    
    
# for char in "leopard":
#     print(char)



# for anime in ['one piece ','naruo','boruto']:
#     print(anime)

# for key in {'A101': 'RAJESH'}:
    # print(key)
    
# lis=['dessert','fruit']
# for i in enumerate(lis):
#     print(i)



n=int(input("enter a no:"))
if n<1:
    print("not prime ")
else:
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            print("not prime")
            break
    else:
          print("prime")