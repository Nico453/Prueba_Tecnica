from django.db import models

class Result(models.Model):
    
    CATEGORY_CHOICES = [
        ('bad', 'bad'),
        ('medium', 'medium'),
        ('good', 'good')]
    user_id = models.CharField(max_length=20 )
    value = models.PositiveIntegerField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    timestamp = models.DateTimeField()
    ip = models.GenericIPAddressField()
    attempts = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user_id} - {self.value} - {self.category} - {self.timestamp}"