# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
# from species import SpeciesSighting


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Wildlife')

wildlife = SHEET.worksheet('Wildlife')

class SpeciesSighting:
    def __init__(self, species_id, common_name, scientific_name, typical_habitats, 
                 estimated_population, date_and_time_of_sighting, location_of_sighting, notes):
        self.species_id = species_id
        self.common_name = common_name
        self.scientific_name = scientific_name.strip()  # To remove any extra spaces
        self.typical_habitats = typical_habitats
        self.estimated_population = estimated_population
        self.date_and_time_of_sighting = datetime.strptime(date_and_time_of_sighting, '%d/%m/%Y %H:%M')
        self.location_of_sighting = location_of_sighting
        self.notes = notes

    def __str__(self):
        return f"{self.common_name} ({self.scientific_name}) seen at {self.location_of_sighting} on {self.date_and_time_of_sighting.strftime('%d/%m/%Y %H:%M')}."

    def to_list(self):
        return [self.species_id, self.common_name, self.scientific_name, self.typical_habitats, 
                self.estimated_population, self.date_and_time_of_sighting.strftime('%d/%m/%Y %H:%M'), 
                self.location_of_sighting, self.notes]

#test adding 2 new items
sighting1 = SpeciesSighting(14, "test ed Fox", "Vulpes vulpes", "Location of sighting", "150,000", "23/08/2023 15:30", "Cork City Park", "None")
sighting2 = SpeciesSighting(15, "test Irish Hare", "Lepus timidus hibernicus", "Woodlands, urban", "40,000", "24/08/2023 07:20", "Galway Countryside", "None")

print(sighting1)
print(sighting2)


def all_data():
    #get all values from spreasheet
    data = wildlife.get_all_values()
    print(data)

def update_sheet(sighting, worksheet='Wildlife'):
    #convert sighting into list
    data = sighting.to_list()
    # update the spreadsheet
    update = SHEET.worksheet(worksheet)
    update.append_row(data)

    print(f"{worksheet} has been updated! ")

def delete(species_id, worksheet ="Wildlife"):
    sheet = SHEET.worksheet(worksheet)
    id = sheet.col_values(1)
    
    #find row index for species_id
    row = id.index(str(species_id)) + 1
    sheet.delete_row(row)
    print(f"{row} deleted")


def menu():
    print("Menu")
    print("1 - Add wildlife")
    print("2 - Delete wildlife")
    print("3 - View wildlife")
    print("4 - Update wildlife")
    print("5 - Size of list")
    print("6 -Search by common name")
    print("7 -Search by scientific name")
    print("8 - Search by typical habitats")
    print("9 - chart of estimated population")
    print("10 - View full wildlife list")
    print("q - Quit")

#options of Menu
while True:
    menu()
    option = input("Pick an option: \n")

    if option == "1":
        option1()
    elif option == "2":
        option2()
    elif option == "3":
        option3()
    elif option == "4":
        option4()
    elif option == "5":
        option5()
    elif option == "6":
        option6()
    elif option == "7":
        option7()
    elif option == "8":
        option8()
    elif option == "9":
        option9()
    elif option == "q":
        print("Program Dead")
        break
    else:
        print("Invalid!!! Please try again!!!")

# delete(15)

# all_data()
# update_sheet(sighting1)
# update_sheet(sighting2)

# def main():

menu()