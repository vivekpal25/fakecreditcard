print('''                       ooooo      .oo  o   o .oPYo.   .oPYo.  .oPYo. .oPYo. ooo.                             
  8     8     8        8         .P 8  8  .P 8.       8    8  8   `8 8.     8  `8.     8     8     8     8   
.8P8. .8P8. .8P8.     o8oo      .P  8 o8ob'  `boo     8      o8YooP' `boo   8   `8   .8P8. .8P8. .8P8. .8P8. 
`Y8   `Y8   `Y8        8       oPooo8  8  `b .P       8       8   `b .P     8    8   `Y8   `Y8   `Y8   `Y8   
  8Y.   8Y.   8Y.      8      .P    8  8   8 8        8    8  8    8 8      8   .P     8Y.   8Y.   8Y.   8Y. 
`Yoo' `Yoo' `Yoo'      8     .P     8  8   8 `YooP'   `YooP'  8    8 `YooP' 8ooo'    `Yoo' `Yoo' `Yoo' `Yoo' 
:.8 .::.8 .::.8 .::::::..::::..:::::..:..::..:.....::::.....::..:::..:.....:.....:::::.8 .::.8 .::.8 .::.8 .:
::...:::...:::...::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::...:::...:::...:::...:
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::''')

print('''𝖇𝖞 - 𝖛𝖎𝖛𝖊𝖐𝖕𝖆𝖑շՏյօ 𝖆𝖓𝖉 𝖁𝖔𝖗𝖙𝖊𝖝𝖍𝖆𝖈𝖐


𝕱𝖔𝖑𝖑𝖔𝖜 𝖔𝖚𝖗 𝖞𝖔𝖚𝖙𝖚𝖇𝖊 𝖈𝖍𝖆𝖓𝖓𝖊𝖑 -- 𝕳𝖆𝖘𝖍𝕮𝖗𝖞𝖕𝖙𝖎𝖓𝖌

𝕬𝖑𝖘𝖔 𝖛𝖎𝖘𝖎𝖙 𝖔𝖚𝖙 𝖇𝖑𝖔𝖌  𝖍𝖙𝖙𝖕𝖘://𝖛𝖎𝖛𝖊𝖐𝖕𝖆𝖑շՏյօ.𝖇𝖑𝖔𝖌𝖘𝖕𝖔𝖙.𝖈𝖔𝖒''')


#Coding Part #
#-----------------------------------------------------
print("Choose Your Credit Card")
credlist=["MasterCard","Visa"]
print(credlist)
                #choosing type of credit card

print('')
choose=int(input("Enter number --> "))
print('')
if choose==1:
 print("You choosed MasterCard")
elif choose==2:
 print("You choosed Visa")
else:
	print('exit')
	exit()
                  #exit for wrong choice 

print('')
print("Select One Bank")
banklist=["Axis Bank Limited ","CitiBank ","Canara Bank ","Oriental Bank Of Commerce ","Yes Bank "]
print(banklist)

print('')
choosee=input("Enter number --> ")


print('')
print("!!!CHOOSE ANY CARD NUMBER FROM BELOW TWO CARDS IF ONE WILL NOT WORK THEN OTHER WILL!!!")
import random
card=random.choice(range(51,55))
cardmid=random.choice(range(1254739,9874536))
cardlast=random.choice(range(1002301,2004501))
zone=str(card)
zoon=str(cardmid)
zono=str(cardlast)
zbno=zone+zoon+zono
print('')
print("Your MasterCard Number --> "+ zbno)
#Generating card number
import random
vcard=4
vcardmid=random.choice(range(1254739,9874536)) 
vcardlast=random.choice(range(10020350,20340450))
vzone=str(vcard) 
vzonee=str(vcardmid)
vzoneee=str(vcardlast)
vzoneeee=vzone+vzonee+vzoneee
print('')
print("Your Visa Card Number --> "+ vzoneeee)
#generating cvv
cvv=random.choice(range(100,578))
cvvv=str(cvv)
print('')
print("Your CVV/CVV2 --> "+ cvvv)

#expiry date of card
exmon=random.choice(range(1,12))
exyear=random.choice(range(2022,2024))
exm=str(exmon)
exy=str(exyear)
print('')
print("Expiry (MM/YYYY) --> "+ exm+'/'+exy)

#Done coding 
#Credit goes to vivekpal2510 modified by Vortexhack
