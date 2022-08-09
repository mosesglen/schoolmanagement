from django.shortcuts import render
from rest_framework.decorators import APIView
from . models import StudentDetails, District
from . serializers import StudentDetailsSerializer, DistrictSerializer
from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.
class getprofile_by_id(APIView):
    # to show student data by id by using / after url in Django REST framework
    def get(self, requests, key):
        stud = StudentDetails.objects.get(stud_id=key)
        display = StudentDetailsSerializer(stud)
        return Response(display.data)

    def put(self, requests, key):
        # to replace/update student data
        stud = StudentDetails.objects.get(stud_id=key)
        display = StudentDetailsSerializer(stud, requests.data)
        if display.is_valid():
            display.save()
            return Response(display.data)
        else:
            return Response('No data added')

    def delete(self, requests, key):
        # to delete student data
        stud = StudentDetails.objects.get(id=key)
        stud.delete()
        return Response('Student data removed')


class getprofile(APIView):
    def get(self, requests):
        stud = StudentDetails.objects.all()
        stud = StudentDetailsSerializer(stud, many=True)
        return Response(stud.data)

    def post(self, requests):
        # to add a new student data
        print(requests.data)
        stud = StudentDetailsSerializer(data=requests.data)
        if stud.is_valid():
            stud.save()
            return Response({'status': 1, 'data': stud.data})
        else:
            return Response({'status': 0, 'msg': 'The submitted Data is invalid'})

    def delete(self, requests):
        # to delete student data
        stud = StudentDetails.objects.all()
        stud.delete()
        return Response('All student data removed')


class getdist(APIView):
    # to get dist
        def get(self, requests):
            import pdb
            pdb.set_trace()
            takepro = District.objects.all()
            takeallpro = DistrictSerializer(takepro, many=True)
            return Response(takeallpro.data)
