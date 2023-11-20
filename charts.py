import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()   #fig: figura ax: coordenadas en las que vamos a graficar
    ax.bar(labels, values)    #genero grafica de barras
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()   #fig: figura ax: coordenadas en las que vamos a graficar
    ax.pie(values, labels=labels)    #genero grafica de pie
    ax.axis("equal")
    plt.show()

if __name__ == "__main__":
    labels = []
    values = []
    cant = int(input("Ingrese cantidad de valores: "))
    i = 0
    while i < cant:
        label = input(f"Ingrese label {i+1}: ")
        labels.append(label)
        value= int(input(f"Ingrese value {i+1}: "))
        values.append(value)
        i += 1

    print(labels)
    print(values)
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)