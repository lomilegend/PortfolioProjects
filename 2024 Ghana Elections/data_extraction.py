import requests
from bs4 import BeautifulSoup
import pandas 



# url to scrape(Wikipedia US Companies Revenue)
# url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

# response = requests.get(url)

# show = BeautifulSoup(response.text,'html.parser')

# # a = show.find('table',class_="wikitable sortable jquery-tablesorter")

# table = show.find_all('table')[0]

# table_h = table.find_all('th')

# a = [i.text.strip() for i in table_h]

# # b= [i.get_text(separator=" ").strip() for i in table_h]

# table_r = table.find_all('td')

# c = [j.text.strip() for j in table_r]

# list_data = [c[j:j+7] for j in range(0, len(c), 7)]

# table_data = pandas.DataFrame(list_data, columns = a)



# print(table_data)

# # url to scrape (Ghana 2024 Elections Data)
url = "https://en.wikipedia.org/wiki/2024_Ghanaian_general_election"

url_1 = "https://en.wikipedia.org/wiki/List_of_MPs_elected_in_the_2024_Ghanaian_general_election"

url_2 = "https://en.wikipedia.org/wiki/List_of_parliamentary_constituencies_of_Ghana"

url_3 = "https://en.wikipedia.org/wiki/2020_Ghanaian_general_election"

url_4 = "https://en.wikipedia.org/wiki/List_of_political_parties_in_Ghana"




response = requests.get(url)

show = BeautifulSoup(response.text,'html.parser')

response_1 = requests.get(url_1)

show_1 = BeautifulSoup(response_1.text,'html.parser')

response_2 = requests.get(url_2)

show_2 = BeautifulSoup(response_2.text,'html.parser')

response_3 = requests.get(url_3)

show_3 = BeautifulSoup(response_3.text,'html.parser')

response_4 = requests.get(url_4)

show_4 = BeautifulSoup(response_4.text,'html.parser')

#Presidentail Candidate List

pres_list = show.find_all('table')[13]

pres_list_h = pres_list.find_all('th')

pres_list_r = pres_list.find_all('td')

d1 = [th.text.strip() for th in pres_list_h]

d2 = [th.text.strip() for th in pres_list_r]

d3 = [d2[i:i+5] for i in range(0,len(d2),5) ]


data_1 = pandas.DataFrame(d3,columns=d1)

# data_1.to_csv(r'C:\Users\justi\Desktop\Power BI\Project\Ghana Election 2024\data_1.csv',index=False)


#2024Presidential Polls Results

# url to scrape (Ghana 2024 Elections Data2)


polls_list = show.find_all('table')[14]

polls_list_h = polls_list.find_all('th')

polls_list_r = polls_list.find_all('td')

d4 = [th.text.strip() for th in polls_list_h[:5]]
d4 = ['Empty'] + d4[:-1]


d5 = [th.text.strip() for th in polls_list_r]

d6 = [d5[i:i+5] for i in range(1,len(d5),6) ]


data_2 = pandas.DataFrame(d6,columns=d4)

# data_2.to_csv(r'C:\Users\justi\Desktop\Power BI\Project\Ghana Election 2024\data_2.csv',index=False)


#2024Presidential Polls by Region Results

reg_list = show.find_all('table')[15]

reg_list_h = reg_list.find_all('th')

reg_list_r = reg_list.find_all('td')

d7 = [th.text.strip() for th in reg_list_h[:13]]



d8 = [th.text.strip() for th in reg_list_r]

d9 = [d8[i:i+13] for i in range(0,len(d8),13)]


data_3 = pandas.DataFrame(d9,columns=d7)

# data_3.to_csv(r'C:\Users\justi\Desktop\Power BI\Project\Ghana Election 2024\data_3.csv',index=False)



#Parlimentary Polls by  Results

par_list = show_1.find_all('table')[4]

par_list_h = par_list.find_all('th')

par_list_r = par_list.find_all('td')

d10 = [th.text.strip() for th in par_list_h[:6]]



