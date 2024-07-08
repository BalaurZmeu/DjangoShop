# DjangoShop

#### 1. Create a virtual environment. (Recommended)
After downloading the files on your computer, open the terminal and navigate to the DjangoShop-main directory.
Run the following command to create a virtual environment in this directory:
```bash
python -m venv venv
```
Run this command to activate the created virtual environment:
```bash
source venv/bin/activate
```

#### 2. Install the dependencies.
```bash
pip install -r requirements.txt
```

#### 3. Create a database.
Navigate to `DjangoShop-main/django_shop`
Run this command to create a database:
```bash
python manage.py migrate
```

#### 4. Create superuser to access the admin page.
Create superuser using this command:
```bash
python manage.py createsuperuser
```
Enter a name and a password.

#### 5. Run the development server.
```bash
python manage.py runserver 8080
```
Then open your browser and enter the address `localhost:8080`
You can also access the admin page `localhost:8080/admin`
