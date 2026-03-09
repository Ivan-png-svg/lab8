const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const app = express();

app.use(express.json());

const db = new sqlite3.Database('./language_school.db', (err) => {
    if (err) console.error("Помилка підключення:", err.message);
    else console.log("База даних підключена! Всі таблиці з 1-ї лаби доступні.");
});

app.get('/students', (req, res) => {
    db.all("SELECT * FROM students", [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(rows);
    });
});

app.get('/schedule', (req, res) => {
    const sql = `
        SELECT s.lesson_time, g.group_name, t.full_name 
        FROM schedule s
        JOIN groups_list g ON s.group_id = g.group_id
        JOIN teachers t ON s.teacher_id = t.teacher_id`;
    db.all(sql, [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(rows);
    });
});

app.post('/students', (req, res) => {
    const { first_name, last_name, group_id } = req.body;
    const sql = 'INSERT INTO students (first_name, last_name, group_id) VALUES (?, ?, ?)';
    db.run(sql, [first_name, last_name, group_id], function(err) {
        if (err) return res.status(400).json({ error: err.message });
        res.json({ id: this.lastID, message: "Студента додано успішно!" });
    });
});

app.put('/students/:id', (req, res) => {
    const student_id = req.params.id;
    const { first_name, last_name, group_id } = req.body;
    
    console.log("Отримані дані:", first_name, last_name, group_id, "для ID:", student_id);

    const sql = "UPDATE students SET first_name = ?, last_name = ?, group_id = ? WHERE student_id = ?";
    
    db.run(sql, [first_name, last_name, group_id, student_id], function(err) {
        if (err) {
            console.error("Помилка SQL:", err.message); 
            return res.status(500).json({ error: err.message });
        }
        console.log("Кількість змінених рядків:", this.changes); 
        if (this.changes === 0) {
            return res.status(404).json({ message: "Студента з таким ID не існує!" });
        }
        res.json({ message: "Успішно оновлено!" });
    });
});

app.delete('/students/:id', (req, res) => {
    const studentId = req.params.id;
    
    const sql = "DELETE FROM students WHERE student_id = ?";
    
    db.run(sql, studentId, function(err) {
        if (err) return res.status(500).json({ error: err.message });
        res.json({ message: "Студента видалено!" });
    });
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Сервер працює на http://localhost:${PORT}`);
    console.log(`Перевір студентів: http://localhost:${PORT}/students`);
    console.log(`Перевір розклад: http://localhost:${PORT}/schedule`);
});