d11 = [th.text.strip() for th in par_list_r]

# Filter out elements containing the word 'seats'
filtered_list = [item for item in d11 if 'seats' not in item]

d12 = [filtered_list[i:i+6] for i in range(0,len(filtered_list),6)]




data_4 = pandas.DataFrame(d12,columns=d10)

# data_4.to_csv(r'C:\Users\justi\Desktop\Power BI\Project\Ghana Election 2024\data_4.csv',index=False)


#List of Constituencies


con_list = show_2.find_all('table')[8]

con_list_h = con_list.find_all('th')

con_list_r = con_list.find_all('td')

d13 = [th.text.strip() for th in con_list_h]

d14 = [th.text.strip() for th in con_list_r]

# d15 = [d14[i:i+4] for i in range(0,len(d14),4)]


# con_list_16 = ['Ahanta West Municipal', 'Agona Ahanta', 'Ahanta West', '', 
# 'Amenfi Central', 'Manso', 'Amenfi Central', '', 
# 'Amenfi West Municipal', 'Asankragua', 'Amenfi West', '', 
# 'Effia Kwesimintsim Municipal[11]', 'Kwesimintsim', 'Effia', '', 
# 'Effia Kwesimintsim Municipal[11]', 'Kwesimintsim',  'Kwesimintsim[11]', 'Created 2012', 
# 'Ellembelle', 'Nkroful', 'Ellembelle', '', 
# 'Jomoro Municipal', 'Half Assini', 'Jomoro', '', 
# 'Mpohor', 'Mpohor', 'Mpohor', 'Created 2012', 
# 'Nzema East Municipal', 'Axim', 'Evalue Gwira Evalue-Gwira', '', 
# 'Prestea-Huni Valley Municipal', 'Bogoso', 'Prestea-Huni Valley', 'Created 2008', 
# 'Sekondi Takoradi Metropolitan', 'Sekondi-Takoradi', 'Essikado-Ketan', 'Created 2004', 
# 'Sekondi Takoradi Metropolitan', 'Sekondi-Takoradi', 'Sekondi', '',
# 'Sekondi Takoradi Metropolitan', 'Sekondi-Takoradi', 'Takoradi', '', 
# 'Shama', 'Shama', 'Shama', '',
# 'Tarkwa-Nsuaem Municipal', 'Tarkwa', 'Tarkwa-Nsuaem', '', 
# 'Wassa Amenfi East Municipal', 'Wassa-Akropong', 'Amenfi East', '', 
# 'Wassa East', 'Daboase', 'Wassa East', '']


