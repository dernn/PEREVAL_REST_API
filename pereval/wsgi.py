"""
WSGI config for pereval project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv

# For your web app itself: loading your .env file in your WSGI file
project_folder = os.path.expanduser('/home/dernn/PEREVAL_REST_API')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'), override=True)

# assuming your django settings file is at '/home/dernn/mysite/mysite/settings.py'
# and your manage.py is is at '/home/dernn/mysite/manage.py'
path = '/home/dernn/PEREVAL_REST_API'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'pereval.settings'

# then:
application = get_wsgi_application()
