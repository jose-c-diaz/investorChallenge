print("House buying app")

print("Please Log In")

#username=input("please enter your username >> ")
#password-input("pleasde enter your password >> ")

counter=int(input("how many houses do you want to insert >> "))

while True:
 if (counter) >= 1: 

    
    housesp=float(input("Please enter the house buying price >> "))
    monthl=int(input("Please submit the amount of months that you have owned the house >> ")) 
    creditCardNumber=int(input("Please enter your credit card number >> "))
    creditCardExpiration=int(input("Please enter your credit card expiration date >> "))
    creditCardSecurity=int(input("Please enter your credit card security code >> "))

    realtyFee=((housesp) * (.06))
    loanFee=(((monthl* .0083) * (housesp)))
    titleFee=((housesp) * .03)
    total=((housesp) + (realtyFee) + (loanFee) + (titleFee))
    print("The sale price is ")
    print (housesp)
    print("The realty fee is")
    print(realtyFee)
    print("The loan fee is ")
    print (loanFee)
    print("The title fee is")
    print (titleFee)
    print("The sales price is")
    print(total)
    counter-=1
else :
    print("Done")
