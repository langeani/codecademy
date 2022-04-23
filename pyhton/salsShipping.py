weight = 41.5
#ground_shipping
if weight <= 2:
    ground_shipping = ((weight * 1.5) + 20)
elif weight >= 2:
    ground_shipping = ((weight * 3) + 20)
elif weight >= 6:
    ground_shipping = ((weight * 4) + 20)
else:
    ground_shipping = ((weight *4.75) + 20)
#print ('Ground Shipping Price: ' + str(ground_shipping))

#premium_shipping
premium_shipping = 125
#print('Premium shipping price is: ' + str(premium_shipping))

#drone_shipping
if weight <= 2:
    drone_shipping = (weight * 4.5)
elif weight >= 2:
    drone_shipping = (weight * 9)
elif weight >= 6:
    drone_shipping = (weight * 12)
else:
    drone_shipping = (weigth *14.25)

#print('Drone shipping price is: ' + str(drone_shipping))

if (ground_shipping < premium_shipping) and (ground_shipping < drone_shipping):
    print('Ground shipping is the cheapest price: You will pay: ' + str(ground_shipping) )
elif premium_shipping < ground_shipping and premium_shipping < drone_shipping:
    print(' Premium shipping is the cheapest price: You will pay: ' + str(premium_shipping))
if drone_shipping < ground_shipping and drone_shipping < premium_shipping:
    print(str(drone_shipping) + ' This is the cheapest price')