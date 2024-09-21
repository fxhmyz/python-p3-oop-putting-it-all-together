class Shoe:
    all_shoes = []

    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color
        Shoe.all_shoes.append(self)

    def __repr__(self):
        return f"<Shoe: {self.brand}, Size: {self.size}, Color: {self.color}>"

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str) and value:
            self._brand = value
        else:
            raise ValueError("Brand must be a non-empty string.")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._size = value
        else:
            raise ValueError("Size must be a positive number.")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, str) and value:
            self._color = value
        else:
            raise ValueError("Color must be a non-empty string.")

    @classmethod
    def get_all_shoes(cls):
        return cls.all_shoes
