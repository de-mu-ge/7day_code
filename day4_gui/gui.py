import json
from tkinter import *
from tkinter import ttk, messagebox

data = []
try:
    f = open('students.json', 'r', encoding='utf-8')
    data = json.load(f)
    f.close()
except Exception:
    pass


def new_id():
    if len(data) == 0:
        return 1
    ids = []
    for x in data:
        ids.append(x['id'])
    return max(ids) + 1


def save():
    f = open('students.json', 'w', encoding='utf-8')
    json.dump(data, f, ensure_ascii=False)
    f.close()


def refresh():
    tree.delete(*tree.get_children())
    for x in data:
        tree.insert('', 'end', values=(x['id'], x['name'], x['age'], x['score']))


def add():
    name = name_var.get()
    age = age_var.get()
    score = score_var.get()
    if name == '' or score == '':
        messagebox.showwarning('提示', '姓名和成绩不能为空')
        return
    data.append({'id': new_id(), 'name': name, 'age': age, 'score': float(score)})
    save()
    refresh()
    clear()


def delete():
    try:
        sel = tree.selection()[0]
        sid = int(tree.item(sel, 'values')[0])
    except Exception:
        messagebox.showwarning('提示', '请先选中一行')
        return
    for x in data:
        if x['id'] == sid:
            data.remove(x)
            break
    save()
    refresh()
    clear()


def update():
    try:
        sel = tree.selection()[0]
        sid = int(tree.item(sel, 'values')[0])
    except Exception:
        messagebox.showwarning('提示', '请先选中一行')
        return
    for x in data:
        if x['id'] == sid:
            x['name'] = name_var.get()
            x['age'] = age_var.get()
            x['score'] = float(score_var.get())
            break
    save()
    refresh()
    clear()


def clear():
    name_var.set('')
    age_var.set('')
    score_var.set('')


def on_select(event):
    try:
        sel = tree.selection()[0]
        v = tree.item(sel, 'values')
        name_var.set(v[1])
        age_var.set(v[2])
        score_var.set(v[3])
    except Exception:
        pass


root = Tk()
root.title('学生信息管理系统')
root.geometry('620x460')

name_var = StringVar()
age_var = StringVar()
score_var = StringVar()

top = Frame(root)
top.pack(pady=10)
Label(top, text='姓名').grid(row=0, column=0)
Label(top, text='年龄').grid(row=0, column=2)
Label(top, text='成绩').grid(row=0, column=4)
Entry(top, textvariable=name_var).grid(row=0, column=1)
Entry(top, textvariable=age_var).grid(row=0, column=3)
Entry(top, textvariable=score_var).grid(row=0, column=5)
Button(top, text='添加', command=add).grid(row=1, column=1, pady=5)
Button(top, text='修改', command=update).grid(row=1, column=3, pady=5)
Button(top, text='删除', command=delete).grid(row=1, column=5, pady=5)

tree = ttk.Treeview(root, columns=('id', 'name', 'age', 'score'), show='headings')
tree.heading('id', text='编号')
tree.heading('name', text='姓名')
tree.heading('age', text='年龄')
tree.heading('score', text='成绩')
tree.column('id', width=80, anchor='center')
tree.column('name', width=150, anchor='center')
tree.column('age', width=100, anchor='center')
tree.column('score', width=100, anchor='center')
tree.pack(fill=BOTH, expand=True, padx=10, pady=10)
tree.bind('<<TreeviewSelect>>', on_select)

refresh()
root.mainloop()
