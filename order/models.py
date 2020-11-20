from django.db import models

# Create your models here.

class Parcel_size(models.Model):
    """Model representing a parcel size."""
    size = models.CharField(max_length=200, help_text='Enter a parcel size (e.g. 20cm x 30cm x 50cm)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.size

class Parcel_weight(models.Model):
    """Model representing a parcel weight."""
    weight = models.CharField(max_length=200, help_text='Enter a parcel weight (e.g. 1kg)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.weight

class Delivery_status(models.Model):
    """Model representing a delivery status."""
    status = models.CharField(max_length=200, help_text='Enter a delivery status (e.g. On transit)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.status

class Vehicle_type(models.Model):
    """Model representing a vehicle type."""
    v_type = models.CharField(max_length=50, help_text='Enter a vehicle type (e.g. bike)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.v_type

class Order(models.Model):
    """Model representig order (order for deliver package)"""
    size = models.ManyToManyField(Parcel_size, help_text='Select a parcel size')
    weight = models.ManyToManyField(Parcel_weight, help_text='Select a parcel weight')
    status = models.ManyToManyField(Delivery_status, help_text='Select a delivery status')

    def display_size(self):
        """Create a string for the parcel size. This is required to display parcel size in Admin."""
        return ', '.join(Parcel_size.size for size in self.size.all()[:3])
    
    display_size.short_description = 'Size'

    def display_weight(self):
        """Create a string for the parcel weight. This is required to display parcel weight in Admin."""
        return ', '.join(Parcel_weight.weight for weight in self.weight.all()[:3])
    
    display_weight.short_description = 'Weight'

    def display_status(self):
        """Create a string for the delivery status. This is required to display delivery status in Admin."""
        return ', '.join(Delivery_status.status for status in self.status.all()[:3])
    
    display_status.short_description = 'Status'

class Vehicle(models.Model):
    """Model representig Vehicles"""
    v_type = models.ManyToManyField(Vehicle_type, help_text='Select a vehicle type')
    production_year = models.IntegerField(default=2000)
    check_date = models.DateField(null=True, blank=True)
    brand = models.CharField(max_length=30, help_text='Enter a brand(e.g. Renault)')
    v_model = models.CharField(max_length=50, help_text='Enter a brand(e.g. Kangoo)')
    plate = models.CharField(max_length=20, help_text='LLE3421')
    comment = models.TextField(max_length=1000, help_text='Enter a comment about behicle')
        
    def display_v_type(self):
        """Create a string for the vehicle type. This is required to display vehicle type in Admin."""
        return ', '.join(Vehicle_type.v_type for v_type in self.v_type.all()[:3])
    
    display_v_type.short_description = 'Vehicle_type'



    
