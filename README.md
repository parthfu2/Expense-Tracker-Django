
Expense Tracker Django
This is a simple expense tracker application built with Django. It allows users to track their expenses, categorize them, and view summaries of their spending.




Features
Expense Management: Users can add, edit, and delete their expenses with details like amount, date, and category.
Categories: Users can categorize their expenses (e.g., Food, Entertainment, Bills, etc.).
Expense Summary: Provides users with a summary of their expenses over a chosen period.
Data Persistence: Data is stored in a database, and users can view past entries.
Requirements
Python 3.x
Django 5
MySQL (xampp)
Bootstrap (for frontend styling)



Installation
Clone the repository:

git clone https://github.com/parthfu2/Expense-Tracker-Django.git
cd Expense-Tracker-Django



Install the required dependencies:

It is recommended to use a virtual environment.
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt



Set up the database:
python manage.py migrate
Create a superuser (optional, for admin access):

python manage.py createsuperuser
Run the development server:

python manage.py runserver
Visit http://127.0.0.1:8000 in your browser to access the app.



Usage
Add Expenses: After logging in, you can add your expenses by specifying the amount, date, and category.
View Expenses: You can view a list of all your expenses and make edits or deletions.
View Summary: See your spending overview across different categories and time periods.




Project Structure

expense_tracker/: Main app where expenses are managed.
templates/: HTML templates for rendering pages.
static/: Static files like CSS, JS, and images.
urls.py: URL routing for the application.
