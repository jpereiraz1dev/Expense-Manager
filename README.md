💰 Expense Manager
A sleek and efficient personal finance dashboard built with Django. This application helps users track their daily spending, manage fixed expenses, and visualize their financial health through interactive reports.

🚀 Features
- Financial Dashboard: A high-level overview of your balances, incomes, and expenses.

- Interactive Charts: Visual data representation using Chart.js to track spending patterns.

- Expense Categorization: Manage different types of costs, including fixed bills, investments, and installments.

- Planning Tools: Set financial goals and monitor your progress.

- Responsive UI: A modern, mobile-friendly interface built with Tailwind CSS.

🛠️ Tech Stack
- Backend: Django (Python)- 

- Frontend: Tailwind CSS & JavaScript 

- Data Visualization: Chart.js

- Environment Management: python-dotenv (for security)

- Database: SQLite (Development) / PostgreSQL (Optional)

🔧 Installation & Setup
Clone the repository:

Bash
git clone https://github.com/your-username/expense-manager.git
cd expense-manager
Create and activate a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Set up Environment Variables:
Create a .env file in the root directory and add your SECRET_KEY and DEBUG status:

Plaintext
SECRET_KEY=your_secret_key_here
DEBUG=True
Run migrations and start the server:

Bash
python manage.py migrate
python manage.py runserver

🗺️ Roadmap (Next Steps)
This project is currently under active development. Here are the planned features and improvements:

- Frontend Interactivity: Implement HTMX or Alpine.js to make all buttons and forms interactive without full page reloads.

- Automatic Month Transition: Develop logic to automatically detect the current month and filter expenses/reports accordingly.

- Multi-user Support: Implement a full Authentication System (Sign Up/Login) so multiple users can manage their own private finances securely.

- Data Export: Add functionality to export reports to PDF or Excel.

📝 License
This project is licensed under the MIT License.

