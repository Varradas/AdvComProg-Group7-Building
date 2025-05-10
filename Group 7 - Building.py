from abc import ABC, abstractmethod

class Building(ABC):  # PARENT CLASS, NO TOUCHY
    def __init__(self, location, size, floors, rooms):
        self.location = location
        self.size = size
        self.floors = floors
        self.rooms = rooms

        self.doors_are_open = False
        self.lights_are_open = False
        self.ac_is_open = False

    def toggle_doors(self):
        self.doors_are_open = not self.doors_are_open
        return self.doors_are_open

    def toggle_lights(self):
        self.lights_are_open = not self.lights_are_open
        return self.lights_are_open

    def toggle_air_conditioning(self):
        self.ac_is_open = not self.ac_is_open
        return self.ac_is_open

    def door_status(self):
        return "Open" if self.doors_are_open else "Closed"

    def lights_status(self):
        return "On" if self.lights_are_open else "Off"

    def ac_status(self):
        return "On" if self.ac_is_open else "Off"

    @abstractmethod
    def location_status(self):
        pass

    @abstractmethod
    def location_action_menu(self):
        pass

# ------------------------------------------
# Library (Building 1) - Laurence
class Library(Building):
    def __init__(self, location, size, floors, rooms, num_books, opening_hours):
        super().__init__(location, size, floors, rooms)
        self.num_books = num_books
        self.opening_hours = opening_hours

    def location_status(self):
        return (f"The Library is at {self.location}, with a size of {self.size}m², "
                f"it has {self.floors} floors, {self.rooms} rooms, "
                f"{self.num_books} books, and is open during {self.opening_hours}.")

    def location_action_menu(self):
        print("[1] [General Actions]  \n[2] [Borrow Book]  \n[3] [Return Book]  \n[0] [Go Back]")
        choice = int(input("Action Chosen: "))
        if choice == 1:
            general_actions(building1)
        elif choice == 2:
            borrow_book(building1)
        elif choice == 3:
            return_book(building1)
        elif choice == 0:
            return menu()
        else:
            print("Please Select A Valid Number!")
            return menu2(building1)
    def borrow_book_action(self, book_title):
        print(f"----------------------------------------------------------\nYou have borrowed '{book_title}'. Please return it on time!")
        print("----------------------------------------------------------")

    def return_book_action(self, book_title):
        print(f"----------------------------------------------------------\nYou have returned '{book_title}'. Thank you!")
        print("----------------------------------------------------------")

