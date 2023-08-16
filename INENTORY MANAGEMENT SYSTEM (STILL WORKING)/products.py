import datetime


class Products():
    all_products = []
    country = "India"

    def __init__(self, name: str, cost_price, mrp, quantity: int):
        assert isinstance(name, str), "Name should be a string..."
        self.name = name

        assert isinstance(cost_price, float), "Cost Price should be a Float..."
        self.cost_price = cost_price
        assert isinstance(mrp, float) or isinstance(
            mrp, int), "MRP should be a Float..."
        self.mrp = mrp

        assert isinstance(quantity, int), "Qunatity should be integer."
        assert quantity > 0, "Quantity should be greater than 0!"
        self.quantity = quantity
        if None in self.all_products:
            index = self.all_products.index(None)
            Products.all_products[index] = self
        else:
            Products.all_products.append(self)
        self.generateBarcode()

    def generateBarcode(self):
        # Format: YYYYMMCXXXX
        """
        YYYY: Year of purchase in 4 digits (to be fetched from the system date using datetime module)
        MM: Month of purchase in 2 digits (to be fetched from the system date using datetime module)
        C: category_code (E/G/F/T/C)
        XXXX: Index number in the list + 100
        """

    def generateBarcode(self):
        purchase_year = datetime.datetime.today().strftime("%Y")
        purchase_month = datetime.datetime.today().strftime("%m")
        self.barcode = str(purchase_year)+str(purchase_month)+"".join(
            self.category_code+str(str(Products.all_products.index(self)+100).zfill(4)))

    def show_details(self):
        print(f"------------- Details of {self.name} -------------")
        print("Category:", self.category)
        print("Cost price:", self.cost_price)
        print("MRP:", self.mrp)
        print("Stock:", self.quantity)
        print("Barcode:", self.barcode)

    @staticmethod
    def addNewItem():
        print("Enter the following details:")
        name = input("Name: ")
        cost_price = float(input("Cost Price: "))
        mrp = float(input("MRP: "))
        quantity = int(input("Quantity: "))
        return name, cost_price, mrp, quantity

    def deleteItem(self):
        Products.all_products[int(self.barcode[-4:])-100] = None

    @staticmethod
    def showInventory():
        print("SrNo\t\tItem Name")
        for item in Products.all_products:
            if item != None:
                print(f"{item.barcode}\t{item.name}")
        barcode = input("Enter barcode no: ")
        index = int(barcode[-4:]) - 100
        return index

    def editDetails(self):
        print("Enter new details (Press 'Enter' to keep old detail):")
        print("Field\tOld Value\tNew Value".expandtabs(20))
        name = input(f"Item Name\t{self.name}:\t ")
        self.name = self.name if name == "" else name
        category = input(f"Item Name\t {self.category}:\t")
        self.category = self.category if category == "" else category
        cost_price = input(f"Item Name\t {self.cost_price}:\t")
        self.cost_price = self.cost_price if cost_price == "" else cost_price
        mrp = input(f"Item Name\t {self.mrp}:\t")
        self.mrp = self.mrp if mrp == "" else mrp
        quantity = input(f"Item Name\t{self.quantity}:\t ".expandtabs(30))
        self.quantity = self.quantity if quantity == "" else quantity
        month = input(
            f"Month\t{self.barcode[4 : 6]}:\t".expandtabs(20)).zfill(2)
        if month != "":
            self.barcode = self.barcode[: 4] + month + self.barcode[6:]
        year = input(f"Year\t{self.barcode[ : 4]}:\t".expandtabs(20))

        if year != "":
            self.barcode = year + self.barcode[4:]


if __name__ == '__main__':
    # p1 = Products("1234", 35.5, 50.5, 10)
    # p1.show_details()
    # p2 = Products("Sample product 1", 35.5, 50.5, 10)
    # p2.show_details()
    # s1 = 123
    # print(isinstance(s1, str))
    pass
