from django.db import models

class informacion(models.Model):
  nombre= models.CharField(max_length=100)
  ano= models.DateTimeField()
  texto= models.TextField()

  def publish(self):
      self.save()

class comentario(models.Model):
  titulo= models.CharField(max_length=100)
  estrellas= models.IntegerField()
  comentario= models.TextField()
  autor= models.CharField(max_length=100)

  def publish(self):
      self.save()

