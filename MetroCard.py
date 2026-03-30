card_pin = "1234"
attempts = 3
balance = 0.0
debt = 0.0
daily_limit = 100.0
total_added_today= 0.0
rides_today = 0
total_spent_today = 0.0
total_discounts_today = 0.0
mode = "Normal"
history = []

print("Welcome to MetroCard System")
while atemps > 0:
    user_pin = input("Enter 4-digit PIN:")
    if user_pin == card_pin:
        print("Login successful!")
        break
    else:
        attemps -= 1
        print("Wrong PIN! Attemps left:" , attemps)
        if attemps == 0:
            print("Card blocked.Program stopped.")
            exit()
while True:
    print("\n--- WHAT DO YOU WANT TO DO? ---")
    print("1.Check Balance")
    print("2.Add Money")
    print("3.Ride (Turnstile)")
    print("4.History")
    print("5.Stats")
    print("6.Settings")
    print("0.Exit")

    user_choice = input("Your choice:")
    if user_choice == "1":
        print("Balance:" , balance, "AZN")
        if debt > 0:
            print("Your Debt:", debt, "AZN")
    elif user_choice == "2":
        add_amount = float(input("Enter amount to add:"))
        if add_amount <=0: 
            print("Error: Amount must be positive!")
    elif total_added_today + add_amount > daily_limit:
        print("Error: Daily limit reached!")
    else:
        #check debt first
        if debt > 0:
            if add amount >= debt :
                add_amount -= debt
                print(debt, "AZN debt paid.")
                debt = 0
        else:
            debt -= add_amount
            print("Part of debt paid.Remaining debt:", debt)
            add_amount = 0
    balance += add_amount
    total_added_today += (add_amount if debt == 0 else add_amount)
    history.append (f"Added: +{add_amount} | Balance: {balance}")
    print("Success! New balance:" , balance)
elif choice == "3":
    price = 0.40
    discount = 0.0
if mode == "Student":
    price= 0.20
elif mode == "Pensioner":
    price ==0.15
else : #Normal mode
    rides_today += 1
    if rides_today == 1:
        price = 0.40
    elif 2 <= rides_today <= 4:
        price = 0.36
        discount = 0.04
    else : # 5 or more
        price = 0.30
        disount = 0.10
#CHECk balance for ride
if balance >= price:
    balance -= price
    total_spent_today += price
    total_discounts_today +=discount
    history.append(f"Ride: -{price} | Discount:{discount} | Balance: {balance}")
    print("Pass successful! Price:", price)
elif 0.30 <= balance < 0.40 and mode == "Normal":
    debt += (price - balance)
    balance= 0
    print("Emergency pass used!You have a debt now.")
else:
    print("Not enough money! Ride rejected.")

elif choice == "4":
    n = int(input("HOW MANY LAST TRANSACTIONS?"))
    print("Last transactions:")
    for item in history[-n:] :
        print(item)
elif choice == "5":
    print("---DAILY STATS---")
    print("Total rides:", rides_today)
    print("Total spent:" , total_spent_today , 'AZN')
    print("Total discounts:", total_discount_today, "AZN")
    print("Total added money:", total_added_today, "AZN")
elif choice = "6":
    print("1.CHANGE DAILY LIMIT")
    print("2.Change mode (NORMAL/STUDENT/PENSIONER)")
    set_choice = input("Select setting:")
    if set_choice == "1"
    daily_limit = float(input("Enter new daily limit: "))
    print("Limit updated.")
elif set_choice =="2":
    print("1.Normal\n2. Student\n3. Pensioner")
    m_choice = input("Chose mode:")
    if m_choice =="1" : mode ="Normal"
    elif m_choice =="2" : mode = "Student"
    elif m_choice =="3" : mode = "Prisoners"
    print("Mode changed to:", mode)
elif choice == "0":
    print("System closing.Goodbye!")
    break
else:
    print("Invalid choice!Try again.")




