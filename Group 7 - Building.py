from abc import ABC, abstractmethod

class Building(ABC): #PARENT CLASS, NO TOUCHY 
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
        return "Open" if self.doors_are_open == True else "Closed"
    def lights_status(self):
        return "On" if self.lights_are_open == True else "Off"
    def ac_status(self):
        return "On" if self.ac_is_open == True else "Off"
    
    @abstractmethod
    def location_status(self):
        pass

    @abstractmethod
    def location_action_menu(self):
        pass

#SubClasses, dont remove the abstract methods or it will break.
class Building1(Building): #Laurence
    def location_status(self):
        return f"Building 1 is at {self.location}, with a size of {self.size}m^2, it has {self.floors} floors, and {self.rooms} rooms in total."
    
    def location_action_menu(self):
        return f"Your Building's Method Menu Go Here"
    
class Building2(Building): #Vinz
    def location_status(self):
        return f"Building 2 is at {self.location}, with a size of {self.size}m^2, it has {self.floors} floors, and {self.rooms} rooms in total."
    def location_action_menu(self):
        print(f"[1] [General Actions]  \n[2] [Go Back]")
        choice = int(input("Action Chosen: "))
        if choice == 1:
            general_actions(building2)
        elif choice == 2:
            return menu()
        else:
            print(f"Please Select A Valid Number!")
            return menu2()

class Building3(Building): #Jyvhan
    def location_status(self):
        return f"Building 3 is at {self.location}, with a size of {self.size}m^2, it has {self.floors} floors, and {self.rooms} rooms in total."
    def location_action_menu(self):
        return f"Your Building's Method Menu Go Here"
    
class Building4(Building): #Shanlee
    def location_status(self):
        return f"Building 4 is at {self.location}, with a size of {self.size}m^2, it has {self.floors} floors, and {self.rooms} rooms in total."
    def location_action_menu(self):
        return f"Your Building's Method Menu Go Here"


# DO NOT CHANGE THE VARIABLE NAME (eg. building1_name and building1) CHANGE THE ACTUAL VALUE TO MATCH THE SUBCLASS (eg. Building1 -> Library)

building1_name = "Building01"
building2_name = "Building02"
building3_name = "Building03"
building4_name = "Building04"

building1 = Building1("Batangas", 100, 4, 24)
building2 = Building2("Taal", 50, 2, 16)
building3 = Building3("Lipa", 150, 6, 36)
building4 = Building4("Quezon", 200, 10, 100)


#ALL MENUS GO UNDER HERE

def menu(): # MAIN MENU (UNIVERSAL)
    #Toggle Actions
    print(f"\nSelect Building:")
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
        print(f"Please Select A Valid Number!")
        return menu()

def menu2(selected_building): # SECONDARY MENU (UNIVERSAL)
    print(f"\nDescription: {selected_building.location_status()}")
    print(f"Available Actions: \n{selected_building.location_action_menu()}")

def general_actions(selected_building): # GENERAL MENU (UNIVERSAL)
    print(f"\nToggable Options: \n[1] [Doors] \t\t[Current status: {selected_building.door_status()}] \n[2] [Lights] \t\t[Current status: {selected_building.lights_status()}] \n[3] [Air Conditioner] \t[Current status: {selected_building.ac_status()}] \n[4] [Go Back]")
    choice = int(input("Action No. : "))
    if choice == 1:
        selected_building.toggle_doors()
        print(f"Doors are now {selected_building.door_status}!")
        return general_actions(selected_building)
    elif choice ==2:
        selected_building.toggle_lights()
        print(f"Doors are now {selected_building.lights_status}!")
        return general_actions(selected_building)
    elif choice ==3:
        selected_building.toggle_air_conditioning()
        print(f"Doors are now {selected_building.ac_status}!")
        return general_actions(selected_building)
    elif choice ==4:
        return menu2(selected_building)

menu() #STARTS THE PROGRAM