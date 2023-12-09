class Instalator:
    def __init__(self, font, destiny):
        self.options = []
        self.font = font
        self.destiny = destiny

    def preferencies(self, option):
        self.options.append(option)

    def execute(self):
        for option in self.options:
            if list(option.values())[0]:
                print(f'Instalando {self.font} en {self.destiny} con {option}')
            else:
                print("Operation finished")

if __name__ == '__main__':
    instalator = Instalator('Arial', 'C:/Windows/Fonts')
    instalator.preferencies({'bold': True})
    instalator.preferencies({'italic': False})
    instalator.preferencies({'underline': True})
    instalator.preferencies({'sdf': True})
    instalator.execute()