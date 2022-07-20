import csv

print("\n\n************************** WELCOME TO CANTEEN MANAGEMENT SYSTEM ******************************\n")
canteenFileName = "canteen.csv"

while(True):
    print("------------- Please choose from one of the options shown below -------")
    print("1. Create Order")
    print("2. Show Order History")
    print("0 to exit")

    mainMenuInput = int(input("Please enter your choice: "))

    if(mainMenuInput == 1):
        customerName = input("Enter customer name: ")
        
        print("------------ Choose Items to Order -------------")
        print("1. Chilli Potato - ₹ 50")
        print("2. Spring Roll(2 pcs) - ₹ 40")
        print("3. Manchurian - ₹ 160")
        print("4. Sandwich - ₹ 30")

        orderMenuInput = int(input("Please enter your choice: "))

        if(orderMenuInput == 1):
            foodName = "Chilli Potato"
            foodPrice = 50

        elif(orderMenuInput == 2):
            foodName = "Spring Roll(2 pcs)"
            foodPrice = 40

        elif(orderMenuInput == 3):
            foodName = "Manchurian"
            foodPrice = 160

        elif(orderMenuInput == 4):
            foodName = "Sandwich"
            foodPrice = 30

        foodQuantity = int(input("Enter food quantity: "))

        totalPrice = foodPrice * foodQuantity

        print("\n***************** ORDER RECEIPT ******************\n")
        print("Customer Name: ", customerName)
        print("Items:")
        print(f"{foodName}..........₹ {foodPrice} x {foodQuantity}")
        print(f"Order Total: ₹ {totalPrice}")
        print("\n***************** ORDER COMPLETED ******************\n")

        with open(canteenFileName, "a", newline="") as canteenFile:
            canteenWriter = csv.writer(canteenFile)

            orderRow = [customerName, foodName, foodPrice, foodQuantity, totalPrice]
            canteenWriter.writerow(orderRow)

    elif(mainMenuInput == 2):
        # SHOW ORDER HISTORY
        pass

    else:
        break
