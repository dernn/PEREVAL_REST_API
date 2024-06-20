from api.models import Coords, Images, Level, Pereval, Users
from api.serializers import PerevalSerializer

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class PerevalApiTestCase(APITestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(
            beauty_title='Beauty title 1',
            title='Title 1',
            other_titles='Other titles 1',
            connect='Connect',
            user=Users.objects.create(
                email='user1@mail.ru',
                fam='lastname1',
                name='firstname1',
                otc='patronymic1',
                phone='+11111111111'
            ),
            coords=Coords.objects.create(
                latitude='11.11111',
                longitude='22.22222',
                height='1111'
            ),
            level=Level.objects.create(
                winter='1A',
                spring='1A',
                summer='1A',
                autumn='1A'
            ),
        )

        self.image_1 = Images.objects.create(
            title='imageTitle1',
            image='image1.jpg',
            pereval=self.pereval_1
        )

        self.pereval_2 = Pereval.objects.create(
            beauty_title='Beauty title 2',
            title='Title 2',
            other_titles='Other titles 2',
            connect='Connect',
            user=Users.objects.create(
                email='user2@mail.ru',
                fam='lastname2',
                name='firstname2',
                otc='partonymic2',
                phone='+22222222222'
            ),
            coords=Coords.objects.create(
                latitude='33.33333',
                longitude='44.44444',
                height='2222'
            ),
            level=Level.objects.create(
                winter='',
                spring='1A',
                summer='1A',
                autumn='1A'
            ),
        )

        self.image_2 = Images.objects.create(
            title='imageTitle2',
            image='image2.jpg',
            pereval=self.pereval_2
        )

    def test_get(self):
        url = f'{reverse("pereval-list")}?get_all=true'
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data

        print('--------url----------')
        print(url)
        print('------response-------')
        print(response)
        print('-----serializer------')
        print(serializer_data)
        print('----response.data----')
        print(response.data)
        # print('---response[results]-')
        # print(response.data['results'])

        # сравнивает serializer_data и response.data
        self.assertEqual(serializer_data, response.data)
        # проверяет, что количество serializer_data = 2
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)