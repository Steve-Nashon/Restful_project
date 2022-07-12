# setting up Restful_project 
  ## first install all the project dependecies am assuming that python is installed and configured 
**pip install -r requirements.txt**
 ## Configure your postgress database
- from r'/Restful_project/backend/inventory/inventory' open setting.py and update your database connection credential respectively \
      &emsp;&emsp;  'NAME': 'Database Name', \
      &emsp;&emsp;  'USER':'Your USER', \
       &emsp;&emsp; 'PASSWORD':'Your PASSWORD', \
       &emsp;&emsp; 'HOST':'localhost', \
       &emsp;&emsp; 'PORT':'5432', \
   ## make db migration and create db migration
   - from r'/Restful_project/backend/inventory' make db migration \
   &emsp;&emsp; **python manage.py makemigrations**
   - from r'/Restful_project/backend/inventory' migrate to the db \
  &emsp;&emsp;  **python manage.py migrate**
  ## Run Server
  - from r'/Restful_project/backend/inventory'  run our django server \
  &emsp;&emsp;  **python manage.py runserver 8000** \
  you can change the port to the one that you have configured your django with.
  ## open Restful_project urls
  from your web browser launch **localhost/description** to get a list of the project descriptions and endpoints
  

