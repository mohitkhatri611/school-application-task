from django.db import models

from django.db import models

#student model
class Students(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    dob = models.DateField()
    address=models.TextField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)

    pincode=models.IntegerField()
    phone=models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    class_opted = models.IntegerField()
    marks = models.IntegerField()

    date_enrolled=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.id, self.name
    class Meta:
        db_table = 'students'

