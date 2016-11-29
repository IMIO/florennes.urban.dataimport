# -*- coding: utf-8 -*-

"""
Notes:

à reprendre:
    X- zonage au plan de secteur. Dans la table 'prc_data' lien via la parcelle.
    X- PCA , checker la valeur PPA 1, 2 ou 3 de la table 'schema'. les sous valeurs pour la zone de pca sont dans la table 'schemaaff'.
      Encore chercher pour le lien avec les dossiers
    X- Lotissements: regarder les tables 'prc_lotiss', 'lot' (et 'k' 'k2' ??) il ya une colonne dossier_id dans la table 'lot'.
    X- Délai du dossier colonne 'DOSSIER_DELAI' de la table wrkdossier. X => basé sur les valeurs fournies par florennes
    X- Adresse des travaux, vérifier pourquoi ça n'a pas marché.
    X- Enquete publique: EnqDatDeb et Fin bien dans le catalogue mais pas affiché sur le site
        données dans 'wrkparam'
        retrouver le n° du dossier dans k2 (K2_ID = WRKPARAM_ID de 'wrkparam'), l'id du dossier est dans la colonne 'K_ID1' de la table k2
        reprendre "object", articles et date de début et de fin d'enquête
    X- demandes d'avis: table 'wrkavis' colonne '' pour lien avec id du dossier
    X- demande d'avis du FD idem que pour enquête publique (wrkparam rechercher 'avis préalable du FD')
    NA- pour les documents (table cremarq, colonne REAMRQ_DOC):
        regarder l'id CREMARQ_ID, faire correspondre avec k2 dans la colonne K_ID2 (3eme) récuperer l'id du permis dans la 2eme colonne de k2 (K_ID1) : NA => pas de REMARQ_DOC liés aux dossiers :
        SELECT * FROM urb93022ac.wrkdossier AS DOSSIER
        INNER JOIN urb93022ac.k2 AS K2
        ON K2.K_ID1 = DOSSIER.WRKDOSSIER_ID
        INNER JOIN urb93022ac.cremarq AS CRE
        ON K2.K_ID2 = CRE.CREMARQ_ID
        WHERE CRE.REMARQ_DOC IS NOT NULL;

    X- lettres de notaires:
        le classique: parcelle, adresse, ...
        demandeur = notaire
        date octroi de la lettre d'info notariale (event)
        reprendre le document => cremarq nommé 'Annexe 49' X => aucune remarq_lib nommée annexe 49 de près ou de loin.

    A- lettres de notaires (suite):
       X- zonage de plan de secteur
       X- raccordement égouts/voirie suffisament équipées/zone faiblement habitée épuration ind
            => voir param "accordable à l'égout" et "sera accordable à l'égout" dans raccordable-egout et raccordable-egout-prevision
            => voir param "épuration individuelle (?)" ou "zone d'épuration individuelle" dans zone-faiblement-habitee
            => voir param "accès voirie équipée" ou "voirie équipée" dans voirie-suffisamment-equipee

       A- permis accordés pour cette parcelle (dossier lié ?)
       X- titre
       X- adresse postale (dans cloc pour demandeur et notaire)
    A- Divisions
       A- notaire lié (comment trouver le notaire lié hors lettre notariale ?)
    A- Demande de principe
       X- zonage de plan de secteur
       A- rapport du collège
    X- adresse postale des travaux (dans adr)
    A Global
        X Liste des notaires basés sur les CPSN_TYPE 89801 (et ajout si n'existe pas sur les lettres de notaires)
        X EventDateDecision et EventDecision (peu d'infos à ce niveau, pas de match trouvé avec ETAPE comme l'eventDate) => demande chez eux
        X Préchargement des architectes, link de ceux-ci si trouvé (idem que notaires)
        A copie de permis d'urbanisme, url du fichier dans burdoc :
            SELECT * FROM urb93022ac_20160819.wrkdossier AS DOSSIER
                INNER JOIN urb93022ac_20160819.k2 AS K2DOSSIER1
                ON K2DOSSIER1.K_ID1 = DOSSIER.WRKDOSSIER_ID
                INNER JOIN urb93022ac_20160819.k2 AS K2DOSSIER2
                ON K2DOSSIER1.K_ID2 = K2DOSSIER2.K_ID1
                INNER JOIN urb93022ac_20160819.burdoc AS DOC
                ON K2DOSSIER2.K_ID2 = DOC.BURDOC_ID
        ? pièces jointes dans wrkparam

"""

