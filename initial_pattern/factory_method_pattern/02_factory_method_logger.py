"""
这个实现完整展示了工厂方法模式在日志系统中的应用：
核心结构：
抽象产品（Logger）
定义所有日志记录器的统一接口log，包含日志消息和日志级别参数
具体产品
FileLogger：将日志写入文件，包含文件路径属性和文件写入逻辑
ConsoleLogger：在控制台输出日志，包含时间戳格式化逻辑
DatabaseLogger：模拟数据库日志存储（实际可扩展为真实数据库操作）
抽象工厂（LoggerFactory）
声明创建日志记录器的接口create_logger，隔离具体创建逻辑
具体工厂
FileLoggerFactory：根据文件路径创建文件日志器
ConsoleLoggerFactory：创建控制台日志器
DatabaseLoggerFactory：创建数据库日志器
模式优势：
解耦对象创建：客户端无需知道具体日志器的创建细节，只需与抽象工厂和抽象日志器交互
易于扩展：新增日志类型（如 EmailLogger）时，只需添加新的具体产品和具体工厂，无需修改现有代码
统一管理：通过工厂类集中管理日志器创建，方便添加日志器初始化参数（如文件路径、数据库配置）
扩展建议：
可以添加日志级别枚举类（如 DEBUG/INFO/ERROR）提高类型安全性
在抽象日志器中添加set_level方法实现日志级别过滤
为数据库日志器添加真实的数据库连接池和 SQL 执行逻辑
通过配置文件（如 JSON/YAML）动态指定日志类型和参数，实现更灵活的日志系统配置
"""
from abc import ABC, abstractmethod
import time


# --------------------- 抽象产品（Logger） ---------------------
class Logger(ABC):
    """日志记录器抽象类"""

    @abstractmethod
    def log(self, message: str, level: str = "INFO") -> None:
        """记录日志的抽象方法"""
        pass


# --------------------- 具体产品（Concrete Loggers） ---------------------
class FileLogger(Logger):
    """文件日志记录器"""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def log(self, message: str, level: str = "INFO"):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(self.file_path, "a") as f:
            f.write(f"[{timestamp}] [{level}] {message}\n")
        print(f"文件日志已记录: {message}")


class ConsoleLogger(Logger):
    """控制台日志记录器"""

    def log(self, message: str, level: str = "INFO"):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level}] {message}")


class DatabaseLogger(Logger):
    """数据库日志记录器（模拟实现）"""

    def log(self, message: str, level: str = "INFO"):
        print(f"数据库日志已写入（模拟）: [{level}] {message}")
        # 实际应用中会包含数据库连接和插入操作


# --------------------- 抽象工厂（LoggerFactory） ---------------------
class LoggerFactory(ABC):
    """日志工厂抽象类"""

    @abstractmethod
    def create_logger(self) -> Logger:
        """创建日志记录器的抽象方法"""
        pass


# --------------------- 具体工厂（Concrete Factories） ---------------------
class FileLoggerFactory(LoggerFactory):
    """文件日志工厂"""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def create_logger(self) -> FileLogger:
        return FileLogger(self.file_path)


class ConsoleLoggerFactory(LoggerFactory):
    """控制台日志工厂"""

    def create_logger(self) -> ConsoleLogger:
        return ConsoleLogger()


class DatabaseLoggerFactory(LoggerFactory):
    """数据库日志工厂"""

    def create_logger(self) -> DatabaseLogger:
        return DatabaseLogger()


# --------------------- 客户端使用 ---------------------
if __name__ == "__main__":
    # 创建文件日志器（指定日志文件路径）
    file_factory = FileLoggerFactory("app.log")
    file_logger = file_factory.create_logger()
    file_logger.log("应用启动", "INFO")
    file_logger.log("连接数据库失败", "ERROR")

    # 创建控制台日志器
    console_factory = ConsoleLoggerFactory()
    console_logger = console_factory.create_logger()
    console_logger.log("用户登录成功", "INFO")
    console_logger.log("请求参数校验失败", "WARN")

    # 创建数据库日志器
    db_factory = DatabaseLoggerFactory()
    db_logger = db_factory.create_logger()
    db_logger.log("订单数据已提交", "INFO")
