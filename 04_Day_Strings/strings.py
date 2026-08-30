string = ["thirty", "days", "of", "python"]
print(" ".join(string))  # thirty days of python

company = "Coding For All"
print(company)
print (len(company))
print(company.upper())

#Cut(slice) out the first word of Coding For All string.

print(company[0:6])

if company.find("Coding") != -1:
    print("The word 'Coding' is present in the string.")

print (company.find("ghr")) 

print(company.replace("Coding", "Python"))

print('Coding For All'.split(" "))
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))
print(company.index("C"))

print(company[10])

print(company.index("F"))
print('Coding For All People'.rfind('l'))
print('You cannot end a sentence with because because because is a conjunction'.find('because'))

print(company.startswith("Coding"))

print('   Coding For All      ' .strip(" "))

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

radius = 10
area = 3.14 * radius ** 2
print('The area of the circle with radius {} is {} meters square.'.format(radius, int(area)))

