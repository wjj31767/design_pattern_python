"""
代码说明：
1. 场景背景
现有旧系统接口 OldDataInterface 返回元组格式数据（如 (key, value) 元组列表），但新系统要求使用字典格式数据。适配器模式用于转换这种不兼容的接口。
2. 类适配器（Class Adapter）
实现方式：通过继承旧接口 OldDataInterface 和实现目标接口 NewDataInterface，直接复用旧接口的方法。
核心代码：
python
class ClassAdapter(OldDataInterface, NewDataInterface):
    def get_data_as_dict(self):
        tuple_data = self.get_data_as_tuple()  # 调用旧接口方法
        return {k: v for k, v in tuple_data}  # 转换为字典

特点：
依赖继承，耦合度较高（需适配类支持继承）。
可直接重写旧接口方法，适合接口差异较小的场景。
3. 对象适配器（Object Adapter）
实现方式：通过组合旧接口实例（而非继承），在目标接口方法中委托旧接口的功能。
核心代码：
python
class ObjectAdapter(NewDataInterface):
    def __init__(self, adaptee):
        self.adaptee = adaptee  # 持有旧接口对象
    def get_data_as_dict(self):
        return {k: v for k, v in self.adaptee.get_data_as_tuple()}

特点：
依赖组合，更灵活（无需修改旧接口，符合 “合成复用原则”）。
适合旧接口不可继承或需适配多个旧接口的场景。
4. 客户端调用
无论使用类适配器还是对象适配器，客户端代码（DataConsumer）只需依赖目标接口 NewDataInterface，无需关心底层数据格式转换细节，体现了适配器模式 “解耦接口” 的核心思想。
两种适配器对比：
特性	类适配器	对象适配器
实现方式	继承旧接口（类级适配）	组合旧接口实例（对象级适配）
语言支持	需语言支持多重继承（如 Python）	所有语言均可（更通用）
灵活性	较低（修改旧接口需改适配器）	较高（旧接口不变，适配器内部转换）
适配数量	单旧接口适配	可适配多个旧接口（通过组合）
适用场景扩展：
第三方库适配：当第三方库接口与现有系统不兼容时，通过适配器统一接口（如将不同数据库驱动的查询结果统一为字典格式）。
遗留系统整合：在新旧系统过渡期间，通过适配器让旧模块兼容新接口，避免大规模代码重构。
数据格式转换：如将 XML 数据转换为 JSON、将 CSV 行转换为对象实例等场景。
两种适配器均成功将旧接口的元组数据转换为目标接口的字典格式，客户端无需修改代码即可兼容不同适配器，体现了适配器模式的灵活性和复用性。
"""


# -------------------------- 场景：新旧接口数据格式转换 --------------------------
# 目标接口：新系统需要字典格式数据
class NewDataInterface:
    def get_data_as_dict(self):
        raise NotImplementedError


# 现有旧接口：返回元组格式数据（无法直接使用）
class OldDataInterface:
    def get_data_as_tuple(self):
        return ("name", "Alice"), ("age", 30), ("city", "New York")


# -------------------------- 方式1：类适配器（通过继承实现） --------------------------
class ClassAdapter(OldDataInterface, NewDataInterface):
    def get_data_as_dict(self):
        # 继承旧接口，重写目标方法，将元组转换为字典
        tuple_data = self.get_data_as_tuple()
        return {k: v for k, v in tuple_data}


# -------------------------- 方式2：对象适配器（通过组合实现） --------------------------
class ObjectAdapter(NewDataInterface):
    def __init__(self, adaptee):
        self.adaptee = adaptee  # 组合旧接口实例

    def get_data_as_dict(self):
        # 委托旧接口，转换数据格式
        tuple_data = self.adaptee.get_data_as_tuple()
        return {k: v for k, v in tuple_data}


# -------------------------- 客户端代码 --------------------------
class DataConsumer:
    def process_data(self, data_provider):
        data = data_provider.get_data_as_dict()
        print("处理后的数据（字典格式）:", data)


if __name__ == "__main__":
    old_data = OldDataInterface()

    # 使用类适配器
    class_adapter = ClassAdapter()
    consumer = DataConsumer()
    consumer.process_data(class_adapter)  # 输出：处理后的数据（字典格式）: {'name': 'Alice', 'age': 30, 'city': 'New York'}

    # 使用对象适配器
    object_adapter = ObjectAdapter(old_data)
    consumer.process_data(object_adapter)  # 输出同上