# ------------------------------------------
# Building 2 - Vinz
class Retail_Building(Building):
    def __init__(self, location, size, floors, rooms, personal_budget=0):
        super().__init__(location, size, floors, rooms)
        self.personal_budget = personal_budget
        self.stores_floor1 = [] 
        self.stores_floor2 = []
        self.cart = []
        
    def location_status(self):
        total_stores = len(self.stores_floor1) + len(self.stores_floor2)
        return f"Welcome to {self.location}! \n{self.location} has a Gross Floor Area of {self.size}m²\nThere are {self.floors} floors and {total_stores} stores.\nYour Budget: {self.personal_budget} PHP"

    def location_action_menu(self):
        while True:
            print("\n[1] [Check Building Facilities] \n[2] [Roam 1st Floor Stores] \n[3] [Roam 2nd Floor Stores] \n[0] [Go Back]")
            choice = input("Action: ")
            if choice == '1':
                general_actions(self)
            elif choice == '2':
                self._handle_floor_selection(1)
            elif choice == '3':
                self._handle_floor_selection(2)
            elif choice == '0':
                return menu()
            else:
                print("Invalid choice!")
    def _handle_floor_selection(self, floor):
        if not self.doors_are_open:
            print("Doors are closed! Open them first.")
            return
        stores = self.stores_floor1 if floor == 1 else self.stores_floor2
        while True:
            print(f"\n--- Floor {floor} Stores ---")
            for i, store in enumerate(stores, 1):
                print(f"[{i}] [{store['name']}]")
            print("[0] Go Back")
            choice = input("Select store: ")
            if choice == "0":  # Go back condition
                return
            elif choice.isdigit() and 1 <= int(choice) <= len(stores):
                self._enter_store(stores[int(choice)-1])
            else:
                print("Invalid choice!")

    def _enter_store(self, store):
        while True:
            print(f"\n-- {store['name']} -- \n[1] [View Products] \n[2] [View Cart] \n[3] [Checkout] \n[0] [Go Back]")
            choice = input("Action: ")
            if choice == '1':
                self._view_products(store)
            elif choice == '2':
                self._view_cart()
            elif choice == '3':
                self._checkout()
            elif choice == '0':
                return
            else:
                print("Invalid choice!")

    def _view_products(self, store):
        products = store['products']
        print("\nAvailable Products:")
        for i, p in enumerate(products, 1):
            print(f"[{i}] {p['name']} - {p['price']} PHP")
        print(f"[0] Go Back")
        choice = input("Select product: ")
        if choice == "0":
            return
        elif choice.isdigit() and 1 <= int(choice) <= len(products):
            product = products[int(choice)-1]
            qty = int(input("Quantity: "))
            self.cart.append({
                'product': product['name'],
                'price': product['price'],
                'quantity': qty,
                'total': product['price'] * qty
            })
            print(f"Added {qty}x {product['name']} to cart.")
        else:
            print("Invalid choice!")

    def _view_cart(self):
        if not self.cart:
            print("Cart is empty.")
            return
        total = 0
        print("\n--- Your Cart ---")
        for i, item in enumerate(self.cart, 1):
            print(f"{i}. {item['product']} ({item['quantity']}x) = {item['total']} PHP")
            total += item['total']
        print(f"TOTAL: {total} PHP\n[1] Remove item\n[0] Back")
        choice = input("Action: ")
        if choice == '1':
            idx = int(input("Enter item number: ")) - 1
            if 0 <= idx < len(self.cart):
                removed = self.cart.pop(idx)
                print(f"Removed {removed['product']}.")
            else:
                print("Invalid index!")
        elif choice != '0':
            print("Invalid choice!")

    def _checkout(self):
        total = sum(item['total'] for item in self.cart)
        if total == 0:
            print("Cart is empty!")
            return
        if self.personal_budget < total:
            print("Insufficient funds!")
            return
        self.personal_budget -= total
        print(f"Paid {total} PHP. Remaining budget: {self.personal_budget} PHP")
        self.cart.clear()

# ------------------------------------------
# Building 3 - Jyvhan (YOU) ➜ RESEARCH LAB
class ResearchLab(Building):
    def __init__(self, location, size, floors, rooms, num_labs, open_hours):
        super().__init__(location, size, floors, rooms)
        self.num_labs = num_labs
        self.open_hours = open_hours

    def location_status(self):
        return (f"The Research Lab is at {self.location}, with a size of {self.size}m², "
                f"it has {self.floors} floors, {self.rooms} rooms, {self.num_labs} laboratories, "
                f"and is operational during {self.open_hours}.")

    def location_action_menu(self):
        print("[1] [General Actions]  \n[2] [Publish Research]  \n[3] [Request Lab Equipment]  \n[0] [Go Back]")
        choice = int(input("Action Chosen: "))
        if choice == 1:
            general_actions(building3)
        elif choice == 2:
            publish_research(building3)
        elif choice == 3:
            request_equipment(building3)
        elif choice == 0:
            return menu()
        else:
            print("Please Select A Valid Number!")
            return menu2(building3)

    def publish_research_action(self, research_title):
       print(f"----------------------------------------------------------\nResearch titled '{research_title}' has been successfully published!")
       print("----------------------------------------------------------")


    def request_equipment_action(self, equipment_name):
       print(f"----------------------------------------------------------\nRequest for '{equipment_name}' has been sent to the lab manager!")
       print("----------------------------------------------------------")
    
