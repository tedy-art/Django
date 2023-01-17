**jinja 2 templates in html**
->  if we want to execute python line logic in HTML then use jinja 2 templates.


----------------------------------+---------------------------------

**jinja code**                                  

{{data}}                                        

**Python code**
print(data)


----------------------------------+---------------------------------
                                  
**jinja code**                                  
{% if condition %}                              
        tags                                        
{% else %}                                      
        tags                                        
{% end if %}                        

**Python code**                                    
if condtion:                                    
     logic    
else: 
    logic       


----------------------------------+---------------------------------

**Jinja code**                            
{% for i in sequence%}                          
        tags                                        
{% endfor %}    

**Python code**                                    
for i in sequence:
    logic

     
----------------------------------+---------------------------------

step 1: Suppose we have database(dictionary):

data = {1:{'name':'Tom', 'roll': 1, 'marks':77},
        2:{'name':'Harry', 'roll': 2, 'marks':66},
        3:{'name':'Pavan', 'roll': 3, 'marks':88},
        4:{'name':'Jay', 'roll': 4, 'marks':56}
        }

step 2:sql table format:
    name    roll    marks
    Tom     1       77
    Harry   2       66
    Pavan   3       88
    Jay     4       56

step 3:
    context={
        'data' : data
    }

step 4:start project


step 1: Start virtual env

step 2: django-admin startproject jinjaproject

step 3: cd jinjaproject

step 4: python manage.py startapp jinjaapp

step 5: code . {for open VS code}

step 6: jinjaproject -> settings.py

"Add template app in settings.py"
e.g. "settings.py"
    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'jinjaapp',
    ]

step 7:jinjaapp-> templates-> jinjaapp-> display.html