# Installation

#### step 1: create virtual environment (a box)
> `python -m venv myvenv`

#### step 2: activate environment (open box)
> `myvenv/scripts/activate`

#### step 3: install django
> `pip install django`
<!--OR-->
> `python -m pip install django` "-m" is for module

*Note: Check if it's installed*
> `django-admin --version`

# Create project (Setup Hospital)

## Create django project:
> `django-admin startproject mysite .`

*Note: here "full stop" is telling django to create project right here on this path.*

## Run project to check if everything is working correctlty:
> `python manage.py runserver`

- #### IMP files: settings (add new applications) and urls (connect urls and webpages)

# Create applications (Create department in Hospital)

#### An app is a web application that has a specific meaning in your project, like a home page, a contact form, or a members database.

> `python manage.py startapp app_name`

*After creating application we have to add it to "mysite > settings.py > installed_apps", so django and other applications can know about new application.*

- #### IMP files: views (display UI), models (handles database and it's shape), admin (CRUD UI of all models), migrations (logs of database changes)



# MVT (MODEL-VIEW-TEMPLATE)

## Views (django send request object throught url.py to views and they render associated template)

#### Types of Django Views:
1) **Function-based View (FBVs):** user sends url input (http request) and django calls function to render template to user.
> `def functio_name(parameter):  */statements to run/* return`

2) **Class-based View (CBVs):** user sends url input (http request) and django calls class to render template to user.
> `class classNameView(View_type):  */statement to run/*`
- Note: class name should always end with "View".

#### When to choose what?
> You should choose Function-Based Views (FBVs) when you need complete control over custom, non-standard workflow logic, and Class-Based Views (CBVs) when your logic maps directly to common CRUD operations (ListView, CreateView, etc) or benefits from object-oriented reusability.


#### CRUD Views (Built-in Generic Class-Based Views): practice this with student data management project
1) Create: CreateView - Renders a form, validates it, and saves a new record
2) Read: DetailedView (single object) - Displays a detailed page for a single record, ListView (many object) - Displays a list of database records
3) Update: UpdateView - Renders a form to edit and save an existing record
4) Delete: DeleteView

## Templates (receive data from Views and render templates to user, it uses DTL-Django Template Language)

#### Create Template folder
> Create "templates" folder inside application and put HTML files there. Views will find these templates automatically from this folder.

- **Variables**: blank spaces in template that gets filled by real data using DTL
> `{{ variableName }}` # Data is passed from views to template variables

- **tags**: it's used for adding logic like contional or looping
> `{% tags %}` # We have to close tags with endif or endfor.

- **filters**: change the appereance of data by appling filters
> `{{ variable_name | filter_name }}`
<!-- EX. -->
> `{{ variable_name | upper }}`
> `{{ variable_name | date:"d m y" }}`

- **Templates Inheritance**: other templates inherits everything from base template
1) In base template create this. (Note: content is block's name here)
> `{% block content %}`
> Your Statements
> `{% endblock %}`
2) In other template extend it. (At the top of the page)
> `{% extends "base.html" %}`
> `{% block content %}`
> Your Statement
> `{% endblock %}`

- **Static Files** (CSS, JavaScript, Images): to add a static file do this.
1) At the top of the template page load static first.
> `{% load static %}`
2) Then in head tag link it.
> `<link rel="stylesheet" href="{% static 'file_path' %}">`

##### Note: remember to restart server after creating new template or application.


## Model (query data from database and sends Object Relation Mapping to View)

#### In Django, model (blueprint of a table structure which is going to be used to store data in DB) is a python class that describes the type of data which we wanna store in column. for example, we will create one model for invoices, one for customers, one for payments and every model is descibed as table in DB & every field will be a column. After model is described we have to run a command to actually create the table in the database.

- **fields** (columns): every model has fields like name, age, etc.

- **Migration** (actually stores/modify the table structute in DB): django automatically create this file and it has exact instructions for how to modify database that will match with our exact model. When we create a new model or update a model, new migration file gets created, django reads it and applies the changes to database.

1) This commands tells django to see what's in model.py and compare it with what's currently in database, then automatically write instructinos for what needs to be change and creates a file describing the changes and stores the file in the /migrations/ folder.
> `python manage.py makemigrations invoices`
`
Migrations for 'invoices':
  invoices\migrations\0001_initial.py
     +Create model Invoive
`

2) The table is not created yet, you will have to run one more command, then Django will create and execute an SQL statement, based on the content of the new file in the /migrations/ folder. This command will tell django to apply all the unapplied changes from migration file.
> `python manage.py migrate` 
` 
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, invoices, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying invoices.0001_initial... OK
  Applying sessions.0001_initial... OK 
  `

*Note: Django inserts an 'id' field for your tables, which is an auto increment number (first record gets the value 1, the second record 2 etc.), this is the default behavior of Django, you can override it by describing your own 'id' field.*

