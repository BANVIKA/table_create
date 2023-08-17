from django.db import models

# Create your models here.
class dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
    def __str__(self):
       return self.dname

    
class emp(models.Model):
    eno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    hiredate=models.DateField()
    sal=models.IntegerField()
    com=models.IntegerField(default=None,null=True,blank=True)
    deptno=models.ForeignKey(dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.job

    


    

