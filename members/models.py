from django.db import models
from django.utils import timezone
from datetime import timedelta

class Member(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    country_code = models.CharField(max_length=5, default='+49')
    phone = models.CharField(max_length=20)
    application_reason = models.TextField(blank=True)
    dorm_room = models.CharField(max_length=50, blank=True)
    street_address = models.CharField(max_length=200, blank=True)
    postal_code_city = models.CharField(max_length=100, blank=True)

    registration_date = models.DateField(auto_now_add=True)
    membership_expiry = models.DateField(blank=True, null=True)

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACTIVE', 'Active'),
        ('EXPIRED', 'Expired'),
        ('DENIED', 'Denied'),
        ('PASSIVE', 'Passive')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    def save(self, *args, **kwargs):
        if not self.membership_expiry:
            self.membership_expiry = self.registration_date + timedelta(days=4 * 365)
        super().save(*args, **kwargs)

    def approve(self, duration_years=1):
        self.status = 'ACTIVE'
        self.membership_expiry = timezone.now().date() + timedelta(days=365 * duration_years)
        self.save()

    def __str__(self):
        return f"{self.name} ({self.status})"