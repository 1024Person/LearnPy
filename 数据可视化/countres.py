from pygal_maps_world.i18n import COUNTRIES
import json


# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code + ':' + COUNTRIES[country_code])
def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif country_name == 'Yemen, Rep.':
            return 'ye'
    return None


if __name__ == '__main__':
    print(get_country_code('Andorra'))
    filename = 'population_data.json'
    countries = set()
    with open(filename) as f:
        reader = json.load(f)
        for country in reader:
            code = get_country_code(country['Country Name'])
            if not code:
                countries.add(country['Country Name'])
    print(len(countries))
