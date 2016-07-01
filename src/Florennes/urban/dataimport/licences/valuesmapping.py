# -*- coding: utf-8 -*-

"""
Notes:

à reprendre:
    - zonage au plan de secteur. Dans la table 'prc_data' lien via la parcelle. X
    - PCA , checker la valeur PPA 1, 2 ou 3 de la table 'schema'. les sous valeurs pour la zone de pca sont dans la table 'schemaaff'.
      Encore chercher pour le lien avec les dossiers X
    - Lotissements: regarder les tables 'prc_lotiss', 'lot' (et 'k' 'k2' ??) il ya une colonne dossier_id dans la table 'lot'. X
    - Délai du dossier colonne 'DOSSIER_DELAI' de la table wrkdossier. X => basé sur les valeurs fournies par florennes
    - Adresse des travaux, vérifier pourquoi ça n'a pas marché. C
    - Enquete publique:
        données dans 'wrkparam'
        retrouver le n° du dossier dans k2 (K2_ID = WRKPARAM_ID de 'wrkparam'), l'id du dossier est dans la colonne 'K_ID1' de la table k2
        reprendre "object", articles et date de début et de fin d'enquête X
    - demandes d'avis: table 'wrkavis' colonne 'AVIS_DOSSIERID' pour lien avec id du dossier X
    - demande d'avis du FD idem que pour enquête publique (wrkparam rechercher 'avis préalable du FD') C
    - pour les documents (table cremarq, colonne REAMRQ_DOC):
        regarder l'id CREMARQ_ID, faire correspondre avec k2 dans la colonne K_ID2 (3eme) récuperer l'id du permis dans la 2eme colonne de k2 (K_ID1) : NA => pas de REMARQ_DOC liés aux dossiers :
        SELECT * FROM urb93022ac.wrkdossier AS DOSSIER
        INNER JOIN urb93022ac.k2 AS K2
        ON K2.K_ID1 = DOSSIER.WRKDOSSIER_ID
        INNER JOIN urb93022ac.cremarq AS CRE
        ON K2.K_ID2 = CRE.CREMARQ_ID
        WHERE CRE.REMARQ_DOC IS NOT NULL;

    - lettres de notaires:
        le classique: parcelle, adresse, ...
        demandeur = notaire
        reprendre le document => cremarq nommé 'Annexe 49' C => aucune remarq_lib nommée annexe 49 de près ou de loin.
"""

from imio.urban.dataimport.mapping import table

