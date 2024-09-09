from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dotenv import load_dotenv
import os

load_dotenv

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='ADMIN').exists():
            User.objects.create_superuser('USER', 'EMAIL_SUPER_USER', 'PASSWORD_SUPER_USER')
            self.stdout.write(self.style.SUCCESS('Superusuario creado exitosamente'))
        else:
            self.stdout.write(self.style.WARNING('El superusuario ya existe'))
