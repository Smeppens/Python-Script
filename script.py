#!/usr/bin/env python
from crud import AnimalShelter

# define data
data = {
    'age_upon_outcome': '3 year',
    'animal_id': 'A66969',
    'animal_type': 'Cat',
    'breed': 'Taby',
    'color': 'White',
    'date_of_birth': '2019-09-05',
    'datetime': '2019-09-04 10:49:00',
    'monthyear': '2019-09-04T10:49:00',
    'name': 'Sorry',
    'outcome_subtype': 'SCRP',
    'outcome_type': 'Transfer',
    'sex_upon_outcome': 'Female',
    'location_lat': 30.6525984560228,
    'location_long': -97.7419963476444,
    'age_upon_outcome_in_weeks': 52.9215277777778,
    }

# define search criteria
search = {'animal_id': 'A66969'}

# instantiate an object of AnimalShelter class
assignment = AnimalShelter('aacuser', 'pass123')

# call the create method
success = assignment.create(data)
print (success)

# call the read method
results = assignment.read(search)
print (results)
