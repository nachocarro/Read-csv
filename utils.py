def get_population(country):
    #print(country)

    country_dict = {
        "1970" : int(country['1970 Population']),          #pop.append(int(country['1970 Population']))
        "1980" : int(country['1980 Population']),
        "1990" : int(country['1990 Population']),
        "2000" : int(country['2000 Population']),
        "2010" : int(country['2010 Population']),
        "2020" : int(country['2020 Population']),
        "2022" : int(country['2022 Population'])
    }

    years = country_dict.keys()
    pop = country_dict.values()
    print(years)
    print(pop)
    return years, pop

def population_by_country(data, country):
    result_list = list(filter(lambda i: i["Country/Territory"] == country, data))
    return result_list

def world_population(data):
    countries = []
    world_pop = []
    for country in data:
        countries.append(country["Country/Territory"])
        world_pop.append(country["World Population Percentage"])
    print(countries)
    print(world_pop)
    return countries, world_pop

