from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    role = models.TextField()

    def __str__(self):
        return self.name + f' ({self.role})'
    
    class Meta:
        verbose_name_plural = "people"

class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    assignedTo = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title
