from .models import Essay,Album,Files
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):

    author_name=serializers.ReadOnlyField(source='author.username')

    class Meta:
        model=Essay
        fields=('pk','title','body','author_name',)


class AlbumSerializer(serializers.ModelSerializer):

    author_name=serializers.ReadOnlyField(source='author.username')
    image=serializers.ImageField(use_url=True)#업로드한 이미지의확인작업 url로 하겠다

    class Meta:
        model=Album
        fields=('pk','image','desc','author_name',)


class FilesSerializer(serializers.ModelSerializer):
    #여기에서는 model의 column명과 동일하게 변수명을 지어야한다
    author=serializers.ReadOnlyField(source='author.username')
    myfile=serializers.FileField(use_url=True)#파일 업로드한 확인을 url로 확인하겠다

    class Meta:
        model=Files
        fields=('pk','myfile','desc','author',)