# Photo Gallery Application


## Quick Start - Django backend

Setup Python env and fetch dependencies
```shell script
cd backend
python -m venv env
env\scripts\activate # Windows
. env/bin/activate # MAC or Linux 
pip install -r requirements.txt
```

Prepare database structure
```shell script
python manage.py makemigrations
python manage.py migrate
```

Init data
```shell script
python manage.py loaddata initial_role_data.json
```

Start server
```shell script
python manage.py runserver
```


## Quick Start - Vue.js Frontend

Setup
```shell script
cd frontend
npm install
```

Run
```shell script
npm run serve -- --port 3000
```