# con_list_3 = ['Adansi Asokwa', 'Adansi Asokwa', 'Adansi-Asokwa', '', 
# 'Adansi North', 'Fomena', 'Fomena', '', 
# 'Adansi South', 'New Edubiase', 'New Edubease', '', 
# 'Afigya Kwabre North', 'Boamang', 'Afigya Kwabre North', '', 
# 'Afigya Kwabre South', 'Kodie', 'Afigya Kwabre South', '', 
# 'Ahafo Ano North Municipal', 'Tepa', 'Ahafo Ano North', '', 
# 'Ahafo Ano South East', 'Dwinyame / Adugyama', 'Ahafo Ano South East', 'Created 2012', 
# 'Ahafo Ano South West', 'Mankranso', 'Ahafo Ano South West', '', 
# 'Akrofuom', 'Akrofuom', 'Akrofuom', 'Created 2004', 
# 'Amansie Central', 'Jacobu', 'Odotobri', '', 
# 'Amansie West', 'Manso Nkwanta', 'Manso Nkwanta', '', 
# 'Amansie South', 'Manso Adubia', 'Manso Edubia', 'Created 2012', 
# 'Asante Akim Central Municipal', 'Konongo', 'Asante Akim Central', '', 
# 'Asante Akim North', 'Agogo', 'Asante Akim North', 'Created 2012', 
# 'Asante Akim South Municipal', 'Juaso', 'Asante Akim South', '', 
# 'Asokore Mampong', 'Asokore Mampong', 'Asawase', 'Created 2004', 
# 'Asokwa Municipal', 'Asokwa', 'Asokwa', '', 
# 'Atwima Kwanwoma', 'Twedie', 'Atwima-Kwanwoma', '', 
# 'Atwima Mponua', 'Nyinahin', 'Atwima Mponua', '', 
# 'Atwima Nwabiagya Municipal', 'Nkawie', 'Atwima-Nwabiagya South', '', 
# 'Atwima Nwabiagya North', 'Barekese', 'Atwima-Nwabiagya North', 'Created 2012', 
# 'Bekwai Municipal', 'Bekwai', 'Bekwai', '', 
# 'Bosome Freho', 'Asiwa', 'Bosome-Freho', '', 
# 'Bosomtwe', 'Kuntanse', 'Bosomtwe', '', 
# 'Ejisu Municipal', 'Ejisu', 'Ejisu', '', 
# 'Ejura Sekyedumase Municipal', 'Ejura', 'Ejura-Sekyedumase', '', 
# 'Juaben Municipal', 'Juaben', 'Juaben', 'Created 2012', 
# 'Kumasi Metropolitan', 'Kumasi', 'Bantama', '',  
# 'Kumasi Metropolitan', 'Kumasi','Manhyia North', 'Created 2012', 
# 'Kumasi Metropolitan', 'Kumasi', 'Manhyia South', '',  
# 'Kumasi Metropolitan', 'Kumasi', 'Nhyiaeso', 'Created 2004', 
# 'Kumasi Metropolitan', 'Kumasi', 'Subin', '', 
# 'Kwabre East Municipal', 'Mamponteng', 'Kwabre East', '', 
# 'Kwadaso Municipal', 'Kwadaso', 'Kwadaso', 'Created 2004', 
# 'Mampong Municipal', 'Mampong', 'Mampong', '', 
# 'Obuasi East Municipal', 'Tutuka', 'Obuasi East', 'Created 2012', 
# 'Obuasi Municipal', 'Obuasi', 'Obuasi West', '', 
# 'Offinso Municipal', 'Offinso', 'Offinso South', '', 
# 'Offinso North', 'Akomadan', 'Offinso North', '', 
# 'Oforikrom Municipal', 'Oforikrom', 'Oforikrom', '', 
# 'Old Tafo Municipal', 'Old Tafo', 'Old Tafo', 'Created 2004', 
# 'Sekyere Afram Plains', 'Drobonso', 'Sekyere Afram Plains', 'Created 2012', 
# 'Sekyere Central', 'Nsuta', 'Nsuta-Kwamang', '', 
# 'Sekyere East', 'Effiduase', 'Afigya Sekyere East', '', 
# 'Sekyere Kumawu', 'Kumawu', 'Kumawu', '', 
# 'Sekyere South', 'Agona', 'Effiduase-Asokore', '', 
# 'Suame Municipal', 'Suame', 'Suame', 'Created 2004']


