class Product:
    def __init__(self, name, length, width, height, dim_unit, weight, weight_unit, quantity):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.dim_unit = dim_unit
        self.weight = weight
        self.weight_unit = weight_unit
        self.quantity = quantity
    
    def get_volume(self):
        # Convert dimensions to cm
        if self.dim_unit == "M":
            length, width, height = self.length * 100, self.width * 100, self.height * 100
        elif self.dim_unit == "INCH":
            length, width, height = self.length * 2.54, self.width * 2.54, self.height * 2.54
        else:
            length, width, height = self.length, self.width, self.height
        
        # Calculate volume in cubic cm
        return length * width * height
    
    def get_weight(self):
        # Convert weight to grams
        if self.weight_unit == "KG":
            return self.weight * 1000
        elif self.weight_unit == "OZ":
            return self.weight * 28.35
        else:
            return self.weight

class Locad:
    def __init__(self):
        self.rates = {
            "X-Small": {"max_dim": 25, "max_weight": 1000, "price": 100},
            "Small": {"max_dim": 55, "max_weight": 5000, "price": 200},
            "Medium": {"max_dim": 105, "max_weight": 25000, "price": 300},
            "Large": {"max_dim": float("inf"), "max_weight": float("inf"), "price": 400}
        }
    
    def get_size_class(self, product):
        # Calculate volume and weight of the product
        volume = product.get_volume()
        weight = product.get_weight() * product.quantity
        
        # Find the size class based on the maximum dimension and weight
        for size_class, limits in self.rates.items():
            if volume <= limits["max_dim"]**3 and weight <= limits["max_weight"]:
                return size_class
        
        # If no size class is found, return None
        return None
    
    def get_fulfillment_cost(self, products):
        total_cost = 0
        for product in products:
            size_class = self.get_size_class(product)
            if size_class is not None:
                cost = self.rates[size_class]["price"] * product.quantity
                total_cost += cost
                print(f"{product.name} ({product.quantity}): {size_class} - {cost}")
            else:
                print(f"{product.name} ({product.quantity}): Cannot be fulfilled by Locad")
        print(f"Total Fulfillment Cost: {total_cost}")

# Example usage
toy_one = Product("ToyOne", 90, 50, 40, "CM", 8000, "GM", 45)
toy_two = Product("ToyTwo", 1.2, 0.3, 0.2, "M", 9000, "GM", 28)
locad = Locad()
locad.get_fulfillment_cost([toy_one, toy_two])
