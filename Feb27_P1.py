"""
Objects => That will manage workflow 
                            |=> State Changes,
                            |=> Validates

* Zamoto/Swiggy:- 
    Problem Statement:- 
    => food deleviry tracking System.
    => Order Class
    => Stores order ID, Restuarant name,delivery status
    => Status progression: placed -> confirmed -> out for deliver -> delivred
    => prevents States from going backward/skip steps
    => Display full order Summary


"""
# Food Delivery Tracking System

class Order:
    # delivery status steps
    status_flow = ["Placed", "Confirmed", "Out for Delivery", "Delivered"]

    def __init__(self, order_id, restaurant):
        self.order_id = order_id
        self.restaurant = restaurant
        self.current_step = 0  # Start at "Placed"

    def update_status(self):
        # block updates after delivery
        if self.current_step == len(self.status_flow) - 1:
            print("Order already delivered")
            return

        self.current_step += 1
        print("Status:", self.status_flow[self.current_step])

    def show_summary(self):
        print("Order ID:", self.order_id)
        print("Restaurant:", self.restaurant)
        print("Status:", self.status_flow[self.current_step])


# create object
order1 = Order("OR001", "Pista House")
order1.show_summary()

order1.update_status()
order1.update_status()
order1.update_status()
order1.update_status()