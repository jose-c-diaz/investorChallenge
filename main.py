print("House buying app")

print("Please Log In")

#username=input("Please enter your username >> ")
#password-input("Please enter your password >> ")

#counter=int(input("How many houses do you want to store? >> "))

#while True 
housesp=int(input("Please enter the house buying price >> "))
monthl=int(input("Please submit the amount of months that you have owned the house >> ")) 

realtyFee=((housesp) * (.06))
loanFee=(((monthl* .0083) * (housesp)))
titleFee=((housesp) * .03)
total=((housesp) + (realtyFee) + (loanFee) + (titleFee))
print("The sale price is", housesp)
print("The realty fee is", realtyFee)
print("The loan fee is", loanFee)
print("The title fee is", titleFee)
print("The sales price is", total)
