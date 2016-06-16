# -*- coding: utf-8 -*-

from Florennes.urban.dataimport.parcellings.mappers import IdMapper, ParcellingMapper, ParcelDataMapper, ParcelsMapper
from Florennes.urban.dataimport.parcellings.mappers import ParcellingFactory, ParcelFactory


OBJECTS_NESTING = [
    (
        'PARCELLINGS', [
            ('PARCEL', []), ],
    ),
]

FIELDS_MAPPINGS = {
    'PARCELLINGS':
    {
        'factory': [ParcellingFactory],

        'mappers': {

            IdMapper: {
                'from': ('URBLOT_ID',),
                'to': ('id',)
            },

            ParcellingMapper: {
                'table': 'urblot',
                'from': ('URBLOT_ID', 'LOT_NUM', 'LOT_NOM', 'LOT_DATE', 'LOT_NBLOT'),
                'to': ('id', 'label', 'subdividerName', 'authorizationDate', 'numberOfParcels')
            },
        },
    },

    'PARCEL':
    {
        'factory': [ParcelFactory, {'portal_type': 'PortionOut'}],

        'mappers': {
            ParcelsMapper: {
                'table': 'prc_lotiss',
                'KEYS': ('URBLOT_ID', 'PRCL_LOTISID'),
                'mappers': {
                    ParcelDataMapper: {
                        'from': ('PRCL_PRC',),
                        'to': ('division',),
                    },
                },
            },
        },
        # 'mappers': {
        #     ParcelDataMapper: {
        #         'table': 'prc_lotiss',
        #         'from': ('PRCL_PRC',),
        #         'to': ('division'),
        #     },
        # },
    },
}