from imio.urban.dataimport.mapping import table

VALUES_MAPS = {
    'type_map': table({
        'header': ['portal_type', 'foldercategory'],
        -88291: ['', ''],  # Abattage d'arbre, ne pas reprendre ces dossiers
        -67348: ['', ''],  # ne pas reprendre ces dossiers (DIVENV)
        -62737: ['ParcelOutLicence', 'lap'],
        -57728: ['', ''],  # ne pas reprendre ces dossiers
        -53925: ['', ''],  # Permis unique, ne pas reprendre ces dossiers
        -52990: ['', ''],  # Article 65, ne pas reprendre ces dossiers
        -49306: ['Article127', ''],
        -46623: ['', ''],  # permis d'environnement classe 3
        -42575: ['BuildLicence', 'uap'],
        -40086: ['ParcelOutLicence', 'lap'],
        -37624: ['', ''],  # permis d'environnement classe 1
        -36624: ['', 'infraction'],  # infractions, ne pas reprendre
        -34766: ['NotaryLetter', ''],  # lettre de notaire
        -28278: ['', ''],  # permis d'environnement classe 1
        -26124: ['ParcelOutLicence', 'lap'],
        -25638: ['MiscDemand', 'dpr'],
        -21454: ['', 'reclam'],  # reclamations, ne pas reprendre
        -20646: ['Article127', ''],
        -19184: ['', ''],  # permis d'environnement classe 2
        -17277: ['BuildLicence', 'uap'],
        -15200: ['Declaration', ''],
        -14333: ['', 'reclam'],  # reclamations, ne pas reprendre
        -14179: ['Division', ''],
        -13467: ['', 'infraction'],  # infractions, ne pas reprendre
        -11889: ['BuildLicence', 'uap'],
        -10362: ['MiscDemand', 'dpr'],  # demande de principe
        -7812: ['Article127', ''],
        -5976: ['', ''],  # permis d'environnement classe 3
        -5753: ['NotaryLetter', ''],  # lettre de notaire
        -3575: ['', ''],  # permis d'environnement classe 2
        -2982: ['UrbanCertificateOne', ''],  # A faire !!!
        -1972: ['ParcelOutLicence', 'lap'],
        0: ['', ''],  # ne pas reprendre ces dossiers
        537481: ['BuildLicence', 'uap'],
        585827: ['ParcelOutLicence', 'lap'],
        596954: ['UrbanCertificateOne', ''],  # A faire !!!
        598613: ['', ''],  # Permis unique classe 1, ne pas reprendre ces dossiers
        598861: ['', ''],  # Permis unqiue classe 2, ne pas reprendre ces dossiers
        599084: ['', ''],  # Classe 3, as reprendre ces dossiers
        600326: ['Division', ''],
        917233: ['BuildLicence', 'uap'], # TODO id présent dans Châtelet (RA-B): type permis d'urbanisme : à valider
        1057715: ['ParcelOutLicence', 'lap'],  # TODO id présent dans Châtelet (RA-L): type permis d'urbanisation : à valider
        3937207: ['', ''],  # Abattage d'arbre, ne pas reprendre ces dossiers
    }),

    # pour la reférence, virer le 'RA' ou 'RG'
    # pour la référence, reprendre la colonne DOSSIER_REFCOM

    # Main dictionaries

    # octroi/refus
    'state_map': {
        -46L: 'refuse',  # -46 = annulé par le FD
        -49L: 'accept',  # -49 = octroyé
        -26L: 'accept',  # -26 = octroyé
        -20L: '',  # chatelet => TODO validate
        -19L: 'retire',  # -19 = périmé
        -14L: 'accept',  # -14 = octroyé
        -12L: 'accept',  # -12 = octroyé (validé par Fl)
        -11L: 'retire',  # -11 = retiré
        -10L: 'retire',  # -10 = retiré (validé par Fl)
        -6L: 'accept',  # -6 = octroyé (validé par Fl)
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
        'header':               ['decision_event', 'folder_complete', 'deposit_event', 'send_licence_applicant_event', 'send_licence_fd_event', 'first_folder_transmitted_to_rw_event'],
        'BuildLicence':         ['delivrance-du-permis-octroi-ou-refus', 'accuse-de-reception', 'depot-de-la-demande', 'envoi-du-permis-au-demandeur', 'envoi-du-permis-au-demandeur', 'envoi-du-permis-au-fd', 'transmis-1er-dossier-rw'],
        'ParcelOutLicence':     ['delivrance-du-permis-octroi-ou-refus', 'accuse-de-reception', 'depot-de-la-demande', 'envoi-du-permis-au-demandeur', 'envoi-du-permis-au-demandeur', 'envoi-du-permis-au-fd', 'transmis-1er-dossier-rw'],
        'Declaration':          ['deliberation-college', '', 'depot-de-la-demande', '', '', ''],
        'Division':             ['decision-octroi-refus', '', 'depot-de-la-demande', '', '', ''],
        'MiscDemand':           ['deliberation-college', '', 'depot-de-la-demande', '', '', ''],
        'UrbanCertificateOne':  ['octroi-cu1', '', 'depot-de-la-demande', '', '', ''],
        'UrbanCertificateTwo':  ['octroi-cu2', '', 'depot-de-la-demande', '', '', ''],
        'NotaryLetter':         ['octroi-lettre-notaire', '', 'depot-de-la-demande', '', '', ''],
        'Article127':           ['delivrance-du-permis-octroi-ou-refus', '', 'depot-de-la-demande', '', '', ''],
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
        89801: 'master',
    },

    # event name map dictionaries
    'event_deposit_name_map': {
        'BuildLicence': [u'récépissé'],
        'ParcelOutLicence': [u'dépôt dossier', u'récépissé'],
        'Article127': [u'Début du dossier', u'dépôt dossier', u'réception de la demande du FD', u'dossier complet'], # dossier complet ask by Florennes
        'NotaryLetter': [u'Réception demande'],
        'UrbanCertificateOne': [u'réception demande'],
        'UrbanCertificateTwo': [u'réception demande'],
        'Declaration': [u'dépôt ou envoi de la déclaration'],
        'Division': [u'Réception avis de division du notaire'],
        'MiscDemand': [u'Accusé de réception', u'réception demande'],
    },

    'event_decision_date_map': {
        'BuildLicence': [u'délivrance permis'],
        'ParcelOutLicence': [u"délivrance modification permis d'urbanisation", u"délivrance permis d'urbanisation" ],
        'Article127': [u'délivrance du permis par le FD ou le Gvt wallon', u'Délivrance permis'],
        'NotaryLetter': '',
        'UrbanCertificateOne': [u'CU1'],
        'UrbanCertificateTwo': [u'CU2'],
        'Declaration': [u'délivrance permis'],
        'Division': [u'délivrance permis'],
        'MiscDemand': [u'Délivrance autorisation'],
    },

    'event_decision_map': {
        'BuildLicence': [u'Octroi du permis'],
        'ParcelOutLicence': [u"octroi du permis d'urbanisation"],
        'Article127': [u'Octroi du permis', u'OctroiPermis' , u'octroi permis'],
        'NotaryLetter': '',
        'UrbanCertificateOne': [u'CU1'],
        'UrbanCertificateTwo': [u'CU2'],
        'Declaration': [u'délivrance permis'],
        'Division': [u'délivrance permis'],
        'MiscDemand': [u'Délivrance autorisation'],
    },

    'event_college_report_date_map': {
        'BuildLicence': [u'rapport Collège avant décision du FD'],
        'Article127': [u'rapport Collège'],
        'Declaration': [u'rapport collège'],
        'MiscDemand': [u'rapport collège', u'Décision du Collège'], # Demande de principe, others
    },

    # Misc. dictionaries

    'solicitOpinionDictionary': {
        u"stp_eau": "stp",
        u"stp": "stp",
        u"stp_voirie": "stp",
        u"base aérienne": "ba",
        u"ddr": "ddr",
        u"sri": "sri",
        u"direction des routes": "spw-dgo1",
        u"x4": "x4",
        u"défense": "defense",
        u"fluxys": "fluxys",
        u"asbl bois du roi": "asblbdr",
        u"cwedd": "cwedd",  # Conseil wallon de l'Environnement pour le Développement durable
        u"elia": "elia",
        u"police": "Police",
        u"tec": "tec",
        u"égouts": "egouts",
        u"ores": "ores",
        u"inasep": "inasep",
        u"dnf": "dnf",
        u"sncb": "sncb",
        u"ccatm": "ccatm",
        u"dgrne": "dgrne",
        u"belgacom": "belgacom",
        u"autres": "autres",
    },

    'zoneDictionary': {
        u"zone d'habitat": "zh",
        u"zone d'habitat à caractère rural": "zhcr",
        u"zone d'habitat à caractère rural sur +/- 50 m et le surplus en zone agricole": "zhcrza",
        u"zone de services publics et d'équipements communautaires": "zspec",
        u"zone de centre d'enfouissement technique": "zcet",
        u"zone de loisirs": "zl",
        u"zones d'activité économique mixte": "zaem",
        u"zones d'activité économique industrielle": "zaei",
        u"zones d'activité économique spécifique agro-économique": "zaesae",
        u"zones d'activité économique spécifique grande distribution": "zaesgd",
        u"zone d'aménagement différé à caractère industriel": "zadci",
        u"zone agricole": "za",
        u"zone forestière": "zf",
        u"zone d'espaces verts": "zev",
        u"zone naturelle": "zn",
        u"zone de parc": "zp",
        u"zone natura 2000": "znatura2000",
        u"zone d'assainissement collectif": "zac",
        u"zone de construction d'habitation fermée": "zchf",
        u"zone de cours et jardins": "zcj",
        u"zone de recul": "zr",
        u"zone forestière d'intérêt paysager": "zfip",
        u"zone faiblement habitée": "zfh",
        u"zone de construction en annexe": "zca",
        u"zone de construction d'habitation semi-ouverte": "zcso",
        u"zone de construction d'habitation ouverte": "zcho",
        u"zone de bâtisses agricoles": "zba",
        u"zone d'habitat dans un périmètre d'intérêt culturel, historique ou esthétique": "zhche",
        u"zone d'habitat à caractère rural sur une profondeur de 50 mètres": "zhcr50",
        u"zone d'habitat à caractère rural sur une profondeur de 40 mètres": "zhcr40",
        u"zone d'extraction": "ze",
        u"zone d'ext. d'habitat": "zeh",
        u"zone d'équipements communautaires et de services publics": "zspec",
        u"zone d'équipement communautaire": "zec",
        u"zone d'assainissement autonome": "zaa",
        u"zone d'aménagement communal concerté mise en oeuvre": "zaccmeo",
        u"zone d'aménagement communal concerté": "zacc",
        u"zone boisée": "zb",
        u"zone artisanale": "zart",
        u"zone agricole pour partie": "zapp",
        u"zone agricole pour le surplus": "zapls",
        u"zone agricole et zone forestière": "zaezf",
        u"zone agricole dans un périmètre d'intérêt paysager pour le surplus": "zapippls",
        u"zone agricole dans un périmètre d'intérêt paysager": "zapip",
        u"voirie": "zv",
        u"sans affectation": "sa",
        u"pv de constat d'infraction": "pvci",
        u"plan d'eau": "pe",
        u"périmètre de réservation sur 75 m de profondeur à partir de l'axe de la voirie": "pr75padlv",
        u"infraction relevée mais sans PV": "pr75irspvpadlv",
        u"aire de faible densité": "afd",
        u"aire de moyenne densité": "amd",
        u"aire de forte densité": "afod",
        u"en partie dans un périmètre de réservation": "eppdr",
        u"déclaré inhabitable": "di",
        u"dans un périmètre d''intérêt culturel, historique ou esthétique": "pche",
        u"dans un périmètre de réservation": "dpdr",
        u"dans un périmètre d'intérêt paysager": "dpip",
        u"faible": "fai",
        u"très faible": "tfai",
        u"eau": "eau",
        u"élevé": "eleve",
        u"éloignée": "eloi",
        u"dossier en cours": "dec",
        u"dans un périmètre d'intérêt culturel, historique ou esthétique": "dupiche",
        u"zone d'habitat sur 50 m de profondeur": "zhas50dp",
    },

    'pcaZoneDictionary' : {
        u"aire de faible densité": "afad",
        u"aire de forte densité": "afod",
        u"aire de moyenne densité": "amd",
        u"dans un périmètre d'intérêt culturel, historique ou esthétique": "dupiche",
        u"dans un périmètre d'intérêt paysager": "dupip",
        u"dans un périmètre de réservation": "dupdr",
        u"déclaré inhabitable": "di",
        u"dossier en cours": "dec",
        u"eau": "eau",
        u"élevé": "eleve",
        u"éloignée": "eloi",
        u"en partie dans un périmètre de réservation": "epdupdr",
        u"faible": "fai",
        u"infraction relevée mais sans pv": "irmspv",
        u"moyen": "moy",
        u"parcs résidentiels": "pres",
        u"périmètre de réservation sur 75 m de profondeur à partir de l'axe de la voirie": "pdrs75mdpapdadlv",
        u"périmètre de zones protégées": "pdzp",
        u"plan d'eau": "peau",
        u"pv de constat d'infraction": "pvdci",
        u"rapprochée": "rapp",
        u"sans affectation": "saffec",
        u"travaux imposés": "timp",
        u"très faible": "tfai",
        u"voirie": "voirie",
        u"zone agricole": "za",
        u"zone agricole dans un périmètre d'intérêt paysager": "zadupip",
        u"zone agricole dans un périmètre d'intérêt paysager pour le surplus": "zadupippsur",
        u"zone agricole et zone de bâtisses agricoles": "zaezba",
        u"zone agricole et zone forestière": "zaezf",
        u"zone agricole pour le surplus": "zaplsur",
        u"zone agricole pour partie": "zapp",
        u"zone artisanale": "zart",
        u"zone boisée": "zb",
        u"zone d'activité économique industrielle": "zaei",
        u"zone d'activité économique mixte": "zaem",
        u"zone d'activités économiques et commerciales": "zaeec",
        u"zone d'aménagement communal concerté": "zacc",
        u"zone d'aménagement communal concerté mise en oeuvre": "zaccmeo",
        u"zone d'assainissement autonome": "zaa",
        u"zone d'assainissement collectif": "zac",
        u"zone d'entreprise commerciale de grande dimension": "zecdgd",
        u"zone d'équipement communautaire": "zec",
        u"zone d'équipements communautaires et de services publics": "zecedsp",
        u"zone d'espaces verts": "zev",
        u"zone d'ext d'industrie": "zexti",
        u"zone d'ext. d'habitat": "zexth",
        u"zone d'ext. d'habitat à caractère rural": "zexthacr",
        u"zone d'ext.. de parcs résidentiels": "zextdpr",
        u"zone d'extension pour bâtisses  espacées": "zexpbe",
        u"zone d'extension pour bâtisses espacées": "zexpbe",
        u"zone d'extraction": "zextract",
        u"zone d'habitat": "zha",
        u"zone d'habitat à caractère rural": "zhaacr",
        u"zone d'habitat à caractère rural sur une profondeur de 40 mètres": "zhaacrsp40",
        u"zone d'habitat à caractère rural sur une profondeur de 50 mètres": "zhaacrsp50",
        u"zone d'habitat dans un périmètre d'intérêt culturel, historique ou esthétique": "zhadupiche",
        u"zone d'habitat sur 50 m de profondeur": "zhas50dp",
        u"zone d'habitation": "zhation",
        u"zone d'habitation, annexes, abris": "zhaaa",
        u"zone de bâtisses agricoles": "zdba",
        u"zone de construction d'habitation fermée": "zdchaf",
        u"zone de construction d'habitation ouverte": "zdchao",
        u"zone de construction d'habitation semi-ouverte": "zdchaso",
        u"zone de construction en annexe": "zdcea",
        u"zone de cours et jardins": "zdcej",
        u"zone de loisirs": "zdl",
        u"zone de parc": "zdparc",
        u"zone de parc ou d'espaces verts": "zdparcev",
        u"zone de prévention en matière de prises d'eau souterraines, zones éloignées.": "zdpemdpeausoutze",
        u"zone de recul": "zdrec",
        u"zone de recul et de voirie": "zdrecedv",
        u"zone de recul, zone de construction d'habitation fermée et zone de cours et jardins": "zdreczdchafeezdcej",
        u"zone de service": "zdserv",
        u"zone de voirie réservée aux piétons": "zdvoirap",
        u"zone de voiries et d'espaces publics": "zdveep",
        u"zone faiblement habitée": "zfaiha",
        u"zone forestière": "zforest",
        u"zone forestière d'intérêt paysager": "zforestip",
        u"zone industrielle": "zi",
        u"zone réservée aux annexes": "zresaa",
        u"zone réservée aux constructions à un étage": "zresacaue",
        u"zone réservée aux constructions principales": "zresacprinc",
        u"zone réservée aux constructions principales, en zone de cours et jardins et en voirie": "zresacprincezcejeev",
    },

    'raw_pca_Dictionary': {
        u"ppa1part": "pca1",
        u"ppa1": "pca1",
        u"ppa1b": "pca1",
        u"ppa1tflo": "pca1",
        u"ppa1tfla": "pca1",
        u"ppa2": "pca2",
        u"ppa2part": "pca2",
        u"ppa2b": "pca2",
        u"ppa3": "pca3",
        u"ppa3part": "pca3",
        u"ppa3mod": "pca3",
    },

}