# ------------------------------------------
# Building 4 - Shanlee
class CanteenBuilding(Building):
    def __init__(self, location, size, floors, rooms, number_of_tables, menu_items):
        super().__init__(location, size, floors, rooms)
        self.number_of_tables = number_of_tables
        self.menu_items = menu_items 

    def open_doors(self):
        print(f"\nCanteen is now open. Enjoy your meal!")

    def close_doors(self):
        print(f"\nCanteen is now closed. Please come again.")

    def order_food(self, item):
        if item in self.menu_items:
            print(f"\n{item} has been ordered. Please wait while we prepare it.")
        else:
            print(f"\nSorry, {item} is not available on the menu.")

    def clean_tables(self):
        print(f"\nCleaning all {self.number_of_tables} tables in the canteen.")

    def location_status(self):
        return f"\nWelcome to the {self.location}, this canteen covers a size of {self.size}m², it has {self.floors} floor, and {self.rooms} room in total, with {self.number_of_tables} total tables."

    def location_action_menu(self):
        while True:
            print("[1] [Check Building Facilities]  \n[2] [Order Food] \n[3] [Clean Tables] \n[0] [Go Back]")
            choice = int(input("Action Chosen: "))
            if choice == 1:
                general_actions(building4)
            elif choice == 2:
                if not self.doors_are_open:
                    print(f"Canteen is closed! Please open them first.")
                    return menu2(building4)
                else:
                    building4.order_food(input(f"\n[Burger] \n[Fries] \n[Shawarma] \n[Soda] \n[Water] \nType Name of Food: "))
            elif choice == 3:
                building4.clean_tables()
            elif choice == 0:
                return menu()
            else:
                print("Please Select A Valid Number!")
                return menu2(building4)

# ------------------------------------------
# STATIC BUILDING INSTANCES
building1_name = "Library"
building2_name = "Mall"
building3_name = "Research Lab"
building4_name = "Canteen"

building1 = Library("Batangas", 100, 4, 24, 2000, "8AM - 5PM")
building2 = Retail_Building("SM Lemery", 14000, 2, 4, personal_budget=100000)
building3 = ResearchLab("Lipa", 150, 6, 36, 5, "9AM - 6PM")
building4 = CanteenBuilding("Campus North Wing", "300 sqm", 1, 1, 20, ["Burger", "Fries", "Shawarma", "Soda", "Water"])

# ------------------------------------------
# MENUS
def menu():
    print("\nSelect Building:")
    print(f"[1] [{building1_name}] \n[2] [{building2_name}] \n[3] [{building3_name}] \n[4] [{building4_name}] \n[0] [Exit Program]")
    selected_building = int(input("Bldg No. : "))
    if selected_building == 1:
        menu2(building1)
    elif selected_building == 2:
        menu2(building2)
    elif selected_building == 3:
        menu2(building3)
    elif selected_building == 4:
        menu2(building4)
    elif selected_building == 0:
        exit()
    else:
        print("Please Select A Valid Number!")
        return menu()

def menu2(selected_building):
    print(f"\n{selected_building.location_status()}")
    selected_building.location_action_menu()

def general_actions(selected_building):
    print(f"\nToggable Options: \n[1] [Doors] \t\t[Current status: {selected_building.door_status()}] \n[2] [Lights] \t\t[Current status: {selected_building.lights_status()}] \n[3] [Air Conditioner] \t[Current status: {selected_building.ac_status()}] \n[0] [Go Back]")
    choice = int(input("Action No. : "))
    if choice == 1:
        selected_building.toggle_doors()
        print(f"Doors are now {selected_building.door_status()}!")
        return general_actions(selected_building)
    elif choice == 2:
        selected_building.toggle_lights()
        print(f"Lights are now {selected_building.lights_status()}!")
        return general_actions(selected_building)
    elif choice == 3:
        selected_building.toggle_air_conditioning()
        print(f"Air Conditioner is now {selected_building.ac_status()}!")
        return general_actions(selected_building)
    elif choice == 0:
        return menu2(selected_building)

