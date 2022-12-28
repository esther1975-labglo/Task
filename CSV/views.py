from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from CSV.serializers import FileUploadSerializer, SaveFileSerializer
from CSV.models import File
import io, csv, pandas as pd
from rest_framework import generics
from django.db.models import Count

class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    queryset = File.objects.all().distinct('Permit_ID')
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        i=0
        for _, row in reader.iterrows():
            
            new_file = File(
                       Inspection_Date = row['Inspection_Date'],
                       Permittee_Name = row["Permittee_Name"],
                       Permit_ID = row['Permit_ID'],
                       Full_Address = row["Full_Address"],
                       )
            print(i)
            i+=1
            new_file.save()
            mylist = [] 
            mylist.append(new_file)
            print(mylist)
            #duplicate_emails = File.objects.values('Permit_ID').annotate(id_count=Count('Permit_ID')).filter(id_count__gt=1)
            for data in mylist:
                Permit_ID = data['Permit_ID']
                s = File.objects.filter(Permit_ID=Permit_ID).order_by('pk')[1:].delete()
                s.save()
        return Response({"status": "success"}, 
                        status.HTTP_201_CREATED)