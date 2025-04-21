"""
懒汉式
懒汉式是在第一次使用时才创建单例实例，实现了延迟加载。但在多线程环境下需要进行同步处理，以确保线程安全。示例代码如下：
"""
import threading
class Singleton:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
            return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)