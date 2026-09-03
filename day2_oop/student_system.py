import json


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def show(self):
        print(self.name, self.age, self.score)


class StudentManager:
    def __init__(self):
        self.students = []
        self.load()

    def load(self):
        try:
            f = open('students.json', 'r', encoding='utf-8')
            data = json.load(f)
            for x in data:
                s = Student(x['name'], x['age'], x['score'])
                self.students.append(s)
            f.close()
        except Exception:
            pass

    def save(self):
        data = []
        for s in self.students:
            data.append({'name': s.name, 'age': s.age, 'score': s.score})
        f = open('students.json', 'w', encoding='utf-8')
        json.dump(data, f, ensure_ascii=False)
        f.close()

    def menu(self):
        print('1 添加 2 删除 3 修改 4 按姓名查找')
        print('5 显示全部 6 按成绩排序 7 统计 0 退出')

    def add(self):
        name = input('姓名：')
        age = input('年龄：')
        score = float(input('成绩：'))
        self.students.append(Student(name, age, score))
        print('添加成功')

    def delete(self):
        name = input('要删除的姓名：')
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                print('删除成功')
                return
        print('找不到')

    def update(self):
        name = input('要修改的姓名：')
        for s in self.students:
            if s.name == name:
                s.age = input('新的年龄：')
                s.score = float(input('新的成绩：'))
                print('修改成功')
                return
        print('找不到')

    def find(self):
        name = input('要查找的姓名：')
        for s in self.students:
            if s.name == name:
                s.show()
                return
        print('找不到')

    def show_all(self):
        if len(self.students) == 0:
            print('没有学生')
            return
        for s in self.students:
            s.show()

    def sort_score(self):
        for i in range(len(self.students)):
            for j in range(i + 1, len(self.students)):
                if self.students[i].score < self.students[j].score:
                    self.students[i], self.students[j] = self.students[j], self.students[i]
        self.show_all()

    def tongji(self):
        if len(self.students) == 0:
            print('没有学生')
            return
        ssum = 0
        count = 0
        for s in self.students:
            ssum += s.score
            if s.score >= 60:
                count += 1
        print('人数', len(self.students))
        print('平均分', round(ssum / len(self.students), 2))
        print('及格率', round(count / len(self.students) * 100, 2), '%')

    def run(self):
        while True:
            self.menu()
            x = input('请选择：')
            if x == '1':
                self.add()
                self.save()
            elif x == '2':
                self.delete()
                self.save()
            elif x == '3':
                self.update()
                self.save()
            elif x == '4':
                self.find()
            elif x == '5':
                self.show_all()
            elif x == '6':
                self.sort_score()
            elif x == '7':
                self.tongji()
            elif x == '0':
                print('拜拜')
                break
            else:
                print('输入错误')


m = StudentManager()
m.run()
