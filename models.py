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
        
class Style(models.Model):
    """The style of beer as defined by the beerxml."""
    
    TYPE_CHOICES = (
        ('ale', 'Ale'),
        ('cider', 'Cider'),
        ('lager', 'Lager'),
        ('mead', 'Mead'),
        ('mixed', 'Mixed'),
        ('wheat', 'Wheat'),
    )
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    version = models.PositiveSmallIntegerField(default=1)
    category = models.CharField(max_length=100)
    category_number = models.CharField(max_length=100)
    style_letter = models.CharField(max_length=100)
    style_guide = models.CharField(max_length=100)
    style_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    og_min = models.FloatField()
    og_max = models.FloatField()
    fg_min = models.FloatField()
    fg_max = models.FloatField()
    ibu_min = models.FloatField()
    ibu_max = models.FloatField()
    color_min = models.FloatField()
    color_max = models.FloatField()
    carb_min = models.FloatField(blank=True, null=True)
    carb_max = models.FloatField(blank=True, null=True)
    abv_min = models.FloatField(blank=True, null=True)
    abv_max = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    profile = models.TextField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    examples = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name

class MashProfile(models.Model):
    """
    A mash profile is a record used either within a recipe or outside the 
    recipe to precisely specify the mash method used.
    """
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    version = models.PositiveSmallIntegerField(default=1)
    grain_temp = models.FloatField()
    notes = models.TextField(blank=True, null=True)
    tun_temp = models.FloatField(blank=True, null=True)
    sparge_temp = models.FloatField(blank=True, null=True)
    sparge_ph = models.FloatField(blank=True, null=True)
    tun_weight = models.FloatField(blank=True, null=True)
    tun_specific_heat = models.FloatField(blank=True, null=True)
    equip_adjust = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name

class MashStep(models.Model):
    """
    A mash step is an internal record used within a mash profile to denote a 
    separate step in a multi-step mash.
    """

    TYPE_CHOICES = (
        ('infusion', 'Infusion'),
        ('temperature', 'Temperature'),
        ('decoction', 'Decoction'),
    )

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    version = models.PositiveSmallIntegerField(default=1)
    mash_step_type = models.CharField(max_length=12, choices=TYPE_CHOICES)
    infuse_amount = models.FloatField(blank=True, null=True)
    step_temp = models.FloatField()
    step_time = models.FloatField()
    ramp_time = models.FloatField(blank=True, null=True)
    end_temp = models.FloatField(blank=True, null=True)
    mash_profile = models.ForeignKey('MashProfile') 

    def __unicode__(self):
        return self.name    

class Recipe(models.Model):
    """A beer recipe."""
    
    TYPE_CHOICES = (
        ('extract', 'Extract'),
        ('partial_mash', 'Partial Mash'),
        ('all_grain', 'All Grain'),
    )
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    version = models.PositiveSmallIntegerField(default=1)
    recipe_type = models.CharField(max_length=12, choices=TYPE_CHOICES)
    style = models.ManyToManyField('Style')
    equipment = models.ManyToManyField('Equipment', blank=True, null=True)
    brewer = models.CharField(max_length=100)
    asst_brewer = models.CharField(blank=True, null=True, max_length=100)
    batch_size = models.FloatField()
    boil_size = models.FloatField()
    boil_time = models.FloatField()
    effeciency = models.FloatField(blank=True, null=True)
    hops = models.ManyToManyField('Hop', blank=True, null=True)
    fermentables = models.ManyToManyField('Fermentable', blank=True, null=True)
    miscs = models.ManyToManyField('Misc', blank=True, null=True)
    yeasts = models.ManyToManyField('Yeast', blank=True, null=True)
    waters = models.ManyToManyField('Water', blank=True, null=True)
    mash = models.ManyToManyField('MashProfile', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    taste_notes = models.TextField(blank=True, null=True)
    taste_rating = models.FloatField(blank=True, null=True)
    og = models.FloatField(blank=True, null=True)
    fg = models.FloatField(blank=True, null=True)
    fermentation_stages = models.PositiveSmallIntegerField(blank=True, null=True)
    primary_age = models.FloatField(blank=True, null=True)
    primary_temp = models.FloatField(blank=True, null=True)
    secondary_age = models.FloatField(blank=True, null=True)
    secondary_temp = models.FloatField(blank=True, null=True)
    tertiary_age = models.FloatField(blank=True, null=True)
    tertiary_temp = models.FloatField(blank=True, null=True)
    age = models.FloatField(blank=True, null=True)
    age_temp = models.FloatField(blank=True, null=True)
    date = models.DateField()
    carbonation = models.FloatField(blank=True, null=True)
    forced_carbonation = models.BooleanField(default=False)
    priming_sugar_name = models.CharField(blank=True, null=True, max_length=100)
    carbonation_temp = models.PositiveSmallIntegerField(blank=True, null=True)
    priming_sugar_equiv = models.FloatField(blank=True, null=True)
    keg_priming_factor = models.FloatField(blank=True, null=True)
    
    
    def __unicode__(self):
        return self.name
