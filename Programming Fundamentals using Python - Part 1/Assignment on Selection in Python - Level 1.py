#lex_auth_012693711503400960120

def find_product(num1,num2,num3):
    product=0
    #write your logic here
    

    if(num3 == 7):
        return -1
    elif(num2 == 7):
        product = num3
        return product
    elif(num1 == 7):
        product = num2 * num3
        return product
    else:
        product = num1 * num2 * num3
        return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(7,6,2)
print(product)