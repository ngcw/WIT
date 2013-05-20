from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Library(models.Model):
    LibraryName = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    OperatePeriod = models.CharField(max_length=200)
    Monday = models.CharField(max_length=200)	
    Tuesday = models.CharField(max_length=200)
    Wednesday = models.CharField(max_length=200)
    Thursday = models.CharField(max_length=200)
    Friday = models.CharField(max_length=200)
    Saturday = models.CharField(max_length=200)
    Sunday = models.CharField(max_length=200)
    def __unicode__(self):
        return self.LibraryName
	
class LibraryLevelTraffic(models.Model):
    Library = models.ForeignKey(Library)
    Level = models.IntegerField(max_length=3)
    ComputerVac = models.IntegerField(max_length=4)
    SeatVac = models.IntegerField(max_length=4)
  
class Room(models.Model):
    Library = models.ForeignKey(Library)
    RoomName = models.CharField(max_length=200)
    def __unicode__(self):
        return self.RoomName
	
class User(models.Model):
    UniEmail = models.CharField(max_length=200)
    Password = models.CharField(max_length=32)
    DispName = models.CharField(max_length=200)
    RatingAccess = models.CharField(max_length=3)
    BookingAccess = models.CharField(max_length=3)
    def __unicode__(self):
        return self.DispName

class Rating(models.Model):
    LibraryLevelTraffic = models.ForeignKey(LibraryLevelTraffic)
    User = models.ForeignKey(User)
    SeatRating = models.CharField(max_length=200)
    TrafficDateTime = models.DateTimeField('Traffic Date and Time')
    
class BookRoom(models.Model):
    Room = models.ForeignKey(Room)
    User = models.ForeignKey(User)
    BookingDateTime = models.DateTimeField('Booking Date and Time')
    def __unicode__(self):
        return '%s-%s' %(self.User,)

   
