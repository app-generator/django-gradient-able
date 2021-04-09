## How to use it

```bash
$ # Get the code
$ git clone https://github.com/muusfa/CPSC471_Project.git
$ cd CPSC471_project
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />

## Code-base structure

The project is coded using a simple and intuitive structure presented bellow:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app logic and serve the static assets
   |    |-- settings.py                    # Django app bootstrapper
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                  # Master pages
   |         |    |-- base-fullscreen.html # Used by Authentication pages
   |         |    |-- base.html            # Used by common pages
   |         |
   |         |-- accounts/                 # Authentication pages
   |         |    |-- login.html           # Login page
   |         |    |-- register.html        # Register page
   |         |
   |      index.html                       # The default page
   |     page-404.html                     # Error 404 page
   |     page-500.html                     # Error 404 page
   |       *.html                          # All other HTML pages
   |
   |-- authentication/                     # Handles auth routes (login and register)
   |    |
   |    |-- urls.py                        # Define authentication routes  
   |    |-- views.py                       # Handles login and registration  
   |    |-- forms.py                       # Define auth forms  
   |
   |-- app/                                # A simple app that serve HTML files
   |    |
   |    |-- views.py                       # Serve HTML pages for authenticated users
   |    |-- urls.py                        # Define some super simple routes  
   |
   |-- databasescripts/                    # Text files containing stored procedures for the database
   |    |
   |    |-- cartPrice.txt                  # Stored procedure: price of all items in cart
   |    |-- cartProducts.txt               # Stored procedure: all products in cart
   |    |-- cartQuantity.txt               # Stored procedure: total quantity of items in cart
   |    |-- getCategory.txt                # Stored procedure: all categories in database
   |    |-- getProducts.txt                # Stored procedure: all products in a particular category
   |    |-- productColors.txt              # Stored procedure: all possible colors of product
   |    |-- productManufacturer.txt        # Stored procedure: manufacturer of product
   |    |-- productPrice.txt               # Stored procedure: price of product
   |    |-- selectionSubmitted.txt         # Stored procedure: product store, name, description, and manufacturer 
   |
   |-- requirements.txt                    # Development modules - SQLite storage
   |
   |-- .env                                # Inject Configuration via Environment
   |-- manage.py                           # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

> Requirements for using the website

- Ensure you have MYSQL server setup on your computer.
- If you do not have it already installed, follow tutorial at the following link to do so 
- [MYSQL Tutorial](https://www.youtube.com/watch?v=GIRcpjg-3Eg&ab_channel=edureka%21) - Youtube Video
- Now create the database, loging to your MYSQL command line tool
- Create a table called "store_inventory" using the command "CREATE DATABASE store_inventory;"
- [Connecting MYSQL to Django](https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database) - Further Information

<br />

> The bootstrap flow

- Django bootstrapper `manage.py` uses `core/settings.py` as the main configuration file
- `core/settings.py` loads the app magic from `.env` file
- Redirect the guest users to Login page
- Unlock the pages served by *app* node for authenticated users

<br />

## Credits & Links

- [Django](https://www.djangoproject.com/) - The offcial website
- [Boilerplate Code](https://appseed.us/boilerplate-code) - Index provided by **AppSeed**
- [Boilerplate Code](https://github.com/app-generator/boilerplate-code) - Index published on Github

<br />

---
[Django Dashboard](https://appseed.us/admin-dashboards/django?ref=gh) Gradient Able - Provided by **AppSeed [App Generator](https://appseed.us/app-generator)**.
