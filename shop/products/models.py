from msilib.schema import Class
from random import choices
from socket import socket
from tkinter.messagebox import YES
from turtle import heading
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
    price = models.IntegerField()
    rating = models.IntegerField(max_length=5)
    manufacturer = models.CharField(max_length=2, choices=MANUFACTURER_CHOICES)
    part_number = models.CharField(max_length=40)
    micro_architecture = models.CharField(max_length=50)
    code_name = models.CharField(max_length=2,choices=CODE_NAME_CHOICES)
    socket_name = models.CharField(max_length=40)
    maximum_supported_memory = models.IntegerField()
    performance_L1_cache = models.CharField(max_length=30)
    performance_L2_cache = models.CharField(max_length=30)
    performance_L3_cache = models.CharField(max_length=30)
    lithography = models.CharField(max_length=30)
    cpu_cooler = models.CharField(max_length=3)
    simultaneous_multiprocessor= models.BooleanField((YES))

    def __str__(self):
        return self.name
    
class Cpu_cooler(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField
    fanRpm = models.IntegerField()
    noise_level = models.IntegerField()
    color = models.CharField(max_length=20)
    radiator_size = models.IntegerField()
    rating = models.IntegerField()
    price = models.IntegerField()
    manufacturer = models.CharField(max_length=40)
    model = models.CharField(max_length=50)
    part_number = models.CharField(max_length=40)
    height = models.IntegerField()
    Cpu_socket_supported = models.CharField(max_length=40)
    water_cooled = models.BooleanField('yes')
    fan_less = models.BooleanField('yes')
    ecc_support = models.BooleanField
    
    
    def __str__(self):
        return self.name
    
class Mother_board(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField()
    socket_cpu = models.CharField(max_length=40)
    pcie_x_16_slots = models.IntegerField()
    pcie_x_8_slots = models.IntegerField()
    pcie_x_4_slots = models.IntegerField()
    pcie_x_1_slots = models.IntegerField()
    pcie_slots = models.IntegerField()
    form_factor = models.CharField(max_length=20)
    memory_max = models.IntegerField()
    memory_slots = models.IntegerField()
    color = models.CharField(max_length=10)
    rating = models.IntegerField(max_length=5)
    price = models.IntegerField()
    manufacturer = models.CharField(max_length=40)
    part_number = models.CharField(max_length=40)
    chip_set = models.CharField(max_length=30)
    memory_type = models.CharField(max_length=23)
    memory_speed = models.IntegerField()
    sli_cross_fire = models.BooleanField('yes')
    m2_slots = models.IntegerField()
    mini_Pcie_slots = models.IntegerField()
    half_mini_pcie_mSATA_slots = models.IntegerField()
    mSATA_slots = models.IntegerField()
    SATA_speed = models.IntegerField()
    on_board_ethernet = models.BooleanField()
    on_board_video = models.BooleanField()
    usb_2_headers = models.IntegerField()
    usb_2_headers_single = models.IntegerField()
    usb_3_2_gen_1_headers = models.IntegerField()
    usb_3_2_gen_2_headers = models.IntegerField()
    usb_3_gen_2x2_headers = models.IntegerField()
    ecc_support = models.BooleanField()
    wireless_networking = models.BooleanField()
    Raid_support = models.BooleanField()
    
    
    
    
    
        
    
        
    


    