💰 Expense ManagerA sleek and efficient personal finance dashboard built with Django. This application helps users track their daily spending, manage fixed expenses, and visualize their financial health through interactive reports.🚀 FeaturesFinancial Dashboard: A high-level overview of balances, incomes, and expenses.Interactive Charts: Visual data representation using Chart.js to track spending patterns.Expense Categorization: Manage different types of costs (fixed bills, investments, and installments).Planning Tools: Set financial goals and monitor your progress in real-time.Responsive UI: A modern, mobile-friendly interface built with Tailwind CSS.🛠 Tech StackTechnologyDescriptionPython 3Core programming languageDjangoHigh-level Web FrameworkTailwind CSSUtility-first CSS framework for stylingChart.jsFlexible JavaScript charting for designers & developersSQLiteLightweight database for developmentpython-dotenvEnvironment variable management for security📂 Project StructureA simplified view of the main application files:Plaintextrecords/
│
├── static/          # Assets (CSS, JS, Favicon)
│   └── records/     # App-specific namespace
├── templates/       # HTML User Interface
│   └── records/     # App-specific namespace
├── models.py        # Database definitions (Expenses, Category)
├── views.py         # Business logic and route control
└── urls.py          # App-specific URL routing
⚙️ How to Run the ProjectFollow the steps below to set up the environment locally:1. Clone the repositoryBashgit clone https://github.com/your-username/expense-manager.git
cd expense-manager
2. Set up Virtual EnvironmentWindows:Bashpython -m venv venv
venv\Scripts\activate
Linux/Mac:Bashpython3 -m venv venv
source venv/bin/activate
3. Install DependenciesBashpip install -r requirements.txt
4. Configure Environment VariablesCreate a .env file in the root directory:PlaintextSECRET_KEY=your_secret_key_here
DEBUG=True
5. Database Setup & RunBashpython manage.py migrate
python manage.py runserver
The project will be available at http://127.0.0.1:8000.🔐 SecurityImportant: The SECRET_KEY and any sensitive credentials must be stored in environment variables (.env). Never version production keys in your public repository.📌 Roadmap (Next Steps)[ ] Frontend Interactivity: Implement HTMX or Alpine.js for seamless UI updates.[ ] Automatic Month Transition: Logic to auto-detect and filter the current month.[ ] Multi-user Support: Full authentication system (Sign Up/Login).[ ] Data Export: Functionality to export financial reports to PDF or Excel.[ ] Responsive UI: Further UX improvements for mobile devices.👨‍💻 AuthorDeveloped with ☕ by João Pedro.