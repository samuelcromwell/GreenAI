# 🌿 GreenAI — Django Web Application

GreenAI is a Django-based web application focused on sustainability, innovation, and AI-driven solutions. This guide will help you set up the project on your local machine.

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/samuelcromwell/GreenAI.git
cd GreenAI
```

---

### 2. Create a Virtual Environment

We recommend using `venv` to manage your Python dependencies:

```bash
python3 -m venv env
```

---

### 3. Activate the Virtual Environment

- On **Linux/macOS**:
  ```bash
  source env/bin/activate
  ```

- On **Windows**:
  ```cmd
  .\env\Scripts\activate
  ```

---

### 4. Install Dependencies

Make sure you're inside the virtual environment, then run:

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing or outdated, run `pip freeze > requirements.txt` after installing packages manually.

---

### 5. Run Migrations

Before running the server, apply the database migrations:

```bash
python manage.py migrate
```

---

### 6. Run the Development Server

```bash
python manage.py runserver
```

Then open your browser and go to:
```
http://127.0.0.1:8000/
```

---

## 🔐 Admin Panel

To access the Django admin panel, visit:

```
http://127.0.0.1:8000/admin/
```

### ✅ Credentials:

- **Username:** `greenaiadmin`  
- **Password:** `admin123`

If you haven't created the superuser yet, run:

```bash
python manage.py createsuperuser
```

And follow the prompts using the credentials above.

---
## 🧩 Dynamic Admin Content
You can manage and update content dynamically from the Django Admin Dashboard, including:

✅ Blogs

✅ Sustainability Articles

✅ Team Members

✅ FAQs

✅ Products

✅ Solutions

✅ Opportunities

✅ Investors

✅ Case Studies

✅ Whitepapers

✅ Reviews

✅ Subscribers

✅ Feedbacks

✅ Footer Galleries

✅ Initiatives

✅ Contacts

✅ CSR Entries

The Django Admin Panel has been enhanced with Jazzmin to provide a cleaner and more modern UI.

## 📁 Project Structure

```bash
GreenAI/
├── manage.py
├── requirements.txt
├── GreenAI/           
└── website/          
```

---

## 🛠️ Technologies Used

- Django (Python)
- HTML/CSS/JS
- SQLite3 (Default DB)
- Bootstrap / Tailwind (For frontend styling)
- Cloudinary (for image hosting)

---

## 💬 Feedback or Contributions?

Feel free to open issues or contribute via pull requests.

---

© 2025 GreenAI — Built by [Samuel Cromwell Musa](https://github.com/samuelcromwell)

