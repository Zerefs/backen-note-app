from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import NoteSerializer
from NoteApp.models import Notes

class NoteViewApi(APIView):
    
    def get_objects(self, id):
        try:
            return Notes.objects.get(id=id)
        except Notes.DoesNotExist:
            return None
            
    
    def get(self, request, *args, **kwargs):
        note = Notes.objects.all()
        serializer = NoteSerializer(note, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            "title" : request.data.get("title"),
            "content" : request.data.get("content"),
        }
        
        serializer = NoteSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
            response = {
                "status":status.HTTP_201_CREATED,
                "message":"Succes create data",
                "data":serializer.data,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id, *args, **kwargs):
        note_data = self.get_objects(id)
        if not note_data:
            return Response(
                {'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Data does not exist...',
                'data': {}},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = NoteSerializer(instance=note_data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_200_OK,
                'message': 'Data updated successfully...',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, *args, **kwargs):
        note_data = self.get_objects(id)
        
        if not note_data:
            return Response({
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"Data doesn't exist",
                "data":{},
            }, status=status.HTTP_400_BAD_REQUEST
                            )
        note_data.delete()
        response ={
            "status":status.HTTP_200_OK,
            "message":"Delete data succesfully",
        }
        return Response(response, status=status.HTTP_200_OK)