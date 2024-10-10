class Device:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def turn_on(self):
        print(f"{self.brand} {self.model} is powered on.")

    def turn_off(self):
        print(f"{self.brand} {self.model} is powered off.")

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")


class Laptop(Device):
    def __init__(self, brand, model, price, ram_size):
        super().__init__(brand, model, price)
        self.ram_size = ram_size

    def open_laptop(self):
        print(f"{self.brand} {self.model} is opened.")

    def display_info(self):
        super().display_info()
        print(f"RAM Size: {self.ram_size} GB")


class Smartphone(Device):
    def __init__(self, brand, model, price, camera_resolution):
        super().__init__(brand, model, price)
        self.camera_resolution = camera_resolution

    def take_photo(self):
        print(f"Photo taken with {self.brand} {self.model}.")

    def display_info(self):
        super().display_info()
        print(f"Camera Resolution: {self.camera_resolution} MP")


# Example:
laptop = Laptop("Dell", "tynn", 998.89, 14)
laptop.turn_on()
laptop.display_info()
laptop.open_laptop()
laptop.turn_off()

smartphone = Smartphone("Sumsunge", "s 24th", 79.29, 16)
smartphone.turn_on()
smartphone.display_info()
smartphone.take_photo()
smartphone.turn_off()