import utils
import read_csv
import charts


def run():
    data = read_csv.read_csv("\\Users\\ignac\\OneDrive\\Documents\\Python\\app\\data.csv")

    """
    option = input("Desea filtrar por ranking (Rank) o continente (Continent): ")
    option = option.title()

    if option == "Rank":
        rank = input("Ingrese el valor maximo del ranking: ")
        data = list(filter(lambda country : int(country["Rank"]) <= int(rank), data))
    elif option == "Continent":
        continent = input("Ingrese un continente: ")
        data = list(filter(lambda country : country["Continent"] == continent, data))

    countries = list(map(lambda country: country["Country/Territory"], data))
    world_pop = list(map(lambda country: country["World Population Percentage"],data))
    charts.generate_pie_chart(countries, world_pop)
    """

    country= input("Ingrese el pais deseado: ")
    country = country.title()

    country_list = utils.population_by_country(data, country)

    if len(country_list) > 0:
        country = country_list[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)
    else:
        print("El pais ingresado no se encuentra en la lista")


if __name__ == "__main__":             #para poder ejecutar el archivo desde aqui
    run()
