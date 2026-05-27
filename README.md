# Gallery Web Application

A simple Django web application with user authentication (login/registration) and three gallery pages displaying cars, flowers, and animals images. This app is designed to be deployed on Microsoft Azure App Service (free tier).

## Features

- User Registration & Login
- Three Gallery Pages:
  - Cars Gallery
  - Flowers Gallery
  - Animals Gallery
- Responsive Design
- Django Admin Integration
- Azure-Ready Configuration

## Local Development

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. **Clone or download this repository**

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Adding Images

1. Log in to the Django admin panel at `/admin/`
2. Navigate to the appropriate gallery section (Cars, Flowers, or Animals)
3. Click "Add" to upload new images with titles and descriptions

## Deploying to Azure App Service (Free Tier)

### Prerequisites

- Azure Account (free tier available)
- Azure CLI installed
- Git installed

### Step-by-Step Deployment

#### 1. Prepare Your Code

Make sure your code is in a Git repository:

```bash
git init
git add .
git commit -m "Initial commit"
```

#### 2. Create Azure Web App

```bash
# Login to Azure
az login

# Create a resource group
az group create --name gallery-rg --location eastus

# Create an App Service plan (Free tier)
az appservice plan create --name gallery-plan --resource-group gallery-rg --sku F1 --is-linux

# Create a web app
az webapp up --resource-group gallery-rg --plan gallery-plan --name your-unique-app-name --runtime "PYTHON|3.9"
```

Replace `your-unique-app-name` with a unique name for your app.

#### 3. Configure Application Settings

```bash
# Set the startup command
az webapp config appsettings set --resource-group gallery-rg --name your-unique-app-name --settings WEBSITE_HTTPLOGGING_RETENTION_DAYS=1

# Set Django settings
az webapp config appsettings set --resource-group gallery-rg --name your-unique-app-name --settings DJANGO_SETTINGS_MODULE=car_flower_animal_app.settings

# Generate a secret key and set it
az webapp config appsettings set --resource-group gallery-rg --name your-unique-app-name --settings SECRET_KEY="your-generated-secret-key-here"

# Set DEBUG to False for production
az webapp config appsettings set --resource-group gallery-rg --name your-unique-app-name --settings DEBUG=False

# Set allowed hosts
az webapp config appsettings set --resource-group gallery-rg --name your-unique-app-name --settings ALLOWED_HOSTS=your-unique-app-name.azurewebsites.net,your-unique-app-name.azurewebsites.net
```

#### 4. Deploy Your Code

```bash
# Configure Git deployment
az webapp deployment source config-local-git --resource-group gallery-rg --name your-unique-app-name

# Add Azure as a remote
git remote add azure <git-url-from-previous-command>

# Deploy
git push azure main
```

#### 5. Run Migrations on Azure

After deployment, access the Kudu console:
- Go to: `https://your-unique-app-name.scm.azurewebsites.net/webssh/host`
- Run: `python manage.py migrate`

#### 6. Create Superuser on Azure

In the same Kudu console:
```bash
python manage.py createsuperuser
```

### Accessing Your Deployed App

- Main application: `https://your-unique-app-name.azurewebsites.net/`
- Admin panel: `https://your-unique-app-name.azurewebsites.net/admin/`

## Project Structure

```
New App/
├── car_flower_animal_app/     # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py             # Main settings file
│   ├── urls.py                 # Main URL configuration
│   └── wsgi.py
├── gallery/                    # Main application
│   ├── migrations/
│   ├── templates/
│   │   └── gallery/
│   │       ├── base.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── home.html
│   │       ├── cars.html
│   │       ├── flowers.html
│   │       └── animals.html
│   ├── __init__.py
│   ├── admin.py                # Admin configuration
│   ├── apps.py
│   ├── models.py               # Database models
│   ├── urls.py                 # App URL configuration
│   └── views.py                # View functions
├── static/                     # Static files (CSS, JS)
├── media/                      # User-uploaded images
├── venv/                       # Virtual environment
├── .gitignore
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version for Azure
└── README.md                   # This file
```

## Technologies Used

- **Django 4.2.30** - Web framework
- **Pillow 11.3.0** - Image processing library
- **WhiteNoise 6.6.0** - Static file serving
- **Gunicorn 20.1.0** - WSGI HTTP Server
- **dj-database-url 2.1.0** - Database URL configuration

## License

This project is open source and available for educational purposes.

## Support

For any issues or questions, please refer to the Django documentation or Azure App Service documentation.