from django.db import models
from bus.models import Bus
# Create your models here.
class Booking(models.Model):
    book_id= models.CharField(max_length=250, blank=True)
    date_added=models.DateField(auto_now_add=False)


class BookingBus(models.Model):
    bus= models.ForeignKey(Bus, on_delete=models.CASCADE)
    book=models.ForeignKey(Booking, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.bus