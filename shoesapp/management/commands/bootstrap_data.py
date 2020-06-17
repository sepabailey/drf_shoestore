from django.core.management.base import BaseCommand, CommandError
from shoesapp.models import Manufacturer, ShoeType, ShoeColor, Shoe


# Matt helped set up the bootstrap file
class Command(BaseCommand):
    help = 'populate shoe type and populate shoe color'

    def handle(self, *args, **options):
        shoecolorlist = [
            'Red',
            'Orange',
            'Yellow',
            'Green',
            'Blue',
            'Indigo',
            'Violet',
            'White',
            'Black',
        ]
        shoetypelist = [
            'sneaker',
            'boot',
            'sandal',
            'dress',
            'other',
        ]

        for shoe_color in shoecolorlist:
            ShoeColor.objects.create(
                color_name=shoe_color
            )

        for shoe_type in shoetypelist:
            ShoeType.objects.create(
                style=shoe_type
            )
