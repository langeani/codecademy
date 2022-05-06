#Codecademy's Lens Slice Project. This project's intendi is to consolidate lists manipulations functions.three_cheapest 
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
print(toppings)
print(prices)

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#Find the length of the toppings list and store it in a variable called num_pizzas.
num_pizzas = len(toppings)
print(num_pizzas)

#Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas
print("We sell " + str(num_pizzas) + " diffetent kinds of pizza!")

#Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices.
#pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "muschrooms"]]
#trying to automaticaly merge the to lists
i=0
pizza_and_prices = []
for entry in prices:
    pizza_and_prices.append([prices[i], toppings[i]])
    i = i + 1
print(pizza_and_prices)

#Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending).
pizza_and_prices.sort()
print(pizza_and_prices)

#Store the first element of pizza_and_prices in a variable called cheapest_pizza.
cheappest_pizza = pizza_and_prices[0]
print(cheappest_pizza)

#A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!”
#Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

#It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice.
pizza_and_prices.pop()
print(pizza_and_prices)

#Since there is no longer an "anchovies" pizza, you want to add a new topping called "peppers" to keep your customers excited about new toppings. Here is what your new topping looks like:
#Add the new peppers pizza topping to our list pizza_and_prices. [2,5, "peppers"]
#Make sure to position it relative to the rest of the sorted data in pizza_and_prices, otherwise our data will not be correctly sorted anymore!
pizza_and_prices.insert(4,[2,5, "peppers"])
print(pizza_and_prices)

#Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest.
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)