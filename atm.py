balance = 1000
print("""Welcome to ATM Machine

Here are your transactions types:
1)CHECK BALANCE
2)WITHDRAW
3)DEPOSIT
4)EXIT

""") 

bank = int(input("What type of transaction would you like to make?"))

if (bank==1):
     print("Your balance is", balance)
elif (bank==2):
  withdrawl = float(input("Enter withdrawl amount: "))
  if (balance > withdrawl):
     total = balance - withdrawl
     print("Withdrawl has been successful")
     print("Your balance is now", total)
  else:
     print("Insufficient balance")
elif (bank==3):
   deposits = float(input("Enter deposit amount: "))
   dep= balance + deposits
   print("Deposit has been successful")
   print("Your balance is now", dep)
elif (bank==4):
   exit()
else:
   print("No selected transaction")