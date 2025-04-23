"""
外观模式（Facade Pattern）是一种结构型设计模式，它为子系统中的一组接口提供一个统一的高层接口，使得子系统更易于使用。外观模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。通过引入一个外观类，将客户端与子系统的复杂性隔离开来，客户端只需要与外观类交互，而不需要了解子系统内部的具体实现细节。
"""


# 子系统类：CPU
class CPU:
    def freeze(self):
        print("CPU: Freezing process.")

    def jump(self, position):
        print(f"CPU: Jumping to position {position}.")

    def execute(self):
        print("CPU: Executing process.")


# 子系统类：内存
class Memory:
    def load(self, position, data):
        print(f"Memory: Loading data '{data}' at position {position}.")


# 子系统类：硬盘
class HardDrive:
    def read(self, lba, size):
        print(f"HardDrive: Reading {size} bytes from LBA {lba}.")


# 外观类
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hardDrive = HardDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load(0, "BOOT_DATA")
        self.cpu.jump(0)
        self.cpu.execute()


# 客户端代码
if __name__ == "__main__":
    computer = ComputerFacade()
    computer.start()
