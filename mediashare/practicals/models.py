from django.db import models

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name

class MenuItem(models.Model):
    menu_item = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=300,default='Change Me')

    def __str__(self):
        return self.menu_item


class Objective(models.Model):
    objective = models.TextField()
    menu_item = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.objective
    def display_subject(self):
        return self.menu_item.subject
    def list_menu(self):
        return ', '.join([self.menu_item for self in self.menu_item.all()])
