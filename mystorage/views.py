from django.shortcuts import render
from rest_framework import viewsets
from .models import Essay,Album,Files
from .serializers import EssaySerializer,AlbumSerializer,FilesSerializer
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset=Essay.objects.all()
    serializer_class=EssaySerializer

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)

    #현재 request를 보내는 유저==self.request.user
    
    #쿼리셋 필터링
    def get_queryset(self):
        qs=super().get_queryset()
        if(self.request.user.is_authenticated):
            qs=qs.filter(author=self.request.user)
        else:
            qs=qs.none()
        return qs

    #Search하기
    filter_backends=[SearchFilter]
    search_fields=('title','body')

class ImageViewSet(viewsets.ModelViewSet):
    queryset=Album.objects.all()
    serializer_class=AlbumSerializer



class FileViewSet(viewsets.ModelViewSet):
    queryset=Files.objects.all()
    serializer_class=FilesSerializer

    #나는왜 업로드가 되는것인가
    #참네..
    #어쨌든 fileupload를 위한것 2가지
    #parser_class지정과 create()를 오버라이딩
    
    parser_classes=(MultiPartParser,FormParser)
    #다양한 방법들로 request를 수락하는 방법중하나
    
    def post(self,request,*args,**kwargs):
        serializer=FilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #APIView배울때 HTTP메소드에 따라서 오버라이딩하는것과 동일
    #create()는 POST요청이므로