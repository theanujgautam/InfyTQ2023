

def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    bill_amount = 0
    # write your logic here

    if(quantity_ordered < 1 or distance_in_kms < 1 or food_type == 'v' or food_type == 'n' ):
        return -1
        
    if(food_type == 'N'):
        bill_amount = 150 * quantity_ordered
    elif(food_type == 'V'):
        bill_amount = 120 * quantity_ordered
        
    if(distance_in_kms <= 3):
        pass
        
    elif(distance_in_kms <= 6):
        bill_amount += (distance_in_kms -3)*3
        
    else:
        bill_amount += (9 + (distance_in_kms - 6) * 6)
        
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)

