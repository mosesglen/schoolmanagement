from .models import StudentDetails, District
from rest_framework.serializers import ModelSerializer



class StudentDetailsSerializer(ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = '__all__'


class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'