from rest_framework import serializers
from .models import *

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'email', 'message')

class covid1Serializer(serializers.ModelSerializer):
      class Meta:
        model = covid1
        fields = ('id', 'place','number')

class technewsSerializer(serializers.ModelSerializer):
      class Meta:
        model = technews
        fields = ('headlines','description','hyperlink','source')
class worldnewsSerializer(serializers.ModelSerializer):
      class Meta:
        model = worldnews
        fields =('headlines','description','hyperlink','source')

class sportsnewsSerializer(serializers.ModelSerializer):
      class Meta:
        model = sportsnews
        fields =('headlines','description','hyperlink','source')

class fullmoreSerializer(serializers.ModelSerializer):
      class Meta:
        model = fullmore
        fields =('headlines','description','hyperlink','source')
class weathernewsSerializer(serializers.ModelSerializer):
      class Meta:
        model = weatherdetails
        fields =('city','description','temperature','pressure','humidity')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'