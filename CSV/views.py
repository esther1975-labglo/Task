from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from CSV.serializers import FileUploadSerializer#, SaveFileSerializer
from CSV.models import File
import io, csv, pandas as pd
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser

class UploadFileView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    serializer_class = FileUploadSerializer
    queryset = File.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        i=0
        file1 = File.objects.values('Permit_ID')
        files_list = []
        for i in file1:
            files_list.append(i['Permit_ID'])
        for _, row in reader.iterrows():
            if row['Permit_ID'] not in files_list:
                new_file = File(
                        Inspection_Date = row['Inspection_Date'],
                        Permittee_Name = row["Permittee_Name"],
                        Permit_ID = row['Permit_ID'],
                        Full_Address = row["Full_Address"],
                        )
                print(i)
                i+=1
                a = new_file.save()
            
           
        return Response(                
                        status.HTTP_201_CREATED)


class CsvViewSet(viewsets.ModelViewSet):
    
    queryset = File.objects.all()
    serializer_class = FileUploadSerializer
    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        i=0
        file1 = File.objects.values('Permit_ID')
        files_list = []
        for i in file1:
            files_list.append(i['Permit_ID'])

        for _, row in reader.iterrows():
            if row['Permit_ID'] not in files_list:
                new_file = File(
                        Inspection_Date = row['Inspection_Date'],
                        Permittee_Name = row["Permittee_Name"],
                        Permit_ID = row['Permit_ID'],
                        Full_Address = row["Full_Address"],
                        )
                print(i)
                i+=1
                a = new_file.save()
            
        return Response(status.HTTP_201_CREATED)

class UploadFile(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        with open("Food.csv","r") as f:
            result = csv.DictReader(f)
            my_list = []
        for i in result:
            my_list.append(i)
            my_dict ={"val":my_list}
            
        return Response({"status":"success"},                 
                        status.HTTP_201_CREATED)

