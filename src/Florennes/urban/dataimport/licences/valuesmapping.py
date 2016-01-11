# -*- coding: utf-8 -*-

from imio.urban.dataimport.mapping import table

VALUES_MAPS = {
    'type_map': table({
        'header': ['portal_type',         'foldercategory'],
        -62737: ['',                    ''          ],  # ne pas reprendre ces dossiers
        -57728: ['',                    ''          ],  # ne pas reprendre ces dossiers
        -53925: ['',                    ''          ],  # ne pas reprendre ces dossiers
        -52990: ['',                    ''          ],  # ne pas reprendre ces dossiers
        -49306: ['',                    ''          ],  # ne pas reprendre ces dossiers
        -46623: ['',                    ''          ],  # permis d'environnement classe 3
        -42575: ['BuildLicence',        'uap'       ],
        -40086: ['ParcelOutLicence',    'lap'       ],
        -37624: ['',                    ''          ],  # permis d'environnement classe 1
        -36624: ['',                    'infraction'],  # infractions
        -34766: ['',                    ''          ],  # RN ? notary letter??
        -28278: ['',                    ''          ],  # permis d'environnement classe 1
        -26124: ['ParcelOutLicence',    'lap'       ],
        -25638: ['MiscDemand',          'dpr'       ],
        -21454: ['',                    'reclam'    ],  # reclamations
        -20646: ['BuildLicence',        'art127'    ],
        -19184: ['',                    ''          ],  # permis d'environnement classe 2
        -17277: ['BuildLicence',        'uap'       ],
        -15200: ['Declaration',         ''          ],
        -14333: ['',                    'reclam'    ],  # reclamations
        -14179: ['Division',            ''          ],
        -13467: ['',                    'infraction'],  # infractions
        -11889: ['BuildLicence',        'uap'       ],
        -10362: ['',                    ''          ],  # DP ???
        -7812: ['BuildLicence',        'art127'    ],
        -5976: ['',                    ''          ],  # permis d'environnement classe 3
        -5753: ['',                    ''          ],  # RN ? notary letter??
        -3575: ['',                    ''          ],  # permis d'environnement classe 2
        -2982: ['UrbanCertificateOne', ''          ],
        -1972: ['ParcelOutLicence',    'lap'       ],
    }),
"""
    0
    537481
    585827
    596954
    598613
    598861
    599084
    600326
    3937207
}),
"""

# pour la reférence, virer le 'RA' ou 'RG'
# pour la référence, reprendre la colonne DOSSIER_REFCOM

# octroi/refus
'state_map': {
    -46: 'refuse',  # -46 = annulé par le FD
    -49: 'accept',  # -49 = octroyé
    -26: 'accept',  # -26 = octroyé
    -19: 'retire',  # -19 = périmé
    -14: 'accept',  # -14 = octroyé
    -11: 'retire',  # -11 = retiré
    -5: 'refuse',  # -5 = refusé
    -4: 'retire',  # -4 = suspendu
    -3: 'accept',  # -3 = octroyé
    -2: 'retire',  # -2 = abandonné
    -1: '',  # -1 = en cours
    0: 'refuse',  # -1 = refusé
    1: 'accept',  # 1 = octroyé
},

'division_map': {
    '01': '93022',
    '02': '93013',
    '03': '93021',
    '04': '93045',
    '05': '93063',
    '06': '93033',
    '07': '93064',
    '08': '93044',
    '09': '93077',
    '10': '93031',
    '11': '93032',
},

'titre_map': {
    -1000: 'mister',
    21607: 'misters',
    -1001: 'madam',
    171280: 'ladies',
    -1002: 'miss',
    -1003: 'madam_and_mister',
    676263: 'madam_and_mister',
    850199: 'madam_and_mister',
},

}
