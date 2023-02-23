def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    
    #Start writing your code here

    #Populate the variables: eligible_loan_amount and bank_emi_expected

    #Use the below given print statements to display the output, in case of success
    #print("Account number:", account_number)
    #print("The customer can avail the amount of Rs.", eligible_loan_amount)
    #print("Eligible EMIs :", bank_emi_expected)
    #print("Requested loan amount:", loan_amount_expected)
    #print("Requested EMI's:",customer_emi_expected)

    #Use the below given print statements to display the output, in case of invalid data.
    #print("Insufficient account balance")
    #print("The customer is not eligible for the loan")
    #print("Invalid account number")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work
    flag = False
    account_number = str(account_number)

    if(account_balance < 100000):
        print("Insufficient account balance")
    elif(len(account_number) != 4):
        print("Invalid account number")
    elif(account_number[0] != '1'):
        print("Invalid account number")
    elif(loan_type not in ['Car', 'House', 'Business']):
        print("Invalid loan type or salary")
    elif(loan_type == 'Car' and salary <= 25000):
        print("Invalid loan type or salary")
    elif(loan_type == 'House' and salary <= 50000):
        print("Invalid loan type or salary")
    elif(loan_type == 'Business' and salary <= 75000):
        print("Invalid loan type or salary")
    else:
        if(loan_type == 'Car'):
            eligible_loan_amount = 500000
            bank_emi_expected = 36
            if(loan_amount_expected <= eligible_loan_amount and customer_emi_expected <= bank_emi_expected):
                flag = True
        
        if(loan_type == 'House'):
            eligible_loan_amount = 6000000
            bank_emi_expected = 60
            if(loan_amount_expected <= eligible_loan_amount and customer_emi_expected <= bank_emi_expected):
                flag = True

        if(loan_type == 'Business'):
            eligible_loan_amount = 7500000
            bank_emi_expected = 84
            if(loan_amount_expected <= eligible_loan_amount and customer_emi_expected <= bank_emi_expected):
                flag = True

        if(flag == True):
            print("Account number:", account_number)
            print("The customer can avail the amount of Rs.", eligible_loan_amount)
            print("Eligible EMIs :", bank_emi_expected)
            print("Requested loan amount:", loan_amount_expected)
            print("Requested EMI's:",customer_emi_expected)
        else:
            print("The customer is not eligible for the loan")


#Test your code for different values and observe the results
calculate_loan(1005,90000,255000,"Business",7600000,80)