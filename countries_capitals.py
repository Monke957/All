import os 
import random
import time
from tkinter import *



os.system('cls' if os.name == 'nt' else 'clear')

capitals = {
    'usa': 'Washington D.C',
    'albania': 'Tirana',
    'andorra': 'Andorra la Vella',
    'angola': 'Luanda',
    'antigua and barbuda': 'Saint John\'s',
    'argentina': 'Buenos Aires',
    'armenia': 'Yerevan',
    'australia': 'Canberra',
    'austria': 'Vienna',
    'azerbaijan': 'Baku',
    'bahamas': 'Nassau',
    'bahrain': 'Manama',
    'bangladesh': 'Dhaka',
    'barbados': 'Bridgetown',
    'belarus': 'Minsk',
    'belgium': 'Brussels',
    'belize': 'Belmopan',
    'benin': 'Porto-Novo',
    'bhutan': 'Thimphu',
    'bolivia': 'Sucre',
    'bosnia and herzegovina': 'Sarajevo',
    'botswana': 'Gaborone',
    'brazil': 'Brasília',
    'brunei': 'Bandar Seri Begawan',
    'bulgaria': 'Sofia',
    'burkina faso': 'Ouagadougou',
    'burundi': 'Gitega',
    'cabo verde': 'Praia',
    'cambodia': 'Phnom Penh',
    'cameroon': 'Yaoundé',
    'canada': 'Ottawa',
    'central african republic': 'Bangui',
    'chad': 'N\'Djamena',
    'chile': 'Santiago',
    'china': 'Beijing',
    'colombia': 'Bogotá',
    'comoros': 'Moroni',
    'congo (congo-brazzaville)': 'Brazzaville',
    'congo (congo-kinshasa)': 'Kinshasa',
    'costa rica': 'San José',
    'croatia': 'Zagreb',
    'cuba': 'Havana',
    'cyprus': 'Nicosia',
    'czech republic': 'Prague',
    'denmark': 'Copenhagen',
    'djibouti': 'Djibouti',
    'dominica': 'Roseau',
    'dominican republic': 'Santo Domingo',
    'east timor': 'Dili',
    'ecuador': 'Quito',
    'egypt': 'Cairo',
    'el salvador': 'San Salvador',
    'equatorial guinea': 'Malabo',
    'eritrea': 'Asmara',
    'estonia': 'Tallinn',
    'eswatini': 'Mbabane',
    'ethiopia': 'Addis Ababa',
    'fiji': 'Suva',
    'finland': 'Helsinki',
    'france': 'Paris',
    'gabon': 'Libreville',
    'gambia': 'Banjul',
    'georgia': 'Tbilisi',
    'germany': 'Berlin',
    'ghana': 'Accra',
    'greece': 'Athens',
    'grenada': 'St. George\'s',
    'guatemala': 'Guatemala City',
    'guinea': 'Conakry',
    'guinea-bissau': 'Bissau',
    'guyana': 'Georgetown',
    'haiti': 'Port-au-Prince',
    'honduras': 'Tegucigalpa',
    'hungary': 'Budapest',
    'iceland': 'Reykjavik',
    'india': 'New Delhi',
    'indonesia': 'Jakarta',
    'iran': 'Tehran',
    'iraq': 'Baghdad',
    'ireland': 'Dublin',
    'israel': 'Jerusalem',
    'italy': 'Rome',
    'ivory coast': 'Yamoussoukro',
    'jamaica': 'Kingston',
    'japan': 'Tokyo',
    'jordan': 'Amman',
    'kazakhstan': 'Astana',
    'kenya': 'Nairobi',
    'kiribati': 'Tarawa',
    'korea, north': 'Pyongyang',
    'korea, south': 'Seoul',
    'kuwait': 'Kuwait City',
    'kyrgyzstan': 'Bishkek',
    'laos': 'Vientiane',
    'latvia': 'Riga',
    'lebanon': 'Beirut',
    'lesotho': 'Maseru',
    'liberia': 'Monrovia',
    'libya': 'Tripoli',
    'liechtenstein': 'Vaduz',
    'lithuania': 'Vilnius',
    'luxembourg': 'Luxembourg City',
    'madagascar': 'Antananarivo',
    'malawi': 'Lilongwe',
    'malaysia': 'Kuala Lumpur',
    'maldives': 'Malé',
    'mali': 'Bamako',
    'malta': 'Valletta',
    'marshall islands': 'Majuro',
    'mauritania': 'Nouakchott',
    'mauritius': 'Port Louis',
    'mexico': 'Mexico City',
    'micronesia': 'Palikir',
    'moldova': 'Chisinau',
    'monaco': 'Monaco',
    'mongolia': 'Ulaanbaatar',
    'montenegro': 'Podgorica',
    'morocco': 'Rabat',
    'mozambique': 'Maputo',
    'myanmar': 'Naypyidaw',
    'namibia': 'Windhoek',
    'nauru': 'Yaren',
    'nepal': 'Kathmandu',
    'netherlands': 'Amsterdam',
    'new zealand': 'Wellington',
    'nicaragua': 'Managua',
    'niger': 'Niamey',
    'nigeria': 'Abuja',
    'north macedonia': 'Skopje',
    'norway': 'Oslo',
    'oman': 'Muscat',
    'pakistan': 'Islamabad',
    'palau': 'Ngerulmud',
    'panama': 'Panama City',
    'papua new guinea': 'Port Moresby',
    'paraguay': 'Asunción',
    'peru': 'Lima',
    'philippines': 'Manila',
    'poland': 'Warsaw',
    'portugal': 'Lisbon',
    'qatar': 'Doha',
    'romania': 'Bucharest',
    'russia': 'Moscow',
    'rwanda': 'Kigali',
    'saint kitts and nevis': 'Basseterre',
    'saint lucia': 'Castries',
    'saint vincent and the grenadines': 'Kingstown',
    'samoa': 'Apia',
    'san marino': 'San Marino',
    'sao tome and principe': 'São Tomé',
    'saudi arabia': 'Riyadh',
    'senegal': 'Dakar',
    'serbia': 'Belgrade',
    'seychelles': 'Victoria',
    'sierra leone': 'Freetown',
    'singapore': 'Singapore',
    'slovakia': 'Bratislava',
    'slovenia': 'Ljubljana',
    'solomon islands': 'Honiara',
    'somalia': 'Mogadishu',
    'south africa': 'Pretoria',
    'south sudan': 'Juba',
    'spain': 'Madrid',
    'sri lanka': 'Colombo',
    'sudan': 'Khartoum',
    'suriname': 'Paramaribo',
    'sweden': 'Stockholm',
    'switzerland': 'Bern',
    'syria': 'Damascus',
    'taiwan': 'Taipei',
    'tajikistan': 'Dushanbe',
    'tanzania': 'Dodoma',
    'thailand': 'Bangkok',
    'togo': 'Lomé',
    'tonga': 'Nukuʻalofa',
    'trinidad and tobago': 'Port of Spain',
    'tunisia': 'Tunis',
    'turkey': 'Ankara',
    'turkmenistan': 'Ashgabat',
    'tuvalu': 'Funafuti',
    'uganda': 'Kampala',
    'ukraine': 'Kyiv',
    'united arab emirates': 'Abu Dhabi',
    'united kingdom': 'London',
    'united states': 'Washington D.C',
    'uruguay': 'Montevideo',
    'uzbekistan': 'Tashkent',
    'vanuatu': 'Port Vila',
    'venezuela': 'Caracas',
    'vietnam': 'Hanoi',
    'yemen': 'Sana\'a',
    'zambia': 'Lusaka',
    'zimbabwe': 'Harare'   
}

