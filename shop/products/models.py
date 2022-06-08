from socket import socket
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120) 
    img = models.ImageField(blank=True, null=True)
    cores = models.IntegerField()
    core_clock = models.FloatField()
    boost_clock = models.FloatField(blank=True, null=True)
    tdp = models.DecimalField(decimal_places=3, max_digits=100)
    integrated_graphics = models.BooleanField(("yes"))  
    price = models.FloatField()
    manufacture = models.CharField(max_length=120)
    micro_architecture = models.CharField(max_length=50)
    core_family = models.CharField(max_length=40)
    socket_name = models.CharField(max_length=40)
    maximum_supported_memory = models.IntegerField()
    performance = models.CharField(max_length=30)
    lithograph = models.CharField(max_length=30)
    cpu_cooler = models.CharField(max_length=3)
    
    
    
    
    

    def __str__(self):
        return self.name
    