from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'secret'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = ['myapp']
MIDDLEWARE = ['django.middleware.csrf.CsrfViewMiddleware']
ROOT_URLCONF = 'myproject.urls'
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'], 'APP_DIRS': True,
    'OPTIONS': {'context_processors': ['django.template.context_processors.request']}}]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
