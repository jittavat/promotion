class SKU:
    def __init__(self, barcode: str, name: str, price: float):
        self.barcode = barcode
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"barcode: {self.barcode}, name: {self.name}, price: {self.price}"

    def __repr__(self) -> str:
        return f"<barcode: {self.barcode}, name: {self.name}, price: {self.price}>"

    @property
    def __members(self):
        return self.barcode,

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__members == other.__members
        else:
            return False

    def __hash__(self):
        return hash(self.__members)
