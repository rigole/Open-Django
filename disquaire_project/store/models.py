from django.db import models

# Create your models here.

ARTISTS = {
    'petit-pays' : {'name': 'Francis Cabrel'},
    'Belka-Tobis': {'name': 'Belka-Tobis'},
    'Ben Decca': {'name': 'Ben Decca'},
    'Jovi': {'name': 'Jovi'},
}

ALBUMS = [
    {'name': 'La monaco', 'artists': [ARTISTS['petit-pays']]},
    {'name': 'Souffrance', 'artists': [ARTISTS['Ben Decca']]},
    {'name': 'solitude', 'artists': [ARTISTS['Belka-Tobis']]},
]