*Note: you can view the SQL statement that were executed from the migration above. All you have to do is to run this command, with the migration number:*
> `python manage.py sqlmigrate members 0001`

- **ORM (Object Relational Mapper)**: It's a middle man who translates our python query into actual SQL query.
  1) CREATE
  2) FETCH (use get only to retrive single record)
  3) FILTER
  4) UPDATE 

*Note: By default, all Models created in the Django project will be created as tables in this database.*

## Managing data in model:
First open Python interpreter (Python shell)
> `python manage.py shell`
After that we can run commands
>> `from members.models import Member`
>> `Member.objects.all()` this will give you an empty "<QuerySet []>" object. it's collection of data from DB.

1) Insert data (Add Record in table):
- to add single record
> `from members.models import Member`
>> `member = Member(firstname='Girish', lastname='Patil')`
> `member.save()`
- to add multiple records
> `member1 = Member(firstname='Girish', lastname='Patil')`
> `member2 = Member(firstname='Yogesh', lastname='Kale')`
>> `memberList = [member1,member2]`
> `for i in memberList:`
> `i.save()`

2) Read Data
- Run this command to see all records from db
> `Member.objects.all().values()`

3) Update data
> `from members.models import Member`
> `x = Member.objects.all()[2]` x will now represent the member at index 2, which is "yogesh" and to verify that we will run this: `x.firstname` it will show firstname from record.
>> `x.firstname = "Madhukar"` This will modify the record's data.
> `x.save()`

4) Delete data
> `from members.models import Member`
>> `x = Member.objects.all()[1]` x will now represent the member at index 1.
> `x.delete()`

### Update Model
- To add a field to a table after it is created, open the models.py file, and make your changes. Note: we have to explicitly allow NULL values for fields we add, because table already contains records who needs data to represent in new field. Ex.
> `phone = models.IntegerField(null=True)`
- Then make a migration to tell Django that it has to update the database. 
> `python manage.py makemigrations members`
> `python manage.py migrate`

# Django Admin
- admin panel (UI for managing applications)

- admin registration
> `admin.site.register()` # It's a instruction/function that tells django to register model and create a management panel on admin panel. After registering a model django will automatically create a UI for it, which will include list page(all records), add page (form), edit, delete, etc. But first you have to create super user.

- Super User (admin account)
> `python manage.py createsuperuser`
>> `Username (leave blank to use 'imxgirish'): admin`
`Email address: girish040405@gmail.com`
`Password: `
`Password (again):` 
`Superuser created successfully.`

- Custom admin
> `class InvoiceAdmin(admin.ModelAdmin)` # Instead of simply registering a model with admin.site.register(MyModel), you create a custom subclass of "admin.ModelAdmin". This lets you control how data is viewed and edited.

# Forms / validity
#### Django Forms is a powerful built-in feature of the Django Framework that automates, secures, and simplifies the process of handling user input. Instead of writing raw HTML forms and handling validation loops manually, you define your forms as Python classes.

1) create `forms.py` in application's folder

2) import libraries and define metadata for form using python class.
> `from django import forms` `from .models import Invoice`
>> `class myForm(forms.modelForm): class Meta: ` # In here define form's metadata.

3) Create view for rendering form template.

4) Create html template for handling form (include `{% csrf_token %}` and `{{form.as_p}}`)
> `{{form.as_p}}` automatically performs basic validation like checking if user input matches with field's datatype or not, it doesn't exceed max length, etc.
>> for custom validation like 'age <= 150' you have to write code logic in `forms.py`

5) add view to urls.py

# Authentication

#### In Django, the built-in User model handles basic authentication with fields like username, email, password, first_name, and last_name. However, in 95% of real-world production projects, this standard setup is insufficient.You should always set up a custom user model at the start of a new project, even if the default model seems enough. Changing it later after running migrations is highly complex and error-prone.

### Custom User Model
- #### Two Approaches to Custom User Models
1) `AbstractUser` (Recommended): 
> When you like how Django’s user works but want to add extra fields or change the login field to email. Keeps all default fields (first_name, last_name, permissions, etc.) and lets you add yours.

- STEP 1: Create App, go to models.py and import AbstractUser.
- STEP 2: create a class and pass AbstractUser as parent class.
- STEP 3: in settings.py add AUTH_USER_MODEL = 'appName.customModelName'

2) `AbstractBaseUser`:
> When you want to completely redesign the user model from scratch.Provides only core authentication machinery (password, last_login). You must define every other field yourself.

### Application Basics

### User registration

# Flow from user input to output

#### user sends url request > it gets converted to request object > urls.py automatically checks if it's valid or not > if it's valid then it call views for output rendering > the function view will talk to models to query data in ORM format from database or class view will render template files > template will render the output to user.