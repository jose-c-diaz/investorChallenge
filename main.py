print("House buying app")

print("Please Log In")

#username=input("please enter your username >> ")
#password-input("pleasde enter your password >> ")

#counter=int(input("hopw many houses do you want to store? >> "))

#while True 
housesp=int(input("Please enter the house buying price >> "))
monthl=int(input("Please submit the amount of months that you have owned the house >> ")) 

realtyFee=((housesp) * (.06))
loanFee=(((monthl* .0083) * (housesp)))
titleFee=((housesp) * .03)
total=((housesp) + (realtyFee) + (loanFee) + (titleFee))
print("The sale price is ")
print (housesp)
print("Realty fee ")
print(realtyFee)
print("Loan fee ")
print (loanFee)
print("Title fee ")
print (titleFee)
print("Sales price .......")
print(total)