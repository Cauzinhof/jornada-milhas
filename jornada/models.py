from django.db import models

class Depoimento(models.Model):
    #Para definir a pasta de upload da imagem com o nome da pessoa
    def upload_path(instance, filename):
        return f'depoimentos/{instance.nome.replace(" ","_")}/{filename}'
    
    nome = models.CharField(max_length=20, blank=False, null=False)
    depoimento = models.TextField(blank=False, null=False)
    foto = models.ImageField(blank=True, upload_to=upload_path)

    def __str__(self) -> str:
        return f'Depoimento de {self.nome}'
    
class Destino(models.Model):
    #Para definir a pasta de upload da imagem com o nome do destino
    def upload_path(instance, filename):
        return f'destinos/{instance.nome.replace(" ","_").replace("/","-")}/{filename}'
    
    nome = models.CharField(max_length=30, blank=False, null=False)
    preco = models.CharField(max_length=20, blank=False, null=False)
    foto = models.ImageField(blank=False, upload_to=upload_path)

    def __str__(self) -> str:
        return self.nome