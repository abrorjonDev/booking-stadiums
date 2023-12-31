from rest_framework import serializers

from stadiums.models import StadiumImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadiumImage
        exclude = ('_modified_by', '_created_by')
    
    def validate(self, attrs):
        if self.instance:
            attrs['_modified_by'] = self.get_request_user()
        else:
            attrs['_created_by'] = self.get_request_user()
        return attrs

    def get_request_user(self):
        if self.context.get('request'):
            return self.context.get('request').user
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['created_by'] = str(instance.created_by) if instance.created_by else None
        data['modified_by'] =str(instance.modified_by) if instance.modified_by else None
        return data