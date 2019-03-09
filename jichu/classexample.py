class Person:
    # 类变量
    total_person = 0

    # 构造方法
    def __init__(self, name, sex, province):
        print("初始化类")
        # 实例变量
        self.name = name
        self.sex = sex
        self.province = province
        Person.total_person +=1

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_province(self):
        return self.province
