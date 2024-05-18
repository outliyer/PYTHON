'''name=input("Type your name:\t")
print("you su*k " +name)'''
#hallticket templet
hall=" my name is |name| my roll number |roll| and my  center |centr| in hyderabad on the date |date|"
N=input("enter your name  :")
E=input("enter your roll  :")
R=input("enter your center  :")
D=input("entr the date  :")
hall=hall.replace("|name|",N)
hall=hall.replace("|roll|",E)
hall=hall.replace("|centr|",R)
hall=hall.replace("|date|",D)

print(hall)