"""
代码说明：
目标接口（Voltage5V）
定义客户端所需的接口（get_5v()），表示提供 5V 电压。
被适配者（Voltage220V）
现有接口，提供 220V 电压，但无法直接被客户端使用（接口不兼容）。
适配器（PowerAdapter）
实现目标接口 Voltage5V，并持有被适配者（Voltage220V）的实例。
通过 get_5v() 方法将被适配者的 get_220v() 接口转换为目标接口，隐藏电压转换的细节。
客户端（PhoneCharger）
依赖目标接口 Voltage5V 工作，通过适配器间接使用 220V 电源，无需修改原有逻辑。
适配器模式核心特点：
解耦接口差异：让不兼容的接口通过适配器协同工作，无需修改原有类或客户端代码。
对象适配器 vs 类适配器：
示例使用对象适配器（通过组合被适配者实例），更灵活且符合 Python 动态特性。
类适配器需继承被适配者（Python 支持多重继承），但实际中对象适配器更常用。
适用场景：当现有类的接口与目标接口不匹配，但需要复用现有类时（如第三方库、遗留代码适配）。
通过适配器，客户端代码无需感知 220V 电源的存在，直接使用目标接口完成充电功能，体现了 “接口转换” 的核心思想。
"""


# 目标接口：客户端期望的接口（5V电压）
class Voltage5V:
    def get_5v(self):
        return 5


# 现有接口：无法直接使用的220V电源类
class Voltage220V:
    def get_220v(self):
        return 220


# 适配器类：将Voltage220V转换为Voltage5V接口
class PowerAdapter(Voltage5V):
    def __init__(self, adaptee):
        self.adaptee = adaptee  # 持有被适配的对象（220V电源）

    def get_5v(self):
        # 将220V转换为5V（模拟转换逻辑）
        high_voltage = self.adaptee.get_220v()
        print(f"适配器：将 {high_voltage}V 转换为 5V")
        return 5  # 实际场景中可能包含复杂的电压转换逻辑


# 客户端代码：使用5V电压的设备（如手机充电器）
class PhoneCharger:
    def charge(self, voltage_provider):
        if voltage_provider.get_5v() == 5:
            print("设备正常充电")
        else:
            print("电压不匹配，无法充电")


# 主程序
if __name__ == "__main__":
    # 现有220V电源
    voltage_220v = Voltage220V()

    # 创建适配器，将220V电源转换为5V接口
    adapter = PowerAdapter(voltage_220v)

    # 设备通过适配器获取5V电压
    charger = PhoneCharger()
    charger.charge(adapter)  # 输出：适配器：将 220V 转换为 5V -> 设备正常充电