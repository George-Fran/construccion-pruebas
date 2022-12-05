from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(default='Hola estoy usando Bindev', max_length=100)
    image = models.ImageField(default='default.jpeg')

    def __str__(self):
        return f'Perfil de {self.user.username}'
    
    def siguiendo(self):
        user_ids = Relaciones.objects.filter(from_user=self.user)\
            .values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)
    
    def seguidores(self):
        user_ids = Relaciones.objects.filter(to_user=self.user)\
            .values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)
    
    

class Post(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.content
    
class Relaciones(models.Model):
	from_user = models.ForeignKey(User, related_name='relaciones', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='relacionado_con', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} para {self.to_user}'
