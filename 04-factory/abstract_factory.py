from abc import ABCMeta, abstractmethod


# AbstractFactory
class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def make_pizza_veg(self):
        pass

    @abstractmethod
    def make_pizza(self):
        pass


# ConcreteFactory A
class BrazilianPizza(PizzaFactory):

    def make_pizza_veg(self):
        return PizzaMandioca()

    def make_pizza(self):
        return PizzaCamarao()


# ConcreteFactory B
class ItalianPizza(PizzaFactory):

    def make_pizza_veg(self):
        return PizzaBrocolli()

    def make_pizza(self):
        return PizzaBolonha()


# AbstractProdutoA
class PizzaVeg(metaclass=ABCMeta):

    @abstractmethod
    def prepare(self, PizzaVeg):
        pass


# AbstractProdutoB
class Pizza(metaclass=ABCMeta):

    @abstractmethod
    def serve(self, PizzaVeg):
        pass


# ProdutoConcreto
class PizzaMandioca(PizzaVeg):

    def prepare(self):
        print(f'Preparing {type(self).__name__}')


# ConcreteProduct
class PizzaCamarao(Pizza):

    def serve(self, PizzaVeg):
        print(f'{type(self).__name__} is served with camarao in {type(PizzaVeg).__name__}')


# ConcreteProduct
class PizzaBrocolli(PizzaVeg):

    def prepare(self):
        print(f'Preparing {type(self).__name__}')


# ConcreteProduct
class PizzaBolonha(Pizza):

    def serve(self, PizzaVeg):
        print(f'{type(self).__name__} is served with bolonha in {type(PizzaVeg).__name__}')


# Cliente
class PizzaStore:

    def make_pizzas(self):
        for factory in [BrazilianPizza(), ItalianPizza()]:
            self.factory = factory
            self.pizza = self.factory.make_pizza()
            self.pizza_veg = self.factory.make_pizza_veg()
            self.pizza_veg.prepare()
            self.pizza.serve(self.pizza_veg)


pizza_store = PizzaStore()
pizza_store.make_pizzas()
