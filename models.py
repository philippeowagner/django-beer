from django.db import models

class Hop(models.Model):
    """
    Represents hop as defined by beerxml.  
    
    See http://beerxml.com/beerxml.htm for details.
    """
    USE_CHOICES = (
        ('boil', 'Boil'),
        ('dry_hop', 'Dry Hop'),
        ('mash', 'Mash'),
        ('first_wort', 'First Wort'),
        ('aroma', 'Aroma'),
    )
    
    TYPE_CHOICES = (
        ('bittering', 'Bittering'),
        ('aroma', 'Aroma'),
        ('both', 'Both'),
    )
    
    FORM_CHOICES = (
        ('pellet', 'Pellet'),
        ('plug', 'Plug'),
        ('leaf', 'Leaf'),
    )
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    version = models.SmallIntegerField(default=1)
    alpha = models.FloatField()
    amount = models.FloatField()
    use = models.CharField(max_length=10, choices=USE_CHOICES)
    time = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    hop_type = models.CharField(blank=True, null=True, max_length=10, choices=TYPE_CHOICES)
    form = models.CharField(blank=True, null=True, max_length=10, choices=FORM_CHOICES)  
    beta = models.FloatField(blank=True, null=True)
    hsi = models.FloatField(blank=True, null=True)
    origin = models.CharField(blank=True, null=True, max_length=100)
    substitutes = models.CharField(blank=True, null=True, max_length=100)
    humulene = models.FloatField(blank=True, null=True)
    caryophyllene = models.FloatField(blank=True, null=True)
    cohumulone = models.FloatField(blank=True, null=True)
    myrcene = models.FloatField(blank=True, null=True)