from django.db import migrations


FEATURED_STORES = [
    {
        'store_code': 'Bhagat Generic Medicine Store',
        'store_state': 'MAHARASHTRA',
        'store_district': 'Raigad',
        'store_address': 'At. Zirad, Alibag Revas Road, Zirad, Alibaug - 402201 (Near New Vaibhav Hotel)',
        'store_pincode': '402201',
    },
    {
        'store_code': 'Kamothe Generic Medicine Store',
        'store_state': 'MAHARASHTRA',
        'store_district': 'Raigad',
        'store_address': 'Shop No 2, Plot No 6, Sector 6, Infront Of Ramsheth Thakur School, Kamothe, Navi Mumbai, Maharashtra - 410209',
        'store_pincode': '410209',
    },
    {
        'store_code': 'Asmi Generic Medicine Store',
        'store_state': 'MAHARASHTRA',
        'store_district': 'Nashik',
        'store_address': 'Shop No. 2, Sarasbagh Apartment, Bhaba Nagar Road, Mumbai Naka, Nashik - 422001',
        'store_pincode': '422001',
    },
    {
        'store_code': 'Avishkar Generic Medicine Store',
        'store_state': 'MAHARASHTRA',
        'store_district': 'Thane',
        'store_address': 'Shop No 10 Sugandh Co-Operative Housing Society Ltd, Sector 7, Kopar, Navi Mumbai - 400709 (Near D-mart)',
        'store_pincode': '400709',
    },
    {
        'store_code': 'Swati Generic Medicine Store',
        'store_state': 'MAHARASHTRA',
        'store_district': 'Satara',
        'store_address': '7 Star Cinema Building, Shop Number 41, Near S T Stand, Satara, Maharashtra',
        'store_pincode': '',
    },
    {
        'store_code': 'Wagholi Generic Medicine Store',
        'store_state': 'MAHARASHTRA',
        'store_district': 'Pune',
        'store_address': 'Fadai Chowk, Grampanchayat Road, near Ganesh Mandir, Wagholi, Pune - 412207',
        'store_pincode': '412207',
    },
]


def seed_featured_stores(apps, schema_editor):
    Store = apps.get_model('website', 'Store')
    for store_data in FEATURED_STORES:
        Store.objects.get_or_create(
            store_code=store_data['store_code'],
            store_state=store_data['store_state'],
            store_district=store_data['store_district'],
            defaults={
                'store_address': store_data['store_address'],
                'store_pincode': store_data['store_pincode'],
                'store_contact': 'Not listed',
            },
        )


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0006_alter_medicine_id_alter_store_id'),
    ]

    operations = [
        migrations.RunPython(seed_featured_stores, migrations.RunPython.noop),
    ]