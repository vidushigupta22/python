
import csv
i = 0

fileName = 'food.csv'



while True:
    print("\n\n----------------------------WELCOME TO VIDUSHI'S FOODS------------------------------\n")
    
    enterName = input('enter your name please :')
    phoneNumber = input('enter your mobile number :')
    if len(phoneNumber) == 10:
        mobileNo = phoneNumber
    else:
        print('\nYour number dosent contain 10 Characters : PLEASE TRY AGAIN\n')
        phoneNumber = input('enter your mobile number :')
        mobileNo = phoneNumber
        
    
    
    print('\n Main Menu\n ')
    print('To order-- Press 1.')
    print('To Order History--Press 2.')
    print('To Exit--Press 0.\n')
    
    mainMenu = int(input('Enter your choice number :'))
    
    if mainMenu == 1:
        i = i+1
        orderNumber = i 
        
        print('\nOur food item list present below\n')
        
        print('3. Chilli panner , Price = 120')
        print('4. Spring roll , price = 40')
        print('5. Manchurian , price = 90')
        print('6. Fried Rice , price = 80')
        print('7. Egg Fried Rice , price = 100')
        print('8. Chilli Mushroom , price = 140\n')
        
        order = int(input('Order Your Choice no. :'))
        qty   = int(input('Enter Quantity :'))
        
        if order ==3:
            food = 'chilli paneer'
            price = 120
            quantity = qty
            
        elif order ==4:
            food = 'spring roll'
            price = 40
            quantity = qty
        
        elif order ==5:
            food = 'manchurian'
            price = 90
            quantity = qty
            
        elif order ==6:
            food = 'fried rice'
            price = 80
            quantity = qty
            
        elif order ==7:
            food = 'egg fried rice'
            price = 100
            quantity = qty
        
        elif order ==8:
            food = 'chilli mushroom'
            price = 140
            quantity = qty
            
        print('\n--------YOUR ORDER RECIEPT--------\n')
        print(f'Customer Name {enterName} and Mobile number is {mobileNo}')
        print(f'\nyour order number is = {orderNumber}')
        print(f'\nyour ordered food is = {food} , Quantity is = {quantity} and price = {price}')
        totalPrice = quantity * price       
        print(f'TOTAL PRICE IS = {totalPrice}')
        
        with open(fileName,'a',newline="") as foodFile:
            foodWriter = csv.writer(foodFile)
            
            #attributeRow = ["customerName", 'customerNumber',"foodName", "foodPrice", "foodQuantity", "totalPrice"]
            orderRow = [enterName,mobileNo,food,price,quantity,totalPrice]
            #foodWriter.writerow(attributeRow)
            foodWriter.writerow(orderRow)
        
    
    elif mainMenu == 2:
        # order history
        pass
    
    else:
        break
        
        
        
            
    
