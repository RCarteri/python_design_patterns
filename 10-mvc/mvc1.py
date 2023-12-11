class Model:
    def __init__(self):
        self.products = {
            'milk': {'id': 1, 'name': 'milk', 'price': 1.50, 'quantity': 10},
            'water': {'id': 2, 'name': 'water', 'price': 0.50, 'quantity': 20},
            'juice': {'id': 3, 'name': 'juice', 'price': 2.50, 'quantity': 5}
        }

class Controller:
    def __init__(self):
        self.model = Model()

    def get_product(self):
        products = self.model.products.keys()
        for product in products:
            print(self.model.products[product])
class View:
    def __init__(self):
        self.controller = Controller()

    def products_list(self):
        self.controller.get_product()

if __name__ == '__main__':
    view = View()
    view.products_list()