VALUES_MAPS = {
    'type_map': table({
        'header': ['portal_type',         'foldercategory'],
        -62737: ['ParcelOutLicence',    'lap'       ],
        -57728: ['',                    ''          ],  # ne pas reprendre ces dossiers
        -53925: ['',                    ''          ],  # Permis unique, ne pas reprendre ces dossiers
        -52990: ['',                    ''          ],  # Article 65, ne pas reprendre ces dossiers
        -49306: ['Article127',          ''          ],
        -46623: ['',                    ''          ],  # permis d'environnement classe 3
        -42575: ['BuildLicence',        ''          ],
        -40086: ['ParcelOutLicence',    'lap'       ],
        -37624: ['',                    ''          ],  # permis d'environnement classe 1
        -36624: ['',                    'infraction'],  # infractions, ne pas reprendre
        -34766: ['NotaryLetter',        ''          ],  # lettre de notaire, à faire!!
        -28278: ['',                    ''          ],  # permis d'environnement classe 1
        -26124: ['ParcelOutLicence',    'lap'       ],
        -25638: ['MiscDemand',          'dpr'       ],
        -21454: ['',                    'reclam'    ],  # reclamations, ne pas reprendre
        -20646: ['Article127',          ''          ],
        -19184: ['',                    ''          ],  # permis d'environnement classe 2
        -17277: ['BuildLicence',        'uap'       ],
        -15200: ['Declaration',         ''          ],
        -14333: ['',                    'reclam'    ],  # reclamations, ne pas reprendre
        -14179: ['Division',            ''          ],
        -13467: ['',                    'infraction'],  # infractions, ne pas reprendre
        -11889: ['BuildLicence',        'uap'       ],
        -10362: ['BuildLicence',        'uap'       ],  #  déclaration préalabe
        -7812: ['Article127',           ''          ],
        -5976: ['',                     ''          ],  # permis d'environnement classe 3
        -5753: ['NotaryLetter',         ''          ],  # lettre de notaire, à faire!!
        -3575: ['',                     ''          ],  # permis d'environnement classe 2
        -2982: ['UrbanCertificateOne',  ''          ],  # A faire !!!
        -1972: ['ParcelOutLicence',     'lap'       ],
        0: ['',                         ''          ],  # ne pas reprendre ces dossiers
        537481: ['BuildLicence',        'uap'       ],
        585827: ['ParcelOutLicence',    'lap'       ],
        596954: ['UrbanCertificateOne', ''          ], # A faire !!!
        598613: ['',                    ''          ],  # Permis unique classe 1, ne pas reprendre ces dossiers
        598861: ['',                    ''          ],  # Permis unqiue classe 2, ne pas reprendre ces dossiers
        599084: ['',                    ''          ],  # Classe 3, as reprendre ces dossiers
        600326: ['Division',            ''          ],
        3937207: ['',                   ''          ],  # Abattage d'arbre, ne pas reprendre ces dossiers
    }),

# pour la reférence, virer le 'RA' ou 'RG'
# pour la référence, reprendre la colonne DOSSIER_REFCOM

# octroi/refus
'state_map': {
    -46L: 'refuse',  # -46 = annulé par le FD
    -49L: 'accept',  # -49 = octroyé
    -26L: 'accept',  # -26 = octroyé
    -19L: 'retire',  # -19 = périmé
    -14L: 'accept',  # -14 = octroyé
    -11L: 'retire',  # -11 = retiré
    -5L: 'refuse',  # -5 = refusé
    -4L: 'retire',  # -4 = suspendu
    -3L: 'accept',  # -3 = octroyé
    -2L: 'retire',  # -2 = abandonné
    -1L: '',  # -1 = en cours
    0L: 'refuse',  # -1 = refusé
    1L: 'accept',  # 1 = octroyé
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

'eventtype_id_map': table({
    'header'             : ['decision_event',                       'folder_complete',     'deposit_event',       'send_licence_applicant_event', 'send_licence_fd_event', 'first_folder_transmitted_to_rw_event'],
    'BuildLicence'       : ['delivrance-du-permis-octroi-ou-refus', 'accuse-de-reception', 'depot-de-la-demande', 'envoi-du-permis-au-demandeur', 'envoi-du-permis-au-fd', 'transmis-1er-dossier-rw'],
    'ParcelOutLicence'   : ['delivrance-du-permis-octroi-ou-refus', 'accuse-de-reception', 'depot-de-la-demande', 'envoi-du-permis-au-demandeur', 'envoi-du-permis-au-fd', 'transmis-1er-dossier-rw'],
    'Declaration'        : ['deliberation-college',                 '',                    'depot-de-la-demande', '', '', 'deliberation-college'],
    'Division'           : ['decision-octroi-refus',                '',                    'depot-de-la-demande', '', '', 'decision-octroi-refus'],
    'MiscDemand'         : ['deliberation-college',                 '',                    'depot-de-la-demande', '', '', 'deliberation-college'],
    'UrbanCertificateOne': ['octroi-cu1',                           '',                    'depot-de-la-demande', '', '', 'octroi-cu1'],
    'UrbanCertificateTwo': ['octroi-cu2',                           '',                    'depot-de-la-demande', '', '', 'octroi-cu2'],
    'NotaryLetter'       : ['octroi-lettre-notaire',                '',                    'depot-de-la-demande', '', '', 'octroi-lettre-notaire'],
}),

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
