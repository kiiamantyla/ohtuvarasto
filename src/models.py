class Product:
    def __init__(self, name, price, quantity):
        self.id = None
        self.name = name
        self.price = price
        self.quantity = quantity


class Warehouse:
    def __init__(self, name):
        self.id = None
        self.name = name
        self.products = []
        self._next_product_id = 1

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        product.id = self._next_product_id
        self._next_product_id += 1
        self.products.append(product)
        return product

    def get_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def delete_product(self, product_id):
        product = self.get_product(product_id)
        if product:
            self.products.remove(product)
            return True
        return False


class WarehouseStore:
    def __init__(self):
        self.warehouses = []
        self._next_id = 1

    def add_warehouse(self, name):
        warehouse = Warehouse(name)
        warehouse.id = self._next_id
        self._next_id += 1
        self.warehouses.append(warehouse)
        return warehouse

    def get_warehouse(self, warehouse_id):
        for warehouse in self.warehouses:
            if warehouse.id == warehouse_id:
                return warehouse
        return None

    def delete_warehouse(self, warehouse_id):
        warehouse = self.get_warehouse(warehouse_id)
        if warehouse:
            self.warehouses.remove(warehouse)
            return True
        return False

    def get_all_warehouses(self):
        return self.warehouses