# con_list_6 = ['Abura Asebu Kwamankese', 'Abura-Dunkwa', 'Abura-Asebu-Kwamankese', '', 
# 'Agona East', 'Nsaba', 'Agona East', '', 
# 'Agona West Municipal', 'Agona Swedru', 'Agona West', '', 
# 'Ajumako Enyan Essiam', 'Ajumako', 'Ajumako-Enyan-Essiam', '', 
# 'Asikuma Odoben Brakwa', 'Breman Asikuma', 'Asikuma-Odoben-Brakwa', '', 
# 'Assin Central Municipal', 'Assin Foso', 'Assin Central', 'Created 2012', 
# 'Assin North', 'Assin Bereku', 'Assin North', '', 
# 'Assin South', 'Nsuaem Kyekyewere', 'Assin South', '', 
# 'Awutu Senya East Municipal', 'Kasoa', 'Awutu-Senya East', 'Created 2012', 
# 'Awutu Senya West', 'Awutu Breku', 'Awutu-Senya West', '', 
# 'Cape Coast Metropolitan', 'Cape Coast', 'Cape Coast North', 'Created 2012', 
# 'Cape Coast Metropolitan', 'Cape Coast','Cape Coast South', '', 
# 'Effutu Municipal', 'Winneba', 'Effutu', '',
# 'Ekumfi', 'Apam', 'Ekumfi', '', 
# 'Gomoa East', 'Potsin', 'Gomoa East', '', 
# 'Gomoa Central', 'Afransi', 'Gomoa Central', 'Created 2012',
# 'Gomoa West', 'Esakyir', 'Gomoa West', '', 
# 'Komenda-Edina-Eguafo-Abirem Municipal', 'Elmina', 'Komenda-Edina-Eguafo-Abirem', '', 
# 'Mfantsiman Municipal', 'Saltpond', 'Mfantseman', '', 
# 'Twifo Atti Morkwa', 'Twifo Praso', 'Twifo-Atii Morkwaa', '', 
# 'Twifo/Heman/Lower Denkyira', 'Hemang', 'Hemang Lower Denkyira', 'Created 2004', 
# 'Upper Denkyira East Municipal', 'Dunkwa-on-Offin', 'Upper Denkyira East', 'Created 2004',
# 'Upper Denkyira West', 'Diaso', 'Upper Denkyira West', 'Created 2004']


# con_list_8 = ['Ablekuma Central Municipal Assembly', 'Lartebiokorshie', 'Ablekuma Central', '', 
# 'Ablekuma North Municipal Assembly', 'Darkuman', 'Ablekuma North', '', 
# 'Ablekuma West Municipal Assembly', 'Dansoman', 'Ablekuma West', 'Created 2012',
# 'Accra Metropolitan Assembly', 'Accra','Okaikwei South', '', 
# 'Accra Metropolitan Assembly', 'Accra', 'Okaikwei Central', 'Created 2012',
# 'Accra Metropolitan Assembly', 'Accra', 'Odododiodio', '', 
# 'Accra Metropolitan Assembly', 'Accra', 'Ablekuma South', '',
# 'Ada East', 'Ada Foah', 'Ada', '', 
# 'Ada West', 'Sege', 'Sege', 'Created 2004',
# 'Adenta Municipal', 'Adenta', 'Adenta', 'Created 2004', 
# 'Ashaiman Municipal', 'Ashaiman', 'Ashaiman', '', 
# 'Ayawaso Central Municipal', 'Kokomlemle', 'Ayawaso Central', '', 
# 'Ayawaso East Municipal Assembly', 'Nima', 'Ayawaso East', '', 
# 'Ayawaso North Municipal Assembly', 'Accra New Town', 'Ayawaso North', 'Created 2012', 
# 'Ayawaso West Municipal Assembly', 'Dzorwulu', 'Ayawaso West', '', 
# 'Ga Central Municipal', 'Sowutuom', 'Anyaa-Sowutuom', 'Created 2012', 
# 'Ga East Municipal', 'Abokobi', 'Dome-Kwabenya', 'Created 2004', 
# 'Ga North Municipal', 'Amomole', 'Trobu', 'Created from Trobu-Amasaman 2012', 
# 'Ga South Municipal', 'Ngleshie Amanfro', 'Bortianor-Ngleshie-Amanfrom', 'Created 2012', 
# 'Ga South Municipal', 'Ngleshie Amanfro','Domeabra-Obom', 'Created 2004',
# 'Ga West Municipal', 'Amasaman', 'Amasaman', 'Trobu-Amasaman 2004Split 2012', 
# 'Korle-Klottey Municipal Assembly', 'Osu', 'Korle Klottey', '', 
# 'Kpone Katamanso Municipal Assembly', 'Kpone', 'Kpone-Katamanso', '', 
# 'Krowor Municipal Assembly', 'Nungua', 'Krowor', '', 
# 'La Dade Kotopon Municipal Assembly', 'La', 'Dade Kotopon', '', 
# 'La Nkwantanang Madina Municipal', 'Madina', 'Abokobi-Madina', 'Created 2004', 
# 'Ledzokuku Municipal', 'Teshie', 'Ledzokuku', '', 
# 'Ningo Prampram', 'Prampram', 'Ningo-Prampram', '', 
# 'Okaikwei North Municipal', 'Tesano', 'Okaikwei North', '', 
# 'Shai Osudoku', 'Dodowa', 'Shai-Osudoku', '', 
# 'Tema Metropolitan Assembly', 'Tema', 'Tema Central', 'Created 2012', 
# 'Tema Metropolitan Assembly', 'Tema','Tema East', '', 
# 'Tema West Municipal', 'Tema Community 18', 'Tema West', '', 
# 'Weija Gbawe Municipal Assembly', 'Weija', 'Weija', 'Created 2004']

