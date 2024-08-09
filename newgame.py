import csv
csv_file_path = r"D:\countrylist.csv"
with open(csv_file_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    csv_list = list(reader)
   # print(csv_list) 

new_list = csv_list[1:] # cuts the headers of the csv file
#print(new_list)


new_list2 = []
country_list = []
capital_list = []
for item in new_list:
    if item[2] == 'countryCapital':
        new_list2.append(item[0])
        new_list2.append(item[1])
        country_list.append(item[0])
        capital_list.append(item[1])

country_list_lower = [countries.lower() for countries in country_list]
#print(country_list_lower) #resulting the list of the countries
capital_list_lower = [capitals.lower() for capitals in capital_list]
#print(capital_list_lower) #resulting the list of the capitals
#print(new_list2)     #resulting one large list example: ['Abkhazia', 'Sukhumi', 'Afghanistan', 'Kabul', ...]
combined = list(zip(country_list, capital_list))
#print(combined) #resulting a large list with example: [('Abkhazia', 'Sukhumi'),......]



#print(country_list[1], capital_list[1]) #prints out country associeted with their capital
import random

random_country = random.choice(country_list)
#print(random_country) #prints out a random country
random_capital = random.choice(capital_list)
#print(random_capital)   #prints out of random capital

#check and match indices of the question with the one of the answer!!!!!!!

question_capital = "What is the capital of " + random_country + " ?"
question_country = "What is the country that has the capital of " + random_capital + " ?"
print(question_capital)
#print(question_country)



answer = input("Please type uour answer: ").strip().lower()

found_match = False

for capital in capital_list:
    #print(capital_list[i])#== country_list[i]
    #print(country_list[i])
    if answer == capital.strip().lower():
     print("Correct")   #(capital_list[i], ": ", country_list[i])
     found_match = True
     break
if not found_match:
   print("Incorrect")
    #if answer == capital_list[i]:
       #print("Correct")
    #else:
       #print("Incorrect")
       


       



 
 
            

    
     
    


    
        



