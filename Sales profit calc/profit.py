selling  = int(input("Enter the selling price: "))
buying  = int(input("Enter the Buying price: "))

profit = selling - buying 
profit_percentage = (profit/ buying ) * 100

print("The profit is:", profit)
print("The profit percentage is:", profit_percentage, "%")