from django.core.management.base import BaseCommand
from carDealers.models import CarDealer
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populate the database with dummy car dealer data'

    def handle(self, *args, **kwargs):
        faker = Faker()
        cities = ['Bangkok', 'Chandigarh', 'Phuket', 'Delhi', 'New York', 'Chiang Mai', 'Chicago', 'Yangon',
                  'Phoenix', 'Chennai', 'Pattaya', 'Surat Thani',
                  'Mumbai', 'Krabi']

        for _ in range(100):  
            CarDealer.objects.create(
                name=faker.company(),
                name_en=faker.company(),
                license_number=faker.bothify(text='?????-#####/2023'),
                status=random.choice(['Operational', 'Closed']),
                logo=faker.image_url(width=300, height=300),
                email=faker.email(),
                rating_score=round(random.uniform(3.0, 5.0), 4),
                rating_count=random.randint(50, 500),
                comments_count=random.randint(100, 1000),
                popularity=random.randint(500, 2000),
                # city=random.randint(1, 10)
                city=random.choice(cities)
            )

        self.stdout.write(self.style.SUCCESS('Dummy car dealer data added'))
