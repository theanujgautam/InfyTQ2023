def find_max(num1, num2):
    max_num=-1
    my_list = []
    digit_sum = 0
    # Write your logic here
    for num in range(num1, num2+1):
        if(num % 5 == 0 and num // 10 != 0 and num // 100 == 0 and num1 < num2):
            digit_sum = sum(int(digit) for digit in str(num))
            if (digit_sum % 3 == 0):
                my_list.append(num)
    if(len(my_list) == 0 ):
        return -1
    else:
        max_num = max(my_list)
        return max_num

#Provide different values for num1 and num2 and test your program.

max_num=find_max(30,30)
print(max_num)  