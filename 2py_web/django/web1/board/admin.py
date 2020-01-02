from django.contrib import admin

from board.models import Table1
admin.site.register(Table1)

# $ conda list => django version check
# $ pip install django==2.2.5 => version change(기존것 자동삭제)
# $ python manage.py createsuperuser
#       L id/pw = admin/1234