from abc import ABCMeta, abstractmethod

class Travel(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def travel_to(self):
        pass

    @abstractmethod
    def day1(self):
        pass

    def day2(self):
        pass

    def day3(self):
        pass

    @abstractmethod
    def travel_back(self):
        pass

    def travel(self):
        self.travel_to()
        self.day1()
        self.day2()
        self.day3()
        self.travel_back()

class VenezaTravel(Travel):
    def __init__(self):
        pass

    def travel_to(self):
        print("Travel to Veneza")

    def day1(self):
        print("Day 1 in Veneza")

    def day2(self):
        print("Day 2 in Veneza")

    def day3(self):
        print("Day 3 in Veneza")

    def travel_back(self):
        print("Travel back to home")

class ParisTravel(Travel):
    def __init__(self):
        pass

    def travel_to(self):
        print("Travel to Paris")

    def day1(self):
        print("Day 1 in Paris")

    def day2(self):
        print("Day 2 in Paris")

    def day3(self):
        print("Day 3 in Paris")

    def travel_back(self):
        print("Travel back to home")

if __name__ == '__main__':
    print("Lets call the template method")
    VenezaTravel().travel()

    ParisTravel().travel()
