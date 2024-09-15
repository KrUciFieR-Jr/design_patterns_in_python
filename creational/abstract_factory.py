"""
          +---------------------+
          |   VehicleFactory    |
          +---------------------+
          | + create_car()      |
          | + create_truck()    |
          +---------+-----------+
                    |
     +--------------+--------------+
     |                             |
+------------+              +--------------+
| BrandAFactory|              | BrandBFactory|
+------------+              +--------------+
| + create_car()|              | + create_car()|
| + create_truck()|            | + create_truck()|
+------+-------+              +-------+------+
       |                              |
       |                              |
+------+-------+              +-------+-------+
| BrandACar    |              | BrandBCar     |
+--------------+              +---------------+
| + drive()    |              | + drive()     |
+--------------+              +---------------+
        |                             |
        |                             |
+------+-------+              +-------+-------+
| BrandATruck  |              | BrandBTruck   |
+--------------+              +---------------+
| + haul()     |              | + haul()      |
+--------------+              +---------------+


The Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.

When to use:
- Multiple family of products
- Use these related objects
- Don't give concrete implementations, just library for these products
- Cross platforms applications
- Confirguations you want switch

Advatnages:
- You want to use objects related to each other, this is useful
- Scalability, code becomoes scalable
- Decoupling

Pitfall:
- Complexity for large product families
- Overkill and unnecessary abstraction

Reral world:
- GUI Libraries
- Database drivers
- Testing frameworks

"""# abstract_factory.py


# Abstract products
from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class CheckBox(ABC):
    @abstractmethod
    def check(self):
        pass

# Concrete implementations of Products
class WindowsButton(Button):
    def click(self):
        return "Windows Button clicked"
    
class WindowsCheckBox(CheckBox):
    def check(self):
        return "Windows Checkbox checked"
    
class MacButton(Button):
    def click(self):
        return "Mac Button clicked"
    
class MacCheckBox(CheckBox):
    def check(self):
        return "Mac Checkbox checked"
    
class LinuxButton(Button):
    def click(self):
        return "Linux Button clicked"
    
class LinuxCheckBox(CheckBox):
    def check(self):
        return "Linux Checkbox checked"
    
# Create Abstract factory

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self)-> Button:
        pass

    @abstractmethod
    def create_checkbox(self)->CheckBox:
        pass

# Implement concrete factories
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> CheckBox:
        return WindowsCheckBox()
    
class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()
    
    def create_checkbox(self) -> CheckBox:
        return MacCheckBox()
    
class LinuxFactory(GUIFactory):
    def create_button(self) -> Button:
        return LinuxButton()
    
    def create_checkbox(self) -> CheckBox:
        return LinuxCheckBox()
    

def create_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.click())
    print(checkbox.check())

# Usage
if __name__ == "__main__":
    platform = "Windows"  # This could be dynamically determined

    if platform == "Windows":
        factory = WindowsFactory()
    else:
        factory = MacFactory()

    create_ui(factory)
