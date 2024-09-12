from django.db import models

class Ticket(models.Model):
    asunto = models.CharField(max_length=255)
    descripcion = models.TextField()
    estado = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey('auth.User', related_name='tickets', on_delete=models.CASCADE)
    soporte = models.ForeignKey('auth.User', related_name='soporte_tickets', on_delete=models.CASCADE)

    def __str__(self):
        return self.asunto

class Comment(models.Model):
    ticket = models.ForeignKey('Ticket', related_name='comments', on_delete=models.CASCADE)
    usuario = models.CharField(max_length=255)
    contenido = models.TextField()

    def __str__(self):
        return self.contenido