import django
import pydoc
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
django.setup()
pydoc.cli()