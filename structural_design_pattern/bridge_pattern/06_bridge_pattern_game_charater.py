"""
游戏角色系统（角色类型 vs 技能体系）
场景描述
设计游戏角色，角色类型（战士、法师、刺客）和技能体系（物理技能、魔法技能、暗杀技能）可独立扩展，支持动态组合技能。
抽象与实现分离
抽象部分（角色类型）：定义 Character 抽象类，包含攻击逻辑，持有技能体系的引用。
"""


class Character:
    def __init__(self, skill_system):
        self.skill_system = skill_system  # 桥接技能体系

    def attack(self):
        raise NotImplementedError


class Warrior(Character):
    def attack(self):
        print("战士发起攻击：", end="")
        self.skill_system.use_physical_skill()


class SkillSystem:
    def use_physical_skill(self):
        raise NotImplementedError

    def use_magic_skill(self):
        raise NotImplementedError


class PhysicalSkillSystem(SkillSystem):
    def use_physical_skill(self):
        print("使用物理技能：挥砍")

    def use_magic_skill(self):
        print("物理角色无法使用魔法技能")
