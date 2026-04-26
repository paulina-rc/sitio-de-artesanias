# Artesanías del Campo
A full-stack web application for a handcraft shop, built with **Python Flask** and **MySQL**. Browse, manage, and showcase traditional handmade artisan products with a clean and responsive interface.

## Preview
> A web platform where customers can explore handcrafted products, send contact messages, and administrators can manage the entire product and user catalog through a CRUD panel.


## Features

- **Product Catalog** — Browse all artisan products with images, descriptions, categories and prices
- **Contact Form** — Visitors can send messages directly stored in the database
- **Authentication System** — Login with session management and role-based access (Admin / User)
- **Product CRUD** — Add, edit, and delete products with image upload support
- **User Management** — Admin panel to create and manage users with active/inactive status
- **Responsive Design** — Built with Bootstrap 5 for mobile-friendly layouts


## Project Structure

```
sitio-de-artesanias/
│
├── controllers/
│   ├── __init__.py
│   ├── db.py                  # Database connection
│   └── productos_controller.py # Product data layer
│
├── static/
│   ├── css/
│   │   └── style.css          # Custom styles
│   └── img/                   # Product images
│
├── templates/
│   ├── base.html              # Base layout with navbar & footer
│   ├── inicio.html            # Home page
│   ├── productos.html         # Product catalog
│   ├── contactenos.html       # Contact form
│   ├── crud.html              # Product management panel
│   ├── editar.html            # Edit product form
│   ├── usuarios.html          # User management panel
│   └── login.html             # Login page
│
└── main.py                    # Flask app & all routes
```

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3 + Flask |
| Database | MySQL |
| Frontend | HTML5, Bootstrap 5, CSS3 |
| Templating | Jinja2 |
| DB Connector | mysql-connector-python |

## Setup & Installation

### Prerequisites
- Python 3.8+
- MySQL Server
- pip

### 1. Clone the repository
```bash
git clone https://github.com/paulina-rc/sitio-de-artesanias.git
cd sitio-de-artesanias
```

### 2. Install dependencies
```bash
pip install flask mysql-connector-python
```

### 3. Set up the database
Create a MySQL database called `artesanias` and run the following SQL:
```sql
CREATE DATABASE artesanias;
USE artesanias;

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT,
    precio INT,
    categoria VARCHAR(50),
    imagen VARCHAR(100)
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    usuario VARCHAR(50),
    password VARCHAR(100),
    tipo INT,       -- 1 = Admin, 2 = User
    estado INT      -- 1 = Active, 0 = Inactive
);

CREATE TABLE mensajes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    mensaje TEXT
);
```

### 4. Configure the database connection
Edit `controllers/db.py` with your MySQL credentials:
```python
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="artesanias"
    )
```

### 5. Run the app
```bash
python main.py
```
Visit `http://127.0.0.1:5000` in your browser.

## Default Admin Access

To log in as admin, insert a user manually in the database:
```sql
INSERT INTO usuarios (nombre, usuario, password, tipo, estado)
VALUES ('Admin', 'admin', 'admin123', 1, 1);
```
Then go to `/login` and use those credentials.

## Routes Overview

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page |
| `/productos` | GET | Product catalog |
| `/contactenos` | GET, POST | Contact form |
| `/login` | GET, POST | Login |
| `/crud` | GET | Product management |
| `/agregar` | POST | Add new product |
| `/editar/<id>` | GET | Edit product form |
| `/actualizar/<id>` | POST | Update product |
| `/eliminar/<id>` | GET | Delete product |
| `/crud_usuarios` | GET | User management (Admin only) |
| `/agregar_usuario` | POST | Add new user |


## Author
**Paulina Rojas** — [@paulina-rc](https://github.com/paulina-rc)
