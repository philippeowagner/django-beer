from django.db import models

class Hop(models.Model):
    """Represents hop as defined by beerxml."""
    
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
    version = models.PositiveIntegerField(default=1)
    alpha = models.FloatField()
    amount = models.FloatField()
    use = models.CharField(max_length=10, choices=USE_CHOICES)
    time = models.FloatField()
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
    
    def __unicode__(self):
        return self.name

class Fermentable(models.Model):
    """Represents fermentables as defined by beerxml."""
    
    TYPE_CHOICES = (
        ('grain', 'Grain'),
        ('sugar', 'Sugar'),
        ('extract', 'Extract'),
        ('dryextract', 'Dry Extract'),
        ('adjunct', 'Adjunct'),
    )
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    version = models.PositiveSmallIntegerField(default=1)
    ferm_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.FloatField()
    ferm_yield = models.FloatField()
    color = models.FloatField()
    add_after_boil = models.BooleanField(default=False)
    origin = models.CharField(blank=True, null=True, max_length=100)
    supplier = models.CharField(blank=True, null=True, max_length=100)
    notes = models.TextField(blank=True, null=True)
    coarse_fine_diff = models.FloatField(blank=True, null=True)
    moisture = models.FloatField(blank=True, null=True)
    diastic_power = models.FloatField(blank=True, null=True)
    protein = models.FloatField(blank=True, null=True)
    max_in_batch = models.FloatField(blank=True, null=True),
    recommend_mash = models.BooleanField(default=False)
    ibu_gal_per_lb = models.FloatField(blank=True, null=True)
    
    def __unicode__(self):
         return self.name

class Yeast(models.Model):
    """Represents yeast as defined by beerxml."""
    
    TYPE_CHOICES = (
        ('ale', 'Ale'),
        ('lager', 'Lager'),
        ('wheat', 'Wheat'),
        ('wine', 'Wine'),
        ('champagne', 'Champagne'),
    )
    
    FORM_CHOICES = (
        ('liquid', 'Liquid'),
        ('dry', 'Dry'),
        ('slant', 'Slant'),
        ('culture', 'Culture'),
    )
    
    FLOCCULATION_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('very_high', 'Very High'),
    )
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    version = models.PositiveSmallIntegerField(default=1)
    yeast_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    form = models.CharField(max_length=10, choices=FORM_CHOICES)
    amount = models.FloatField()
    amount_is_weight = models.BooleanField(default=False)
    laboratory = models.CharField(blank=True, null=True, max_length=100)
    product_id = models.CharField(blank=True, null=True, max_length=100)
    min_temperature = models.FloatField(blank=True, null=True)
    max_temperature = models.FloatField(blank=True, null=True)
    flocculation = models.CharField(blank=True, null=True, max_length=10, choices=FLOCCULATION_CHOICES)
    attenuation = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    best_for = models.CharField(blank=True, null=True, max_length=200)
    times_cultured = models.IntegerField(blank=True, null=True)
    max_reuse = models.IntegerField(blank=True, null=True)
    add_to_secondary = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name

class Misc(models.Model):
    """The miscellaneous non-fermentable ingredients has specified by beerxml."""
    
    TYPE_CHOICES = (
        ('spice', 'Spice'),
        ('fining', 'Fining'),
        ('wateragent', 'Water Agent'),
        ('herb', 'Herb'),
        ('flavor', 'Flavor'),
        ('other', 'Other'),
    )
    
    USE_CHOICES = (
        ('boil', 'Boil'),
        ('mash', 'Mash'),
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('bottling', 'Bottling'),
    )
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    version = models.PositiveSmallIntegerField(default=1)
    misc_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    misc_use = models.CharField(max_length=10, choices=USE_CHOICES)
    time = models.FloatField()
    amount = models.FloatField()
    amount_is_weight = models.BooleanField(default=False)
    use_for = models.CharField(blank=True, null=True, max_length=100)
    notes = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name

class Water(models.Model):
    """Represents water as defined by beerxml."""
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    version = models.PositiveSmallIntegerField(default=1)
    amount = models.FloatField()
    calcium = models.FloatField()
    bicarbonate = models.FloatField()
    sulfate = models.FloatField()
    chloride = models.FloatField()
    sodium = models.FloatField()
    magnesium = models.FloatField()
    ph = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name

class Equipment(models.Model):
    """Provides details about needed equipment."""
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    version = models.PositiveSmallIntegerField(default=1)
    boil_size = models.FloatField()
    batch_size = models.FloatField()
    tun_volume = models.FloatField(blank=True, null=True)
    tun_weight = models.FloatField(blank=True, null=True)
    tun_specific_heat = models.FloatField(blank=True, null=True)
    top_up_water = models.FloatField(blank=True, null=True)
    trub_chiller_loss = models.FloatField(blank=True, null=True)
    evap_rate = models.FloatField(blank=True, null=True)
    boil_time = models.FloatField(blank=True, null=True)
    calc_boil_volume = models.BooleanField(default=False)
    lauter_deadspace = models.FloatField(blank=True, null=True)
    top_up_kettle = models.FloatField(blank=True, null=True)
    hop_utilization = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name