# ------------------------------------------
# LIBRARY-SPECIFIC
def borrow_book(library):
    book_title = input("----------------------------------------------------------\nEnter the title of the book to borrow: ")
    print("----------------------------------------------------------\n")
    library.borrow_book_action(book_title)
    return menu2(library)


def return_book(library):
    book_title = input("----------------------------------------------------------\nEnter the title of the book to return: ")
    print("----------------------------------------------------------\n")
    library.return_book_action(book_title)
    return menu2(library)


# ------------------------------------------
# RESEARCH LAB-SPECIFIC
def publish_research(research_lab):
  title = input("----------------------------------------------------------\n What is the name of the research to be published? ")
  print("----------------------------------------------------------\n")
  research_lab.publish_research_action(title)
  return menu2(research_lab)
    
    
    
    

def request_equipment(research_lab):
    equipment = input("----------------------------------------------------------\n What lab equipment do you want to request? ")
    print("----------------------------------------------------------\n")
    research_lab.request_equipment_action(equipment)
    return menu2(research_lab)

# ------------------------------------------
# RETAIL BUILDING SHOP DATA
building2.stores_floor1 = [
    {'name': 'Bench Body', 'products': [
        {'name': 'Classic White T-shirt', 'price': 399},
        {'name': 'Denim Jeans', 'price': 799},
        {'name': 'Floral Summer Dress', 'price': 799},
        {'name': 'Cotton Boxer Briefs (3-pack)', 'price': 799},
        {'name': 'Canvas Tote Bag', 'price': 799},
        {'name': 'Leather Wallet', 'price': 799},
        {'name': 'Striped Polo Shirt', 'price': 799},
        {'name': 'Cotton Socks (5-pack)', 'price': 799},
        {'name': 'Knit Beanie', 'price': 799},
        {'name': 'Linen Button-down Shirt', 'price': 799},
    ]},
    {'name': 'National Bookstore', 'products': [
        {'name': 'College Notebook', 'price': 45.00},
        {'name': 'Ballpen (Black)', 'price': 12.00},
        {'name': 'Scientific Calculator', 'price': 395.00},
        {'name': 'Sticker Set', 'price': 89.00},
        {'name': 'Colored Pencils (24pc)', 'price': 199.00},
        {'name': 'Harry Potter Paperback', 'price': 599.00},
        {'name': 'Plastic Folder', 'price': 25.00},
        {'name': 'Watercolor Paint Set', 'price': 249.00},
        {'name': 'Correction Tape', 'price': 55.00},
        {'name': 'Stapler with Staples', 'price': 129.00}
    ]},
    {'name': 'Greenwich', 'products': [
        {'name': 'Hawaiian Overload Pizza (Large)', 'price': 349.00},
        {'name': 'Spaghetti Platter', 'price': 129.00},
        {'name': 'Garlic Pepper Beef Rice Meal', 'price': 159.00},
        {'name': 'Chicken Wings (6pc)', 'price': 189.00},
        {'name': 'Lasagna Supreme', 'price': 179.00},
        {'name': 'Tuna Melt Sandwich', 'price': 99.00},
        {'name': 'Overloaded Fries', 'price': 119.00},
        {'name': 'Iced Tea (Regular)', 'price': 45.00},
        {'name': 'Pepperoni Overload Pizza (Family)', 'price': 499.00},
        {'name': 'Choco Lava Cake', 'price': 69.00}
    ]},
    {'name': 'Cotti Coffee', 'products': [
        {'name': 'Americano (Hot)', 'price': 110.00},
        {'name': 'Iced Latte', 'price': 140.00},
        {'name': 'Matcha Latte', 'price': 150.00},
        {'name': 'Croissant', 'price': 95.00},
        {'name': 'Blueberry Cheesecake', 'price': 165.00},
        {'name': 'Cold Brew', 'price': 130.00},
        {'name': 'Chocolate Chip Cookie', 'price': 75.00},
        {'name': 'Caramel Macchiato', 'price': 155.00},
        {'name': 'Tiramisu', 'price': 175.00},
        {'name': 'Bottled Water', 'price': 40.00}
    ]},
]

