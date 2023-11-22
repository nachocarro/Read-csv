import utils
import read_csv
import charts
import pandas as pd


def run():

    df = pd.read_csv("/home/ignaciomcarro/Proyectos-python/read-csv/data.csv")     #obtengo la informacion con Pandas

    option = input("Desea filtrar por ranking (Rank) o continente (Continent): ")
    option = option.title()

    if option == "Rank":
        rank = input("Ingrese el valor maximo del ranking: ")

        #data_pie = list(filter(lambda country : int(country["Rank"]) <= int(rank), data))
        df = df[df["Rank"] <= int(rank)]

        name = f"Ranking de los primeros {rank} paises"
    elif option == "Continent":
        continent = input("Ingrese un continente: ")
        continent = continent.title()

        #data_pie = list(filter(lambda country : country["Continent"] == continent, data))
        df = df[df["Continent"] == continent]

        name = f"{continent}"

    #countries = list(map(lambda country: country["Country/Territory"], data_pie))
    countries = df["Country/Territory"].values                                         #te entrega los valores de la columna

    #world_pop = list(map(lambda country: country["World Population Percentage"],data_pie))
    world_pop = df["World Population Percentage"].values


    charts.generate_pie_chart(name, countries, world_pop)

    data = read_csv.read_csv("/home/ignaciomcarro/Proyectos-python/read-csv/data.csv")
    
    country= input("Ingrese el pais deseado: ")
    country = country.title()
    name_country = country

    country_list = utils.population_by_country(data, country)

    if len(country_list) > 0:
        country = country_list[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(name_country, labels, values)
    else:
        print("El pais ingresado no se encuentra en la lista")



if __name__ == "__main__":             #para poder ejecutar el archivo desde aqui
    run()
