from django.contrib import admin
from LibraryTraffic.models import *

class LibraryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['LibraryName']}),
        (None, 		     {'fields': ['Location']}),
        ('Operating Hours',  {'fields': ['OperatePeriod','Monday', 'Tuesday','Wednesday', 
        'Thursday','Friday', 'Saturday','Sunday']}),
    ]
    
class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['UniEmail']}),
        (None, 		     {'fields': ['Password']}),
        (None, 		     {'fields': ['DispName']}),
        ('User Access',  {'fields': ['RatingAccess','BookingAccess']}),
    ]

class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Library']}),
        (None, 		     {'fields': ['RoomName']}),
    ] 
    
class BookRoomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Room']}),
        (None, 		     {'fields': ['User']}),
        (None, 		     {'fields': ['BookingDateTime']}),
    ]  
    
admin.site.register(Library, LibraryAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(BookRoom, BookRoomAdmin)

