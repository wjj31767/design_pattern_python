"""
日志系统（日志级别 vs 输出目标）
场景描述
设计一个日志系统，支持不同日志级别（调试、信息、错误）和不同输出目标（文件、控制台、数据库），要求两者可自由组合。
抽象与实现分离
"""


class LogLevel:
    def __init__(self, output_target):
        self.output_target = output_target  # 桥接输出目标

    def log(self, message):
        raise NotImplementedError

class DebugLog(LogLevel):
    def log(self, message):
        formatted_msg = f"[DEBUG] {message}"
        self.output_target.write(formatted_msg)


class OutputTarget:
    def write(self, message):
        raise NotImplementedError


class FileOutput(OutputTarget):
    def write(self, message):
        with open("log.txt", "a") as f:
            f.write(message + "\n")


class ConsoleOutput(OutputTarget):
    def write(self, message):
        print(message)
        