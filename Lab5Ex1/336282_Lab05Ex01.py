# Author: S336282
# Computer Programming in Python, A.A. 2024/25
# Lab Practice 05, Part 1 Summary exercises, 05.1.2 Noms des pays

## Add an article to country names
# @param country {string} - the country word
# @return {string} - new string with an article before the country's word
def nomsDePays(country):
    if country in 'États-Unis Pays-Bas':
        return 'les ' + country
    if country in 'Belize Cambodge Mexique Mozambique Zaïre Zimbabwe':
        return 'le ' + country

    firstChar = country[0].lower()
    if firstChar in 'aiueèéo':
        return 'l\'' + country
    
    wordLength = len(country)
    lastChar = country[wordLength-1].lower()
    if lastChar in 'eèé':
        return 'la ' + country
    
    
    return 'le ' + country

def s336282_nomsDePaysExercise():
    inputCountry = input('Enter the country name: ')
    print(nomsDePays(inputCountry))

s336282_nomsDePaysExercise()

## Assert nomsDePays function if it adds the correct article to the country name
countries = ['Afghanistan', 'Belize', 'Belgique', 'Cambodge', 'Canada', 'Mexique', 'Mozambique', 'Zaïre', 'Zimbabwe', 'États-Unis', 'Pays-Bas']
expectedCountries = ['l\'Afghanistan', 'le Belize', 'la Belgique', 'le Cambodge', 'le Canada', 'le Mexique', 'le Mozambique', 'le Zaïre', 'le Zimbabwe', 'les États-Unis', 'les Pays-Bas']

actualCountries = [nomsDePays(country) for country in countries]

assert actualCountries == expectedCountries
