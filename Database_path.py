'''
In diesem Modul wird der Pfad der Datenbank initialisiert. Diese kann dann von anderen Funktionen aus aufgerufen werden
'''

import os


# Funktion: Verzeichnis der Datenbank festlegen, damit andere Funktionen/Methoden darauf zugreifen können
def database_path():
    # Das Verzeichnis des Projektordners
    project_dir = os.path.dirname(os.path.abspath(__file__))

    # Verzeichnis der Datenbank im Projektordner
    path_db = os.path.join(project_dir, 'Database.db')

    return path_db
