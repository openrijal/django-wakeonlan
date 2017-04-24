# Introduction
This is a wakeonlan app on django. Uses wakeonlan python package and custom user model in django for storing mac addresses.

# Requirements
The assumptions are that the machine you are trying to turn on should have wakeonlan feature enabled. It is a BIOS feature, so things will be different for different types of system. Google for your system and enable it.

# Installation
## Install pip
```bash
curl https://bootstrap.pypa.io/get-pip.py | python -
```

## Install virtualenv for virtual environment setup for the app
```bash
pip install virtualenv
```

## Create the virtual env
```bash
mkdir lanwaker
cd lanwaker
virtualenv env
```

## Clone the Repo
```bash
git clone https://github.com/crackjack/django-wakeonlan.git app
```

## Activate the environment and install requirements
```bash
source env/bin/activate
cd app
pip install -r requirements.txt
```

## Django is ready to use, run the migration
```bash
python manage.py migrate
```

## Create the superuser to add users and machines
```bash
python manage.py createsuperuser
```

## Finally you are ready to run the UI
```bash
python manage.py runserver
```

Point your browser to http://127.0.0.1:8000/ and enjoy.
Admin URL: http://127.0.0.1:8000/~admin/


