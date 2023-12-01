class SanityCheck:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not SanityCheck.__instance:
            SanityCheck.__instance = super(SanityCheck, cls).__new__(cls, *args, **kwargs)
        return SanityCheck.__instance

    def __init__(self):
        self.__servers = []

    def check_server(self, server):
        print(f'Checking: {server}')

    def add_server(self):
        self.__servers.append('Server 1')
        self.__servers.append('Server 2')
        self.__servers.append('Server 3')
        self.__servers.append('Server 4')

    def change_server(self):
        self.__servers.pop()
        self.__servers.append('Server 5')

sc1 = SanityCheck()
sc2 = SanityCheck()

sc1.add_server()
print(f'Servers in sc1: {sc1._SanityCheck__servers}')

sc2.change_server()
print(f'Servers in sc2: {sc2._SanityCheck__servers}')
