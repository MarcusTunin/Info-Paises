#pip install countryinfo
from countryinfo import CountryInfo

country = CountryInfo(input('Digite o nome do país: '))

print(f'País: {country.name()}')
print(f'Capital: {country.capital()}')
print(f'Idiomas: {country.languages()}')
print(f'População: {country.population()}')
print(f'Faz fronteira com: {country.borders()}')