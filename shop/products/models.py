from msilib.schema import Class
from random import choices
from socket import socket
from unicodedata import decimal
from django.db import models

MANUFACTURER_CHOICES = [
    ('IN', 'Intel'),
    ('AM', 'AMD'),
]

CORE_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('4', '4'),
    ('6', '6'),
    ('8', '8'),
    ('10', '10'),
    ('12', '12'),
    ('14', '14'),
    ('16', '16'), 
    ('18', '18'),  
]

CODE_NAME_CHOICES = [
    ('AL', 'Alder Lake'),
    ('RL','Rocket Lake'),
    ('SB','Sandy Bridge'),
    ('IB','Ivy Bridge'),
    ('H','Haswell'),
    ('B','Broadwell'),
    ('SL','Skylake'),
    ('CL','Coffe Lake'),
    ('KL','Kaby Lake'),
    ('GL','Gemini Lake'),
    ('WL','Whiskey Lake'),
    ('TL','Tiger Lake'),
    ('LF','Lakefield'),
    ('CL','Cascade Lake'),
    ('CO','Comet Lake'),
    ('RL','Rocket Lake'),
    ('D','Denverton'),
   
]


class Product(models.Model):
    name = models.CharField(max_length=120) 
    img = models.ImageField(blank=True, null=True)
    cores = models.CharField(max_length=2, choices=CORE_CHOICES)
    core_clock = models.FloatField()
    boost_clock = models.FloatField(blank=True, null=True)
    tdp = models.IntegerField()
    integrated_graphics = models.BooleanField(("yes"))  
    price = models.FloatField()
    manufacturer = models.CharField(max_length=2, choices=MANUFACTURER_CHOICES)
    micro_architecture = models.CharField(max_length=50)
    code_name = models.CharField(max_length=2,choices=CODE_NAME_CHOICES)
    socket_name = models.CharField(max_length=40)
    maximum_supported_memory = models.IntegerField()
    performance = models.CharField(max_length=30)
    lithography = models.CharField(max_length=30)
    cpu_cooler = models.CharField(max_length=3)

    def __str__(self):
        return self.name


    