from django.contrib import admin
from .models import *

# which registers models with the Django Admin site to manage easily. 
admin.site.register(Admin_Helath_CSV)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Feedback)
admin.site.register(Search_Data)
