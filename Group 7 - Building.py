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
        return (f"The Library is at {self.location}, with a size of {self.size}m^2, "
                f"it has {self.floors} floors, {self.rooms} rooms, "
                f"{self.num_books} books, and is open during {self.opening_hours}.")

    def location_action_menu(self):
        print("[1] [General Actions]  \n[2] [Borrow Book]  \n[3] [Return Book]  \n[4] [Go Back]")
        choice = int(input("Action Chosen: "))
        if choice == 1:
            general_actions(building1)
        elif choice == 2:
            borrow_book(building1)
        elif choice == 3:
            return_book(building1)
        elif choice == 4:
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
        return (f"The Research Lab is at {self.location}, with a size of {self.size}m^2, "
                f"it has {self.floors} floors, {self.rooms} rooms, {self.num_labs} laboratories, "
                f"and is operational during {self.open_hours}.")

    def location_action_menu(self):
        print("[1] [General Actions]  \n[2] [Publish Research]  \n[3] [Request Lab Equipment]  \n[4] [Go Back]")
        choice = int(input("Action Chosen: "))
        if choice == 1:
            general_actions(building3)
        elif choice == 2:
            publish_research(building3)
        elif choice == 3:
            request_equipment(building3)
        elif choice == 4:
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
class Building4(Building):
    def location_status(self):
        return f"Building 4 is at {self.location}, with a size of {self.size}m^2, it has {self.floors} floors, and {self.rooms} rooms in total."

    def location_action_menu(self):
        return "Your Building's Method Menu Go Here"

# ------------------------------------------
# STATIC BUILDING INSTANCES
building1_name = "Library"
building2_name = "Building02"
building3_name = "Research Lab"
building4_name = "Building04"

building1 = Library("Batangas", 100, 4, 24, 2000, "8AM - 5PM")
building2 = Building2("Taal", 50, 2, 16)
building3 = ResearchLab("Lipa", 150, 6, 36, 5, "9AM - 6PM")
building4 = Building4("Quezon", 200, 10, 100)

# ------------------------------------------
# MENUS
def menu():
    print("\nSelect Building:")
    print(f"[1] [{building1_name}] \n[2] [{building2_name}] \n[3] [{building3_name}] \n[4] [{building4_name}] \n[5] [Exit Program]")
    selected_building = int(input("Bldg No. : "))
    if selected_building == 1:
        menu2(building1)
    elif selected_building == 2:
        menu2(building2)
    elif selected_building == 3:
        menu2(building3)
    elif selected_building == 4:
        menu2(building4)
    elif selected_building == 5:
        exit()
    else:
        print("Please Select A Valid Number!")
        return menu()

def menu2(selected_building):
    print(f"\nDescription: {selected_building.location_status()}")
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
menu()  # START THE PROGRAM
