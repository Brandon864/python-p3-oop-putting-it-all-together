# lib/shoe.py
class Shoe:
    def __init__(self, brand, size):
        """Initialize a Shoe with brand, size, and condition."""
        self._brand = brand
        self._size = size
        self._condition = "New"  # Default condition

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        if not isinstance(brand, str) or not brand:
            raise ValueError("Brand must be a non-empty string")
        self._brand = brand

    brand = property(get_brand, set_brand)

    def get_size(self):
        return self._size

    def set_size(self, size):
        if not isinstance(size, int):
            print("size must be an integer")
            return
        if size <= 0:
            raise ValueError("Size must be a positive integer")
        self._size = size

    size = property(get_size, set_size)

    def get_condition(self):
        return self._condition

    def set_condition(self, condition):
        valid_conditions = ["New", "Used"]
        if condition not in valid_conditions:
            raise ValueError("Condition must be 'New' or 'Used'")
        self._condition = condition

    condition = property(get_condition, set_condition)

    def cobble(self):
        """Repair the shoe, setting condition to New."""
        self._condition = "New"
        print("Your shoe is as good as new!")