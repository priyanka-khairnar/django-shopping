import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping.settings')

import random
from faker import Faker

import django
django.setup()

from cart.models import AccessRecord, Brands, WebPage


fake = Faker()

brands = ['Trends', 'INDIE', 'Levis', 'BIBA', 'Baggit']


def add_brand():
    t = Brands.objects.get_or_create(brand_name=random.choice(brands))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        brand = add_brand()
        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        webpage = WebPage.objects.get_or_create(
            brand=brand, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(
            webpage=webpage, date=fake_date)[0]

if __name__ == '__main__':
    print('Populating scripts')
    populate(20)
    print('complete')
