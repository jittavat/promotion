class Promotion:
    def __init__(self, promotion_code: str, qty: float, barcode: str, discount: float):
        self.barcode = barcode
        self.qty = qty
        self.promotion_code = promotion_code
        self.discount = discount

    def __str__(self) -> str:
        return f"promotion_code: {self.promotion_code}, qty: {self.qty}, barcode: {self.barcode}, discount: " \
               f"{self.discount}"

    def __repr__(self) -> str:
        return f"<promotion_code: {self.promotion_code}, qty: {self.qty}, barcode: {self.barcode}, discount: " \
               f"{self.discount}>"

    def __members(self):
        return self.promotion_code, self.barcode

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__members == other.__members
        else:
            return False

    def __hash__(self):
        return hash(self.__members)
