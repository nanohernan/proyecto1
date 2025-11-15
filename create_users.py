import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ventas_proyectos.settings')
django.setup()

from django.contrib.auth.models import User

# Crear usuario admin
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@ventas.com', 'MiPassword123')

# Crear usuario tecnico01
if not User.objects.filter(username='tecnico01').exists():
    User.objects.create_user('tecnico01', 'tecnico@ventas.com', 'SuContrasenaSegura123')

print("Usuarios creados exitosamente!")