# Receipts for Lovely Loveseats
# First Item 
lovely_loveseat_description = ('Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches widee x 30 inches deep.  Red or white.') 
# First Item Price
lovely_loveseat_price = 254.00 # Dollars
# Second Item
stylish_settee_description = ('Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28  inches deep. Black.')
# Second Item Price
stylish_settee_price = 180.50 # Dollars
# Third Item 
luxurious_lamp_description = ('Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.')
# Third Item Price
luxurious_lamp_price = 52.15 # Dollars
# Sales Tax
sales_tax = .088 # 8.8 percent
# First Customer
customer_one_total = 0 #Dollars
customer_one_itemization = ""
customer_one_total += lovely_loveseat_price # added price of the loveseat
customer_one_itemization += lovely_loveseat_description # added loveseat description
customer_one_total += luxurious_lamp_price # added price of lamp to total
customer_one_itemization += "\n" + luxurious_lamp_description #added lamp description to itemization, "\n" is used to separate the descriptions 
customer_one_tax = customer_one_total * sales_tax # finding total sales tax
customer_one_total += customer_one_tax # adding tax to total price
print('Customer One Items:') # itemization heading
print() #added for asthetics
print(customer_one_itemization) #itemization content
print() # added for asthetics
print('Customer One Total:') # total heading 
print() # added for asthetics
print(customer_one_total) # customers total
