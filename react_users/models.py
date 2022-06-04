from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class React_users(models.Model):
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')
    password = models.TextField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def __str__(self):
        return self.name
