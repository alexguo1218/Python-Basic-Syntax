"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
    1. 添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
        1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
        1.2 检查学生姓名是否已存在, 如果学生不存在, 再添加 (存在则, 不添加)
        1.3 验证成绩范围（0-100分）
        1.4 创建学生对象并添加到系统
    2. 修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
        2.1 输入要修改的学生姓名
        2.2 根据姓名查找该学生, 显示该生当前成绩信息
        2.3 输入新的语文、数学、英语成绩
        2.4 更新学生成绩数据
    3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
    4. 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
        4.1 输出格式为: "姓名：张三 | 语文：85 | 数学：90 | 英语：88 | 总分：263"
    5. 展示全部学生成绩：展示出系统中所有学生的成绩
"""

# 创建学生类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名:{self.name},语文:{self.chinese},数学:{self.math},英语:{self.english},总分:{self.chinese + self.math + self.english}"

    # 修改学生成绩
    def update__score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
            print(f"修改{self.name}的语文成绩成功")
        if math is not None:
            self.math = math
            print(f"修改{self.name}的数学成绩成功")
        if english is not None:
            self.english = english
            print(f"修改{self.name}的英语成绩成功")

# 测试
if __name__ == "__main__":
    s1 = Student("张三", 80, 90, 85)
    print(s1)
    s1.update__score(chinese=100)
    print(s1)

# 创建教务管理系统类
class EduManageSystem:
    system_version = "1.0.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = [] # 列表，记录的是在校学生的成绩
        print(f"{self.system_name}启动成功，当前版本为：{self.system_version}")

    def add_student(self):
        name = input("请输入学生姓名:")

        # 检查学生姓名是否已存在
        for s in self.student_list:
            if s.name == name:
                print(f"{name}已存在,添加失败")
                return

        chinese = int(input("请输入学生语文成绩:"))
        math = int(input("请输入学生数学成绩:"))
        english = int(input("请输入学生英语成绩:"))

        # 验证成绩范围
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, chinese, math, english)
            self.student_list.append(stu)
            print(f"{name}添加成功")
        else:
            print("成绩范围错误")
            return

    # 修改学生成绩
    def update_student(self):
        name = input("请输入要修改的学生姓名:")

        # 判断是否存在该学生
        for s in self.student_list:
            if s.name == name:
                print(f"该学生初试成绩为:{s}")

                chinese = int(input("请输入学生语文成绩:"))
                math = int(input("请输入学生数学成绩:"))
                english = int(input("请输入学生英语成绩:"))

                # 判断成绩范围
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update__score(chinese, math, english)
                    print(f"修改后的成绩为:{s}")
                    return
                else:
                    print("成绩范围错误")
                    return
        print("未找到该学生，请重试...")

    # 删除学生
    def delete_student(self):
        name = input("请输入要删除的学生姓名:")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print(f"{name}删除成功")
                return
        print("未找到该学生，请重试...")

    # 查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询的学生姓名:")
        for s in self.student_list:
            if s.name == name:
                print(s)
                return
        print("未找到该学生，请重试...")

    # 展示全部学生成绩
    def show_all_student(self):
        for s in self.student_list:
            print(s)

    # 运行
    def run(self):
        print(f"欢迎使用教务管理系统 V{EduManageSystem.system_version}")

        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("1. 添加学生成绩    2. 修改学生成绩   3. 删除学生    4. 查询指定学生成绩    5. 展示所有学生成绩   6.退出系统")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")

            choice = input("\n请选择操作(1-6):")
            try:
                match choice:
                    case "1": # 添加学生
                        self.add_student()
                    case "2": # 修改学生
                        self.update_student()
                    case "3": # 删除学生
                        self.delete_student()
                    case "4": # 查询学生
                        self.query_student()
                    case "5": # 展示所有学生
                        self.show_all_student()
                    case "6": # 退出系统
                        print("退出系统")
                        break
                    case _:
                        print("无效的选择，请重新选择")
            except Exception:
                print("程序执行出错，请重试...")


# 测试
if __name__ == "__main__":
    edu_sys = EduManageSystem()
    edu_sys.run()