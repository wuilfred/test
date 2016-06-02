from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ProductEvent(models.Model):
    id_product_event = models.DecimalField(max_digits=8, decimal_places=2)
    name_product_event = models.CharField(max_length=100)
    price_product_evet = models.IntegerField()
    id_event = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return "%s %s %s %s" % (self.id_product_event, self.name_product_event,
                                self.price_product_evet, self.id_event)

class SaveTicketEvent(models.Model):
    id_event = models.DecimalField(max_digits=8, decimal_places=2)
    name_event = models.CharField(max_length=65)
    status_event = models.CharField(max_length=65)
    start_time_event = models.DateTimeField()
    end_time_event = models.DateTimeField()
    time_letter_event = models.CharField(max_length=100)
    location_event  = models.CharField(max_length=100)
    fb_share_img_url_event = models.TextField()
    description_event   = models.TextField()
    ticketshop_url_event  = models.TextField()
    sold_out_event = models.CharField(max_length=25)
    id_event_products = models.ForeignKey(ProductEvent,
                                          on_delete=models.CASCADE)
    organizer_event = models.DecimalField(max_digits=8, decimal_places=2)