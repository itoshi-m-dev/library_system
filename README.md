# 📚 Library Management System

This is a simple Python project that simulates a library system. It allows employees to register books and users to borrow and return them, with all actions being logged automatically.

## 📂 What's in this project?

- `main.py` – Contains the logic for users, employees, and book operations.
- `log_biblioteca.txt` – A log file that records all actions performed in the system.

## ✅ What can you do?

- Employees can add (and remove) books.
- Users can borrow and return books.
- The system logs every interaction into a `.txt` file.

## 🧱 How it works

Main components of the system:

- `Livro` (Book): Holds info about the title, author, and availability.
- `Usuario` (User): Can borrow or return books.
- `Funcionario` (Employee): Can add and manage books.
- `LogFileMixin`: Handles logging messages to a text file.
- `OperacoesBiblioteca`: An abstract class that enforces book operations for users.

## 🧪 Example usage

```python
func = Funcionario('Joao','1234')
livro1 = func.cadastrar_livro('Princesa e o sapo','Emanuel',2025)

usuario = Usuario('Ana')
usuario.pegar_livro(livro1)
usuario.devolver_livro(livro1)
```

All actions above are recorded in the `log_biblioteca.txt` file.

## 💡 Possible improvements

- Add `__str__` methods to improve log readability.
- Implement checks before removing books.
- Build a web or GUI interface for user interaction.
- Store data in a database instead of memory and plain text.

---

### 👨‍💻 Created by Emanuel Pinheiro de Freitas Mellina

---
