import json

stu = []


def load():
    try:
        f = open('students.json', 'r', encoding='utf-8')
        data = json.load(f)
        f.close()
        return data
    except Exception:
        return []


def save():
    f = open('students.json', 'w', encoding='utf-8')
    json.dump(stu, f, ensure_ascii=False, indent=2)
    f.close()


def menu():
    print('====================')
    print('学生信息管理系统')
    print('1 添加学生')
    print('2 删除学生')
    print('3 修改学生')
    print('4 查找学生')
    print('5 显示全部')
    print('6 按成绩排序')
    print('7 统计信息')
    print('0 退出系统')
    print('====================')


def add():
    name = input('请输入姓名：')
    age = input('请输入年龄：')
    score = float(input('请输入成绩：'))
    s = {}
    s['name'] = name
    s['age'] = age
    s['score'] = score
    stu.append(s)
    print('添加成功')


def dele():
    name = input('请输入要删除的姓名：')
    for i in range(len(stu)):
        if stu[i]['name'] == name:
            del stu[i]
            print('删除成功')
            return
    print('没有找到这个学生')


def update():
    name = input('请输入要修改的姓名：')
    for i in range(len(stu)):
        if stu[i]['name'] == name:
            stu[i]['age'] = input('新的年龄：')
            stu[i]['score'] = float(input('新的成绩：'))
            print('修改成功')
            return
    print('没有找到这个学生')


def find():
    name = input('请输入要查找的姓名：')
    for s in stu:
        if s['name'] == name:
            print(s)
            return
    print('没有找到这个学生')


def show():
    if len(stu) == 0:
        print('还没有学生')
        return
    for s in stu:
        print(s['name'], s['age'], s['score'])


def paixu():
    n = len(stu)
    for i in range(n):
        for j in range(i + 1, n):
            if stu[i]['score'] < stu[j]['score']:
                stu[i], stu[j] = stu[j], stu[i]
    show()


def tongji():
    if len(stu) == 0:
        print('还没有学生')
        return
    total = 0
    jige = 0
    for s in stu:
        total = total + s['score']
        if s['score'] >= 60:
            jige = jige + 1
    avg = total / len(stu)
    print('总人数', len(stu))
    print('平均分', round(avg, 2))
    print('及格率', round(jige / len(stu) * 100, 2), '%')


stu = load()
while True:
    menu()
    choice = input('请输入你的选择：')
    if choice == '1':
        add()
        save()
    elif choice == '2':
        dele()
        save()
    elif choice == '3':
        update()
        save()
    elif choice == '4':
        find()
    elif choice == '5':
        show()
    elif choice == '6':
        paixu()
    elif choice == '7':
        tongji()
    elif choice == '0':
        print('谢谢使用')
        break
    else:
        print('输入有误，请重新输入')
