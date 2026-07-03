from operator import attrgetter
class Country:
    def __init__(self, countryname, area, population):
        self.countryname = countryname
        self.area = area
        self.population = population
    def __repr__(self):
        return repr((self.countryname, self.area, self.population))

countries = [Country('USA', 3000, 50)]
countries.append (Country('India', 1000, 140))
countries.append(Country('Pakistan', 100, 20))

countries.sort(key=attrgetter('population'), reverse = True)
print (countries)