# d15 = [con_list_16[i:i+4] for i in range(0,len(con_list_16),4)]

# d15 = [con_list_3[i:i+4] for i in range(0,len(con_list_3),4)]

# d15 = [con_list_6[i:i+4] for i in range(0,len(con_list_6),4)]

# d15 = [con_list_8[i:i+4] for i in range(0,len(con_list_8),4)]

d15 = [d14[i:i+4] for i in range(0,len(d14),4)]

data_5 = pandas.DataFrame(d15,columns=d13)

# data_5.to_csv('data_5.csv', index=False, header= False, mode= 'a')



    

# data_5.to_csv(r'C:\Users\justi\Desktop\Power BI\Project\Ghana Election 2024\data_5.csv',index=False)


#2020Presidential Polls Results



presi_list = show_3.find('table',class_ = "wikitable sortable")

presi_list_h = presi_list.find_all('th')

presi_list_r = presi_list.find_all('td')

d16 = [th.text.strip() for th in presi_list_h[:6]]

d16 = ['Empty'] + d16[:-1]



d17 = [th.text.strip() for th in presi_list_r]

d18 = [d17[i:i+6] for i in range(0,len(d17),6) ]


data_2_2020 = pandas.DataFrame(d18,columns=d16)

# data_2_2020.to_csv(r'C:\Users\justi\Desktop\Power BI\Project\Ghana Election 2024\data_2_2020.csv',index=False)


 




# 2020 Presidential Polls by Region Results

regi_list = show_3.find_all('table')[12]

regi_list_h = regi_list.find_all('th')

regi_list_r = regi_list.find_all('td')

d19 = [th.text.strip() for th in regi_list_h[:13]]



d20 = [th.text.strip() for th in regi_list_r]

d21 = [d20[i:i+13] for i in range(0,len(d20),13)]


data_3_2020 = pandas.DataFrame(d21,columns=d19)

# data_3_2020.to_csv(r'C:\Users\justi\Desktop\Power BI\Project\Ghana Election 2024\data_3_2020.csv',index=False)


#Political Parties

poli_list = show_4.find_all('table')[2]

poli_list_h = poli_list.find_all('th')

poli_list_r = poli_list.find_all('td')

d22 = [th.text.strip() for th in poli_list_h[:10]]

d22 = ['Empty'] + d22[:-1]

d22 =  d22[:8] + ['Last election'] + ['Comments'] 

d23 = [th.text.strip() for th in poli_list_r]

# con_list_9 = ['', 'New Patriotic Party', 'NPP', '1992', 'Nana Akufo-Addo', 'Centre-right', 'Liberal conservatismConservatismLiberalism', '137 / 275',' ', 
# '', '' , 'National Democratic Congress', 'NDC', '1992', 'Samuel Ofosu-Ampofo', 'Centre-left', 'Social democracy', '137 / 275','','']

# d24 = [con_list_9[i:i+10] for i in range(0,len(con_list_9),10)]

d24 = [d23[i:i+10] for i in range(0,len(d23),10)]


data_6 = pandas.DataFrame(d24,columns=d22)

# data_6.to_csv('data_6.csv', index=False, mode= 'a')

data_6.to_csv('data_6.csv', index=False, header= False, mode= 'a')

print(data_6)