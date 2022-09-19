# programing_diccionary= {
# "Bug": "An error in a program that prevents the program from running as expected",
# "Function": "A piece of code that you can easily call over and over again",
# }

# #Retrieving items from dictionary.
# print(programing_diccionary["Function"])

# #Adding new items to dictionary
# programing_diccionary["Loop"] = "The action of doing something over and over again"
# print(programing_diccionary)

# #Create an empthy dictionary
# empty_dictionary = {}

# #Wipe an existing dictionary
# programing_diccionary = {}
# print(programing_diccionary)

# #Edit an item in a dictionary
# programing_diccionary["Bug"] = "A moth in your computer"
# print(programing_diccionary)

# #Loop through a dictionary
# for thing in programing_diccionary:
# 	print(thing)
# 	print(programing_diccionary[thing])

# #Anidado de listas

# travel_log = { 
# 	"France": ["Paris","lille","Dijon"],
# 	"Germany":["Berlin","Hamburg","Stuttgart"]
# }

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits,city):
	new_country = {}
	new_country["Country"] = country
	new_country["Visits"] = visits
	new_country["Cities"] = city
	travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
