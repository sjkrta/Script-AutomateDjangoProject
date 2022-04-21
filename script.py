import os

user_input = int(input('Select from following:\n\n1.Build static\n2.Collect static\n3.Make migrations\n4.Migrate & runserver\n5.Npm start\n6.Pip freeze\n>>'))

if user_input==1:
	os.system('npm run build')
elif user_input==2:
	os.system('python manage.py collectstatic --noinput')
elif user_input==3:
	os.system('python manage.py makemigrations')
elif user_input==4:
	os.system('python manage.py migrate && python manage.py runserver')
elif user_input==5:
	os.system('npm start')
else:
	os.system('echo Wrong input')