import os

try:
    # lower input, split words and return by joining with '_'
    def split_join(name):
        name = "_".join(name.lower().split())
        return name

    # default project / app names
    django_project_name='config'
    django_app_name='app'
    virtual_env_name='.venv'

    # asking user for project and app names
    
    react_app_name = split_join(input('What do you want to name your react app?\n>>'))
    user_input_default=False
    while user_input_default ==False:
        user_input=input('Do you want to use default setup for the rest? (y for yes / n for no)\n>>').lower()
        if user_input=='y':
            user_input_default=True
        elif user_input=='n':
            django_project_name = split_join(
                input('What do you want to name your django project?\n>>'))
            django_app_name = split_join(
                input('What do you want to name your django app?\n>>'))
            virtual_env_name = split_join(
                input('What do you want to name your virtual environment?\n>>'))
            user_input_default=False
        else:
            print("It isn't a valid input.\n")

    # os.system(f'npx create-react-app {react_app_name}')
    os.system(f'npx create-react-app {react_app_name}')

    # change directory to react app
    os.chdir(f'{react_app_name}')

    # create script files (to make migrations and collect static)
    cmd1 = 'npm run build'
    cmd2 = 'python manage.py collectstatic --noinput'
    cmd3 = 'python manage.py makemigrations'
    cmd4 = 'python manage.py migrate && python manage.py runserver'
    cmd5 = 'npm start'
    cmd6 = 'pip freeze > requirements.txt'

    static = open(f"script.py", "x")
    static.write(f"import os\n\nuser_input = int(input('Select from following:\\n\\n1.Build static\\n2.Collect static\\n3.Make migrations\\n4.Migrate & runserver\\n5.Npm start\\n6.Pip freeze\\n>>'))\n\nif user_input==1:\n\tos.system('{cmd1}')\nelif user_input==2:\n\tos.system('{cmd2}')\nelif user_input==3:\n\tos.system('{cmd3}')\nelif user_input==4:\n\tos.system('{cmd4}')\nelif user_input==5:\n\tos.system('{cmd5}')\nelse:\n\tos.system('echo Wrong input')")
    static.close()


    # create virtual env, activate, install pkg, lib and create procfile
    env = f'python -m venv {virtual_env_name}'
    activate_env = f'.\\{virtual_env_name}\\Scripts\\activate'
    install_pkg_lib ='pip install django djangorestframework gunicorn django_heroku django-cors-headers'
    pip_freeze = 'pip freeze > requirements.txt'
    procfile =f'echo web: gunicorn config.wsgi > Procfile'
    os.system(f'{env} && {activate_env} && {install_pkg_lib} && {pip_freeze} && {procfile}')

    # create django project and app
    os.system(f'django-admin startproject {django_project_name} . && django-admin startapp {django_app_name}')

    # migrate and create superuser
    os.system(f'python manage.py migrate && python manage.py createsuperuser')

except:
    print("Something went wrong. (Scripts folder might already exist in the working directory.)")