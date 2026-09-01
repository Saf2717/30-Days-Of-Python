#Declare an empty list
empty_list = list()

#Declare a list with more than 5 items
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'grapes']

#Find the length of your list
print(len(fruits)) # 6

#Get the first item, the middle item and the last item of the list
first_item = fruits[0]

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['John', 25, 5.9, True, "24 zoo lane"]

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'APPLE', 'IBM', 'Oracle', 'Amazon', 'Meta']

print(it_companies) 

#Print the number of companies in the list
no_companies = len(it_companies)
print(no_companies)  

#Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print(first_company)
print(middle_company)
print(last_company)

#Join the it_companies with a string '#;  '
it_companies_str = '# '.join(it_companies)
print(it_companies_str)

#Check if a certain company exists in the it_companies list.
check ='Apple' in it_companies
print(check)  

#Sort the list using sort() method
sorted = it_companies.sort()

#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#Slice out the first 3 companies from the list
copy = it_companies.copy()
del copy[:3]
print(copy)

#Slice out the last 3 companies from the list
slice_last_3 = it_companies[:-3]
print(slice_last_3)

#Slice out the middle IT company or companies from the list
coopy2 = it_companies.copy()
del coopy2[len(coopy2) // 2]
print(coopy2)


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)
front_end.insert(5, 'Python') 
front_end.insert(6, 'SQL')
fullstack = front_end
print(fullstack)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
ages.append(26)
ages.append(19)
ages.sort()
if len(ages) % 2 != 0:
    median = len(ages) // 2
else:
    median = (ages[len(ages) // 2] + ages[len(ages) // 2 - 1]) / 2
print(median)

average = sum(ages) / len(ages)
print(average)

range = max(ages) - min(ages)
print(range)

print(abs(min(ages) - average))
print(abs(max(ages) - average))




countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

if len(countries) % 2 != 0:
    middle_index = len(countries) // 2
    print('Middle country:', countries[middle_index])
else:
    middle_index1 = (len(countries) // 2) - 1
    middle_index2 = len(countries) // 2
    print('Middle countries:', countries[middle_index1], 'and', countries[middle_index2])



if len(countries) % 2 != 0:
    second_half = countries[(len(countries) // 2 + 1):-1]
    first_half = countries[0:(len(countries) // 2)]
else:
    second_half = countries[len(countries) // 2:]
    first_half = countries[0:len(countries) // 2]
print('First half:', first_half, 'length:', len(first_half))
print('Second half:', second_half, 'length:', len(second_half))


idk = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china,russia,usa, *scandic = idk
print(scandic)  # ['Finland', 'Sweden', 'Norway', 'Denmark']