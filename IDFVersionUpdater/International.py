class Languages:
    English = 'english'
    Spanish = 'spanish'
    French = 'french'


CurrentLanguage = Languages.English


def set_language(lang):
    global CurrentLanguage
    CurrentLanguage = lang


EnglishDictionary = {
    'ABOUT_DIALOG': 'This program was created by NREL for the United States Department of Energy.',
    'Choose File to Update...': 'Choose File to Update...',
    'About...': 'About...',
    'File Path': 'File Path',
    'You must restart the app to make the language change take effect.  Would you like to restart now?':
        'You must restart the app to make the language change take effect.  Would you like to restart now?',
    'Old Version': 'Old Version',
    'Keep Original Version?': 'Keep Original Version?',
    'Update File': 'Update File',
    'Close': 'Close',
    'Program Initialized': 'Program Initialized',
    'Running Transition': 'Running Transition',
    'Transition Cancelled': 'Transition Cancelled',
    'Completed Transition': 'Completed Transition',
    'Failed Transition': 'Failed Transition',
    'All transitions completed successfully - Open run directory for transitioned file':
        'All transitions completed successfully - Open run directory for transitioned file',
    'Could not open run directory': 'Could not open run directory',
    'Open Run Directory': 'Open Run Directory',
}

SpanishDictionary = {
    'ABOUT_DIALOG': 'Este programa fue creado por el NREL para el Departamento de Energia de los Estados Unidos.',
    'Choose File to Update...': 'Elegir archivo para actualizar ...',
    'About...': 'Acerca de...',
    'File Path': 'Ruta de archivo',
    'You must restart the app to make the language change take effect.  Would you like to restart now?':
        'Debe reiniciar la aplicacion para que el cambio de idioma tenga efecto. Le gustaria reiniciar ahora?',
    'Old Version': 'Version antigua',
    'Keep Intermediate Versions?': 'Mantener versiones intermedias?',
    'Update File': 'Actualizar archivo',
    'Close': 'Cerca',
'Program Initialized': 'Program Initialized',
    'Running Transition': 'Running Transition',
    'Transition Cancelled': 'Transition Cancelled',
    'Completed Transition': 'Completed Transition',
    'Failed Transition': 'Failed Transition',
    'All transitions completed successfully - Open run directory for transitioned file':
        'All transitions completed successfully - Open run directory for transitioned file',
    'Could not open run directory': 'Could not open run directory',
    'Open Run Directory': 'Open Run Directory',
}


FrenchDictionary = {
    'ABOUT_DIALOG': 'Ce logiciel a ete cree par NREL pour United States Department of Energy.',
    'Choose File to Update...': 'Choisissez Fichier pour mettre a jour ...',
    'About...': 'Sur...',
    'File Path': 'Chemin du fichier',
    'You must restart the app to make the language change take effect.  Would you like to restart now?':
        'Vous devez relancer le logiciel pour effectuer le changement de langue. Voulez-vous relancer maintenant?',
    'Old Version': 'Ancienne version',
    'Keep Intermediate Versions?': 'Gardez Versions intermediaires?',
    'Update File': 'Mise a jour de fichiers',
    'Close': 'Fermer',
'Program Initialized': 'Program Initialized',
    'Running Transition': 'Running Transition',
    'Transition Cancelled': 'Transition Cancelled',
    'Completed Transition': 'Completed Transition',
    'Failed Transition': 'Failed Transition',
    'All transitions completed successfully - Open run directory for transitioned file':
        'All transitions completed successfully - Open run directory for transitioned file',
    'Could not open run directory': 'Could not open run directory',
    'Open Run Directory': 'Open Run Directory',
}


def report_missing_keys():
    base_keys = EnglishDictionary.keys()
    for dict_name, dictionary in {'Spanish': SpanishDictionary, 'French': FrenchDictionary}.iteritems():  # add here
        print("Processing missing keys from dictionary: " + dict_name)
        for key in base_keys:
            if key not in dictionary:
                print("Could not find key: \"%s\"" % key)


def translate(key):
    # if for some reason blank, just return blank
    if key is None or key == "":
        return ""

    # start with English, but switch based on language
    dictionary = EnglishDictionary
    if CurrentLanguage == Languages.Spanish:
        dictionary = SpanishDictionary
    elif CurrentLanguage == Languages.French:
        dictionary = FrenchDictionary

    # if the key is there, return it, otherwise return a big flashy problematic statement
    if key in dictionary:
        return dictionary[key]
    else:
        print("Could not find this key in the dictionary: \"%s\"" % key)
        return "TRANSLATION MISSING"
