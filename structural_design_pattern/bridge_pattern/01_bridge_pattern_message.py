"""
代码说明：
1. 实现部分（Implementor）
抽象实现接口（MessageImplementor）：定义具体行为（如发送消息）的接口，不依赖抽象部分。
具体实现类（NormalSender/EncryptedSender）：实现不同的发送逻辑（普通发送、加密发送），可独立扩展（如新增 VoiceSender）。
2. 抽象部分（Abstraction）
抽象消息类（MessageAbstraction）：
持有实现类的引用（implementor），通过组合而非继承关联实现部分（桥接核心）。
定义高层接口（send_message），将具体实现委托给 implementor。
具体抽象类（EmailMessage/SmsMessage）：
扩展抽象类，实现具体消息类型的逻辑（如邮件、短信的预处理），但不涉及发送细节（由实现类处理）。
3. 桥接模式核心机制
分离抽象与实现：消息类型（邮件 / 短信）和发送方式（普通 / 加密）可独立变化。
新增消息类型：只需创建新的 MessageAbstraction 子类（如 WeChatMessage），无需修改发送方式。
新增发送方式：只需创建新的 MessageImplementor 子类（如 VoiceSender），无需修改消息类型。
动态组合：通过 set_implementor 方法，抽象类可在运行时切换实现类（如邮件从普通发送切换为加密发送）。
4. 客户端调用
python
email.send_message("会议通知...", "user@example.com")

客户端只需与抽象类（EmailMessage/SmsMessage）交互，无需关心具体发送方式，体现了 “高层抽象与底层实现解耦” 的思想。
适用场景：
抽象与实现需独立扩展：如跨平台 UI 组件（“按钮” 抽象与 “Windows/Mac 实现” 分离）、日志系统（“日志级别” 抽象与 “文件 / 数据库 存储实现” 分离）。
避免多层继承：当系统存在两个独立变化的维度（如消息类型 + 发送方式），多层继承会导致类爆炸（如 EmailNormalSender, EmailEncryptedSender, SmsNormalSender...），桥接模式通过组合替代继承，减少类数量。
运行时动态切换实现：如根据配置或用户需求，动态选择不同的实现策略（如普通模式 / 安全模式）。
核心优势：
解耦抽象与实现：两者可独立开发和扩展，符合 “开闭原则”。
提高可复用性：实现类可被多个抽象类复用（如 EncryptedSender 可用于邮件、短信、微信消息）。
简化系统设计：避免复杂的继承层级，通过组合关系清晰分离职责。
"""


# -------------------------- 实现部分（Implementor） --------------------------
# 抽象实现接口：定义消息发送的具体行为
class MessageImplementor:
    def send(self, message: str, receiver: str):
        raise NotImplementedError


# 具体实现类：普通发送方式
class NormalSender(MessageImplementor):
    def send(self, message: str, receiver: str):
        print(f"普通发送：发送消息 '{message}' 给 {receiver}")


# 具体实现类：加密发送方式
class EncryptedSender(MessageImplementor):
    def send(self, message: str, receiver: str):
        # 模拟加密逻辑
        encrypted_msg = f"[加密] {message}"
        print(f"加密发送：发送消息 '{encrypted_msg}' 给 {receiver}")


# -------------------------- 抽象部分（Abstraction） --------------------------
# 抽象消息类：持有实现类的引用，定义高层接口
class MessageAbstraction:
    def __init__(self, implementor: MessageImplementor):
        self.implementor = implementor  # 桥接实现部分

    def set_implementor(self, implementor: MessageImplementor):
        self.implementor = implementor

    def send_message(self, message: str, receiver: str):
        raise NotImplementedError


# 具体抽象类：邮件消息
class EmailMessage(MessageAbstraction):
    def send_message(self, message: str, receiver: str):
        print(f"邮件消息：准备发送给 {receiver}")
        self.implementor.send(message, receiver)  # 委托给实现类


# 具体抽象类：短信消息
class SmsMessage(MessageAbstraction):
    def send_message(self, message: str, receiver: str):
        print(f"短信消息：准备发送给 {receiver}")
        self.implementor.send(message, receiver)  # 委托给实现类


# -------------------------- 客户端代码 --------------------------
if __name__ == "__main__":
    # 创建实现类实例（发送方式）
    normal_sender = NormalSender()
    encrypted_sender = EncryptedSender()

    # 创建抽象类实例（消息类型），并关联实现类（桥接）
    email = EmailMessage(normal_sender)
    sms = SmsMessage(encrypted_sender)

    # 发送消息（抽象与实现分离，可独立扩展）
    email.send_message("会议通知：明天9点开会", "user@example.com")
    sms.send_message("验证码：123456", "13812345678")

    # 动态切换实现类（如邮件改用加密发送）
    email.set_implementor(encrypted_sender)
    email.send_message("机密文件，请查收", "admin@company.com")