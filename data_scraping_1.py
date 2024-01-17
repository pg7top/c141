from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


bright_stars_url = 'https://pt.wikipedia.org/wiki/Lista_das_estrelas_mais_brilhantes'

#Acesse o conteúdo da página através de page
page = requests.get(bright_stars_url)

#Use o interpretador BS4
soup = bs(page.text,'html.parser')

#Encontre a tabela de classe 'wikitable'
star_table = soup.find('table',attrs={'class':'wikitable'})


#Crie uma lista temporária vazia, onde você vai armazenar os dados buscados
temp_list= []

#Encontre as linhas da tabela
table_rows = star_table.find_all('tr')


#Use um laço for para extrair os dados da lista e adicione os dados a lista temporária
for tr in table_rows:
    td = tr.find_all('td')

    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

#Listas que irão armazenar dados do dataframe
Star_names = []
Constelation = []
Magnitude_Ap = []
Bayer = []
Classification_esp = []
Distance =[]

#Adicione os dados a suas respectivas listas
for i in range(1,len(temp_list)):
    ##Adicione aqui seu código
    Star_names.append(temp_list[i][1])
    Constelation.append(temp_list[i][2])
    Magnitude_Ap.append(temp_list[i][3])
    Bayer.append(temp_list[i][4])
    Classification_esp.append(temp_list[i][5])
    Distance.append(temp_list[i][6])
#Cabeçalho do dataframe
headers = ['Nome da estrela', 'Constelação', 'Magnitude_Ap', 'Bayer', 'Classificação','Distância']

#Crie o Dataframe
df1 = pd.DataFrame(list(zip(Star_names,Constelation,Magnitude_Ap,Bayer,Classification_esp,Distance)), columns=headers)
print(df1)

df1.to_csv('estrelas_mais_brilhantes.csv')



