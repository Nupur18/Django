from django.db import models

# make migrations - create changes and store in file
# migrate - apply the pending changes to the file created by makemigartions
# apply ka matlab database write kardo jake db.sqlite database me ya koi bhi database jo use ho rha hai unme changes ko apply kardo

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name