while True:
    print('-------------------------------------')
    print('For help type "help"')
    question = input('What country would you like to know the capital of?: ')

    if not question.strip():  # If the input is empty or just spaces
        continue  # Skip this iteration and ask the question again

    if question == 'exit':
        print("ok bye :)")
        break
    
    if question == 'help'.lower():
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Type exit to quit')
        print('--------------------')
        print('Type "Full list" for a list of all countries')        
        print('--------------------')
        print('Type list followed by a continent for all countrys in that region')
        continue
    
    if question == 'Full list'.lower():
        countries = [
            'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 
            'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 
            'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 
            'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 
            'Chile', 'China', 'Colombia', 'Comoros', 'Congo (Congo-Brazzaville)', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 
            'Czech Republic', 'Democratic Republic of the Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 
            'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 
            'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 
            'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 
            'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 
            'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 
            'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 
            'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 
            'Montenegro', 'Morocco', 'Mozambique', 'Myanmar (formerly Burma)', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 
            'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 
            'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 
            'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 
            'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 
            'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 
            'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 
            'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 
            'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 
            'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
        ]
        
        for country in countries:
            print(country)
        continue    
    
    
    if question == 'list europe':
        countries2 = ['Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Bosnia and Herzegovina',
                    'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Georgia',
                    'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kazakhstan', 'Kosovo', 'Latvia', 'Liechtenstein',
                    'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway',
                    'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden',
                    'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom', 'Vatican City'
        ]
        for country2 in countries2:
            print(country2)
        continue
    
    
    if question == 'list africa':
        countries3 = [
            'Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic',
            'Chad', 'Comoros', 'Congo (Congo-Brazzaville)', 'Congo (Congo-Kinshasa)', 'Djibouti', 'Egypt', 'Equatorial Guinea',
            'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Ivory Coast', 'Kenya', 
            'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique',
            'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'São Tomé and Príncipe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia',
            'South Africa', 'South Sudan', 'Sudan', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe'
        ]
        for country3 in countries3:
            print(country3)
        continue

    if question == 'list aisa':
        aisan_countries = [   'Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 
                'Cyprus', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 
                'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 
                'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Russia', 'Saudi Arabia', 
                'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Timor-Leste', 
                'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen'
        ]
        for aisan in aisan_countries:
            print(aisan)
        continue

    if question == 'list northamerica':
        nordamerika_lander = [
            "Antigua och Barbuda", "Bahamas", "Barbados", "Belize", "Kanada", 
            "Costa Rica", "Dominica", "El Salvador", "Grenada", "Guatemala", 
            "Haiti", "Honduras", "Jamaica", "Mexiko", "Nicaragua", "Panama", 
            "St Kitts och Nevis", "St Lucia", "St Vincent och Grenadinerna", 
            "Trinidad och Tobago", "USA"
        ]
        for nordamerica in nordamerika_lander:
            print(nordamerica)
        continue

    if question == 'list southamerica':
        sydamerika_lander = [
            "Argentina", "Bolivia", "Brasilien", "Chile", "Colombia", "Ecuador", 
            "Guyana", "Paraguay", "Peru", "Surinam", "Uruguay", "Venezuela"
        ]
        for soutamerika in sydamerika_lander:
            print(soutamerika)
        continue

    if question == 'list oceanien':
        oceanien_lander = [
            "Australien", "Fiji", "Kiribati", "Marshallöarna", "Mikronesien", 
            "Nauru", "New zealand", "Palau", "Papua Nya Guinea", "Samoa", 
            "Solomonöarna", "Tonga", "Tuvalu", "Vanuatu"
        ]
        for oceanina in oceanien_lander:
            print(oceanina)
        continue


    # Now, check for the capital of the country
    capital = capitals.get(question.lower(), None)

    if capital:
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.2)
        
        rand = random.randint(2,5)


        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"The capital of {question.title()} is {capital}.")
    
    elif question != capital:
        print('Error no capital found, make sure that what you entered was a country.')
        print('RESETTING IN')
        
        print('5')
        time.sleep(1)
        print('4')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        os.system('cls' if os.name == 'nt' else 'clear')
