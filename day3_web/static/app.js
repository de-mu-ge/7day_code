async function loadAll() {
    let r = await fetch('/api');
    let arr = await r.json();
    let box = document.getElementById('list');
    box.innerHTML = '';
    arr.forEach(function (x) {
        let tr = document.createElement('tr');
        tr.innerHTML = '<td>' + x.id + '</td><td>' + x.name + '</td><td>' + x.age + '</td><td>' + x.score
            + '</td><td><button onclick="del(' + x.id + ')">删除</button>'
            + '<button onclick="edit(' + x.id + ')">修改</button></td>';
        box.appendChild(tr);
    });
}

async function add() {
    let name = document.getElementById('name').value;
    let age = document.getElementById('age').value;
    let score = document.getElementById('score').value;
    if (name == '') {
        alert('姓名不能为空');
        return;
    }
    await fetch('/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({name: name, age: age, score: parseFloat(score)})
    });
    clearInput();
    loadAll();
}

async function del(id) {
    await fetch('/api?id=' + id, {method: 'DELETE'});
    loadAll();
}

async function edit(id) {
    let r = await fetch('/api');
    let arr = await r.json();
    arr.forEach(function (x) {
        if (x.id == id) {
            document.getElementById('eid').value = x.id;
            document.getElementById('name').value = x.name;
            document.getElementById('age').value = x.age;
            document.getElementById('score').value = x.score;
        }
    });
}

async function update() {
    let id = parseInt(document.getElementById('eid').value);
    let name = document.getElementById('name').value;
    let age = document.getElementById('age').value;
    let score = document.getElementById('score').value;
    await fetch('/api', {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({id: id, name: name, age: age, score: parseFloat(score)})
    });
    clearInput();
    loadAll();
}

function clearInput() {
    document.getElementById('name').value = '';
    document.getElementById('age').value = '';
    document.getElementById('score').value = '';
    document.getElementById('eid').value = '';
}

loadAll();
