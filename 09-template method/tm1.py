from abc import ABCMeta, abstractmethod

class Compilator(metaclass=ABCMeta):
    @abstractmethod
    def collect_source(self):
        pass
    @abstractmethod
    def compile_to_object(self):
        pass
    @abstractmethod
    def run(self):
        pass
    def compile_and_run(self):
        self.collect_source()
        self.compile_to_object()
        self.run()

class IOS(Compilator):
    def collect_source(self):
        print("Collecting Swift Source Code")
    def compile_to_object(self):
        print("Compiling Swift code to LLVM bitcode")
    def run(self):
        print("Program running on runtime environment")

class Android(Compilator):
    def collect_source(self):
        print("Collecting Kotlin Source Code")
    def compile_to_object(self):
        print("Compiling Kotlin code to JVM bytecode")
    def run(self):
        print("Program running on JVM")

if __name__ == '__main__':
    ios = IOS()
    android = Android()

    print("IOS compilation")
    ios.compile_and_run()

    print("Android compilation")
    android.compile_and_run()