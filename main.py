import pandas as pd
import matplotlib.pyplot as plt
from os import system
system('cls')

# Poner la ruta del .csv para que funcione correctamente
filePath = 'game_sales.csv'
db = pd.read_csv(filePath)

# Primer grafico
def mainGenreGraph():
    # Variables utilizadas
    x = db.loc[db['Year'] == 2017].sort_values(by='Global_Sales',ascending=False)['Genre']
    y = db.loc[db['Year'] == 2017].sort_values(by='Global_Sales',ascending=False)['Global_Sales']
    colors = []
    for genre in x:
        if genre == x.iloc[0]:
            colors.append('g')
        else: colors.append('gray')
    
    # Creación del gráfico
    fig,ax = plt.subplots()
    fig.set_size_inches(16,9)
    bars = ax.bar(x,y,color=colors)
    ax.set_title('Género Principal',fontdict={'fontsize':25,'fontweight':'bold'},pad=25)
    ax.set_xlabel('Géneros',fontsize=22,labelpad=15)
    ax.set_ylabel('Ventas Globales (2017)',fontsize=20,labelpad=15)
    fig.subplots_adjust(bottom=0.2)
    for bar in bars:
        xcoord = bar.get_x()
        ycoord = bar.get_height()
        ax.annotate(ycoord,xy=(xcoord+(bar.get_width()/2),ycoord+0.5),ha='center',color='gray')
    # Exportar imágen
    fig.savefig('genero_principal.png')
    print('Imagen guardada.')
    # Desplegar gráfico
    plt.show()

# Segundo grafico
def subGenreGraph():
    # Variables utilizadas
    x = db.loc[db['Year'] == 2020].sort_values(by='EU_Sales',ascending=False)['Genre']
    y = db.loc[db['Year'] == 2020].sort_values(by='EU_Sales',ascending=False)['EU_Sales']
    colors = []
    for i in x:
        if i == x.iloc[4]:
            colors.append('g')
        else: colors.append('gray')

    # Creación del gráfico
    fig,ax = plt.subplots()
    fig.set_size_inches(16,9)
    bars = ax.bar(x,y,color=colors)
    ax.set_title('Subgénero',fontdict={'fontsize':25,'fontweight':'bold'},pad=25)
    ax.set_xlabel('Géneros',fontsize=22,labelpad=15)
    ax.set_ylabel('Ventas EU (2020)',fontsize=20,labelpad=15)
    fig.subplots_adjust(bottom=0.2)
    for bar in bars:
        xcoord = bar.get_x()
        ycoord = bar.get_height()
        ax.annotate(ycoord,xy=(xcoord+(bar.get_width()/2),ycoord+0.3),ha='center',color='gray')
    # Exportar imágen
    fig.savefig('subgenero.png')
    print('Imagen guardada.')
    # Desplegar gráfico
    plt.show()

# Tercer grafico
def inversionGraph():
    ventasGlobales = db['Global_Sales'].sum()
    ventasNA = db['NA_Sales'].sum()/ventasGlobales*100
    ventasJP = db['JP_Sales'].sum()/ventasGlobales*100
    ventasEU = db['EU_Sales'].sum()/ventasGlobales*100
    fig,ax = plt.subplots()
    slices = [ventasEU,ventasJP,ventasNA]
    lbls = ['Europa','Japón','Norte América']
    colors = ['#A3F3FF','#CACFFF','#F1ABFF']
    ax.pie(slices,labels=lbls,autopct='%1.1f%%',colors=colors)
    ax.set_title('Porcentajes de ventas | Inversión',fontdict={'fontsize':20,'fontweight':'bold'})
    fig.savefig('inversion.png')
    print('Imagen guardada.')
    plt.show()

# Ejecución de funciones
mainGenreGraph()
subGenreGraph()
inversionGraph()