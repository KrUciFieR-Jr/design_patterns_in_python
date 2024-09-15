from dataclasses import dataclass, field

@dataclass
# @dataclass(frozen=True) # To make data immutability
class Pizza:
    size: str = None  # Corrected type annotation to str
    crust: str = None  # Corrected type annotation to str
    toppings: list = field(default_factory=list)

    def __str__(self):
        return f"Pizza(size={self.size}, crust={self.crust}, toppings={self.toppings})"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size: str) -> 'PizzaBuilder':
        self.pizza.size = size  # Correctly setting the size on the Pizza instance
        return self

    def set_crust(self, crust: str) -> 'PizzaBuilder':
        self.pizza.crust = crust  # Correctly setting the crust on the Pizza instance
        return self

    def add_topping(self, topping: str) -> 'PizzaBuilder':
        self.pizza.toppings.append(topping)  # Correctly adding a topping to the Pizza instance
        return self

    def build(self) -> Pizza:
        return self.pizza  # Correctly returning the built Pizza instance

    def __enter__(self) -> 'PizzaBuilder':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("An error occurred while building Pizza:", exc_val)
        else:
            print("Pizza was built successfully!")

if __name__ == "__main__":
    # Using the builder in a context manager
    with PizzaBuilder() as builder:
        pizza = (builder
                 .set_size('Large')
                 .set_crust('Stuffed')
                 .add_topping('Mushrooms')
                 .add_topping('Olives')
                 .build())

    print(pizza)
