const API = "http://127.0.0.1:5000/tasks";

async function loadTasks() {
    const res = await fetch(API);
    const tasks = await res.json();

    const list = document.getElementById("taskList");
    list.innerHTML = "";

    tasks.forEach(task => {
        const li = document.createElement("li");
        li.innerHTML = `
            ${task.title} 
            <button onclick="deleteTask(${task.id})">X</button>
        `;
        list.appendChild(li);
    });
}

async function addTask() {
    const input = document.getElementById("taskInput");
    
    await fetch(API, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ title: input.value })
    });

    input.value = "";
    loadTasks();
}

async function deleteTask(id) {
    await fetch(`${API}/${id}`, {
        method: "DELETE"
    });

    loadTasks();
}

loadTasks();