from rest_framework import serializers
class studentserializers(serializers.Serializer):
    name=serializers.CharField(max_length=30)
    email=serializers.EmailField()
    address=serializers.CharField(max_length=30)