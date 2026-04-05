```markdown
# 💰 Expense Manager

A sleek and efficient personal finance dashboard built with **Django**. This application helps users track their daily spending, manage fixed expenses, and visualize their financial health through interactive reports.

---

## 🚀 Features

* **Financial Dashboard:** A high-level overview of balances, incomes, and expenses.
* **Interactive Charts:** Visual data representation using **Chart.js** to track spending patterns.
* **Expense Categorization:** Manage different types of costs (fixed bills, investments, and installments).
* **Planning Tools:** Set financial goals and monitor your progress in real-time.
* **Responsive UI:** A modern, mobile-friendly interface built with **Tailwind CSS**.

---

## 🛠 Tech Stack

| Technology | Description |
| --- | --- |
| **Python 3** | Core programming language |
| **Django** | High-level Web Framework |
| **Tailwind CSS** | Utility-first CSS framework for styling |
| **Chart.js** | Flexible JavaScript charting |
| **SQLite** | Lightweight database for development |
| **python-dotenv** | Environment variable management |

---

## 📂 Project Structure

```text
records/
│
├── static/          # Assets (CSS, JS, Favicon)
│   └── records/     # App-specific namespace
├── templates/       # HTML User Interface
│   └── records/     # App-specific namespace
├── models.py        # Database definitions
├── views.py         # Business logic
└── urls.py          # App-specific URL routing
```

---

## ⚙️ How to Run the Project

### 1. Clone the repository
```bash
git clone [https://github.com/your-username/expense-manager.git](https://github.com/your-username/expense-manager.git)
cd expense-manager
```

### 2. Set up Virtual Environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```text
SECRET_KEY=your_secret_key_here
DEBUG=True
```

### 5. Database Setup & Run
```bash
python manage.py migrate
python manage.py runserver
```

---

## 🔐 Security

> **Important:** The `SECRET_KEY` and any sensitive credentials must be stored in environment variables (`.env`). Never version production keys in your public repository.

---

## 📌 Roadmap (Next Steps)

* [ ] **Frontend Interactivity:** Implement HTMX or Alpine.js for seamless UI updates.
* [ ] **Automatic Month Transition:** Logic to auto-detect and filter the current month.
* [ ] **Multi-user Support:** Full authentication system (Sign Up/Login).
* [ ] **Data Export:** Functionality to export financial reports to PDF or Excel.

---

## 👨‍💻 Author

Developed with ☕ by **João Pedro**.
```