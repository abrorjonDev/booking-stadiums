from rest_framework import serializers

from stadiums.models import Stadium


class StadiumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ('id', 'name', 'address', 'contact', 'status')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['images'] = instance.images_data(request=self.context['request'])
        data['created_by'] = str(instance.created_by)
        data['modified_by'] = str(instance.modified_by)

        return data


class StadiumWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = "__all__"
        read_only_fields = ('_created_by', '_modified_by')

    def validate(self, attrs):
        if self.instance:
            attrs['_modified_by'] = self.get_request_user()
        else:
            attrs['_created_by'] = self.get_request_user()
        return attrs

    def get_request_user(self):
        if self.context.get('request'):
            return self.context.get('request').user
