"""Create CAT & NUM logical data types."""


from h1st_iot.data_mgmt.models import EquipmentDataFieldType


def run():
    """Run this script to create CAT & NUM logical data types."""
    print(msg := 'Creating Control & Measurement data field types...')

    try:
        ctl, _ = EquipmentDataFieldType.objects.get_or_create(name='ctl')
        msrmt, _ = EquipmentDataFieldType.objects.get_or_create(name='msrmt')
        print(ctl, msrmt)

    except Exception as err:   # pylint: disable=broad-except
        print(f'*** {err} ***')

    print(f'{msg} DONE!\n')
