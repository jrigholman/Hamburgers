import random
import queue
#Create Order Class
class Order:
    def __init__(self):
        self.randomburger = int(random.randint(1,20))
#Create Person Class
class Person:
    def __init__(self):
        self.customer_name = self.randomname()
    def randomname (Self):
        ascustomers =["Jake","Jon","Ethan","Sky","Jordan","Logan","Stacey","Ponyboy","Liverking"]
        return random.choice(ascustomers)
#Create Customer Class             
class Customer(Person):
    def __init__(self):
        super().__init__ ()
        self.order= Order()
#Create a Queue for the line of orders which is 100
queue= []
Customer_info={}
for i in range(100):
    customer = Customer()
    queue.append(customer)

    # Add customer to the dictionary if not already present
    if customer.customer_name not in Customer_info:
        Customer_info[customer.customer_name] = 0

    # Increment customer's burger count in the dictionary
    Customer_info[customer.customer_name] += customer.order.randomburger
print("Burger Orders")
# Print out each customer and their total burgers ordered sorted by the most number of burgers ordered
for customer_name, burger_count in sorted(Customer_info.items(), key=lambda x: x[1], reverse=True):
    print(" ")
    print("{} ordered {} burgers".format(customer_name,burger_count))