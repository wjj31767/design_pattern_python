"""
享元模式（Flyweight Pattern）是一种结构型设计模式，它通过共享对象来减少内存使用和提高性能。该模式旨在通过复用现有的对象，而不是每次需要时都创建新对象，从而减少系统中对象的数量。享元模式将对象的状态分为内部状态和外部状态：
内部状态：存储在享元对象内部，并且不会随环境改变而改变的状态，它可以被多个享元对象共享。
外部状态：随环境改变而改变，不能被共享的状态，它通常由客户端在使用享元对象时传入。
"""


# 享元类
class Website:
    def __init__(self, site_type):
        self.site_type = site_type

    def use(self, user):
        print(f"User {user} is using a {self.site_type} website.")


# 享元工厂类
class WebsiteFactory:
    def __init__(self):
        self.websites = {}

    def get_website(self, site_type):
        if site_type not in self.websites:
            self.websites[site_type] = Website(site_type)
        return self.websites[site_type]


# 客户端代码
if __name__ == "__main__":
    factory = WebsiteFactory()

    news_site1 = factory.get_website("news")
    news_site1.use("Alice")

    news_site2 = factory.get_website("news")
    news_site2.use("Bob")

    blog_site = factory.get_website("blog")
    blog_site.use("Charlie")
