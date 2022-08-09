from django.db import models




class District(models.Model):
    dist_id = models.AutoField(primary_key=True)
    dist_name = models.CharField(unique=True, max_length=50)


    class Meta:
        managed = False
        db_table = 'district'

        



class StudentDetails(models.Model):
    stud_id = models.AutoField(primary_key=True)
    reg_no = models.CharField(unique=True, max_length=10)
    stud_name = models.CharField(max_length=50)
    date_of_join = models.DateField()
    district = models.ForeignKey(District, models.DO_NOTHING)
    address = models.TextField()
    gender = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'student_details'