building2.stores_floor2 = [
    {'name': 'Octagon', 'products': [
        {'name': 'Wireless Earbuds', 'price': 1299.00},
        {'name': 'Bluetooth Speaker', 'price': 899.00},
        {'name': 'Power Bank 10000mAh', 'price': 799.00},
        {'name': 'USB-C Cable', 'price': 199.00},
        {'name': 'Smartwatch', 'price': 2499.00},
        {'name': 'HDMI Cable', 'price': 349.00},
        {'name': 'Wireless Mouse', 'price': 499.00},
        {'name': '32GB USB Flash Drive', 'price': 399.00},
        {'name': 'Phone Stand', 'price': 149.00},
        {'name': 'Screen Protector', 'price': 299.00}
    ]},
    {'name': 'Miniso', 'products': [
        {'name': 'Scented Candle', 'price': 199.00},
        {'name': 'Plush Toy (Small)', 'price': 299.00},
        {'name': 'Face Mask (5pc)', 'price': 149.00},
        {'name': 'Portable Fan', 'price': 499.00},
        {'name': 'Anime Socks', 'price': 129.00},
        {'name': 'Ceramic Mug', 'price': 249.00},
        {'name': 'Phone Case', 'price': 199.00},
        {'name': 'LED Desk Lamp', 'price': 599.00},
        {'name': 'Backpack', 'price': 699.00},
        {'name': 'Hair Clip Set', 'price': 99.00}
    ]},
    {'name': 'Beyond the Box', 'products': [
        {'name': 'Apple AirPods Pro (2nd Gen)', 'price': 14990.00},
        {'name': 'Sony WH-1000XM5 Headphones', 'price': 25990.00},
        {'name': 'Dyson Supersonic Hair Dryer', 'price': 23990.00},
        {'name': 'Marshall Stanmore II Bluetooth Speaker', 'price': 19990.00},
        {'name': 'Nintendo Switch OLED', 'price': 16990.00},
        {'name': 'Bose QuietComfort Earbuds', 'price': 14990.00},
        {'name': 'Samsung Galaxy Watch5 Pro', 'price': 23990.00},
        {'name': 'JBL Flip 6 Portable Speaker', 'price': 7990.00},
        {'name': 'Logitech MX Master 3S Mouse', 'price': 6990.00},
        {'name': 'OtterBox iPhone 14 Pro Case', 'price': 3490.00}
    ]},
    {'name': 'Samsung', 'products': [
        {'name': 'Galaxy S23 Ultra (256GB)', 'price': 84990.00},
        {'name': 'Galaxy Z Fold5 (512GB)', 'price': 98990.00},
        {'name': 'Galaxy Tab S9 Ultra (5G)', 'price': 49990.00},
        {'name': 'Galaxy Watch6 Classic (47mm)', 'price': 24990.00},
        {'name': 'Galaxy Buds2 Pro', 'price': 11990.00},
        {'name': '65" QLED 4K Smart TV', 'price': 129990.00},
        {'name': '32" Smart Monitor M70B', 'price': 19990.00},
        {'name': 'Portable SSD T7 (1TB)', 'price': 9990.00},
        {'name': 'Bespoke Refrigerator 4-Door', 'price': 159990.00},
        {'name': 'Ecobubble Washing Machine (9kg)', 'price': 69990.00}
    ]},
]
menu()  # START THE PROGRAM
