# 📝 Dynamic Form Builder (Django)

A Django-based web application that allows users to create, preview, and store dynamic form templates with various field types. Users can submit responses, which are stored and displayed in the form details page.

---

## 🚀 Features
- Create dynamic form templates with different field types
- Live preview of forms while creating
- Store form schema as JSON
- Submit responses and store them as JSON
- View submitted responses per form template
- Fully responsive UI with Bootstrap 5

---

## 📌 Setup Instructions

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/RAJKRIS/dynamic_forms.git
cd dynamic_forms
```

### 2️⃣ **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Apply Migrations**
```bash
python manage.py migrate
```

### 5️⃣ **Run the Development Server**
```bash
python manage.py runserver
```
App will be available at **http://127.0.0.1:8000/** 🎉

---

## 🌍 Deployment Instructions (For Production)
1. **Set up a PostgreSQL Database**  
   Update `settings.py` with database credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```
2. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

3. **Collect Static Files**
   ```bash
   python manage.py collectstatic --noinput
   ```

4. **Create a Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run Gunicorn (For Production)**
   ```bash
   gunicorn my_project.wsgi:application --bind 0.0.0.0:8000
   ```

6. **(Optional) Configure Nginx & Gunicorn for Deployment**

---

## 📂 Project Structure
```
/dynamic_forms
│── dynamic_forms/              # Main Django project folder
│── formsapp/                  # Django app containing models, views, templates
│── templates/               # HTML Templates
│── requirements.txt         # Dependencies
│── manage.py                # Django management script
│── README.md                # Documentation
```

---

## 🛠️ Technologies Used
- **Django** (Python Web Framework)
- **Bootstrap 5** (Frontend UI)
- **PostgreSQL** (Database for production)
- **Gunicorn & Nginx** (For deployment)

---

## 🐜 License
This project is licensed under the **MIT License**.

---

## 🤝 Contributing
1. Fork the repository  
2. Create a new branch (`git checkout -b feature-name`)  
3. Commit changes (`git commit -m "Add new feature"`)  
4. Push to GitHub (`git push origin feature-name`)  
5. Open a Pull Request  

---

## 💌 Contact
👤 **RAJKRIS**  
📧 rajesh1993krishnan@gmail.com  
🔗 [GitHub Profile](https://github.com/RAJKRIS)

---
Happy coding! 🚀

