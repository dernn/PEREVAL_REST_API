from api.models import Coords, Level, Pereval, Images, Users
from rest_framework import serializers


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class ImagesSerializer(serializers.ModelSerializer):
    image = serializers.URLField()

    class Meta:
        model = Images
        fields = ['image', 'title']


class UsersSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        self.is_valid()
        user = Users.objects.filter(email=self.validated_data.get('email'))

        if user.exists():
            return user.first()
        else:
            new_user = Users.objects.create(
                email=self.validated_data.get('email'),
                phone=self.validated_data.get('phone'),
                fam=self.validated_data.get('fam'),
                name=self.validated_data.get('name'),
                otc=self.validated_data.get('otc'),
            )
            return new_user

    class Meta:
        model = Users
        fields = ['email', 'phone', 'fam', 'name', 'otc']


class PerevalSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ['beauty_title', 'title', 'other_titles', 'connect',
                  'add_time', 'status', 'user', 'coords', 'level', 'images']

    def create(self, validated_data):
        user = validated_data.pop('user')
        coords = validated_data.pop('coords')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        current_user = Users.objects.filter(email=user['email'])
        if current_user.exists():
            user_serialized = UsersSerializer(data=user)
            user = user_serialized.save()
        else:
            user = Users.objects.create(**user)

        coords = Coords.objects.create(**coords)
        level = Level.objects.create(**level)
        pereval = Pereval.objects.create(**validated_data, user=user, coords=coords, level=level)

        for img in images:
            image = img.pop('image')
            title = img.pop('title')
            Images.objects.create(image=image, title=title, pereval=pereval)

        return pereval
