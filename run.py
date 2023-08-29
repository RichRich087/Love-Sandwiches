import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

try:
    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open('Wildlife')
    wildlife = SHEET.worksheet('Wildlife')
except Exception as e:
    print(f"An error occurred while connecting to Google Sheets: {e}")
    exit(1)


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

    def update(self):
        self.species_id = input(f"Species I.D. (current: {self.species_id}): ") or self.species_id
        self.common_name = input(f"Common Name (current: {self.common_name}): ") or self.common_name
        self.scientific_name = input(f"Scientific Name (current: {self.scientific_name}): ") or self.scientific_name
        self.typical_habitats = input(f"Typical Habitats (current: {self.typical_habitats}): ") or self.typical_habitats
        self.estimated_population = input(f"Estimated Population (current: {self.estimated_population}): ") or self.estimated_population
        date_and_time = input(f"Date and Time of Sighting (current: {self.date_and_time_of_sighting.strftime('%d/%m/%Y %H:%M')}): ") or self.date_and_time_of_sighting.strftime('%d/%m/%Y %H:%M')
        self.date_and_time_of_sighting = datetime.strptime(date_and_time, '%d/%m/%Y %H:%M')
        self.location_of_sighting = input(f"Location of Sighting (current: {self.location_of_sighting}): ") or self.location_of_sighting
        self.notes = input(f"Notes (current: {self.notes}): ") or self.notes


quick option add items to delete items from spreadsheet. Do not delete existing entries!!!
sighting1 = SpeciesSighting(14, "test ed Fox", "Vulpes vulpes", "Location of sighting", "150,000", "23/08/2023 15:30", "Cork City Park", "None")
sighting2 = SpeciesSighting(15, "test Irish Hare", "Lepus timidus hibernicus", "Woodlands, urban", "40,000", "24/08/2023 07:20", "Galway Countryside", "None")

print(sighting1)
print(sighting2)


def all_data():
    #get all values from spreasheet
    data = wildlife.get_all_values()
    print(data)

def all_data1():
    #get all values from spreasheet
    return wildlife.get_all_values()

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

def search_common_name():
    search = input("Enter the common name to search for: ").strip().lower()
    data = all_data1()
    matches = [row for row in data if row[1].lower() == search]
    if not matches:
        print("No matches found for that common name.")
        return
    for match in matches:
        print(', '.join(match))

def search_scientific_name():
    search = input("Enter the scientific name to search for: ").strip().lower()
    data = all_data1()
    matches = [row for row in data if row[2].lower() == search]
    if not matches:
        print("No matches found for that scientific name.")
        return
    for match in matches:
        print(', '.join(match))


def search_typical_habitat():
    search = input("Enter the typical habitat to search for: ").strip().lower()
    data = all_data1()
    matches = [row for row in data if search in row[3].lower()] #partial match
    #exact match: matches = [row for row in data if search row[3].lower() == search]
    if not matches:
        print("No matches found for that typical habitat.")
        return
    for match in matches:
        print(', '.join(match))

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
    print("9 - View full wildlife list")
    print("q - Quit")

def wildlife_list():
    #get data from all_data function
    data = all_data1()
    counter = 1  # start at 1 due to 1st row being header
    for row in data[1:]: 
        print(f"{counter - 1} - {row[1]}") #counter + 1 gets the correct index position
        counter += 1 #add 1 to counter


# # #Add wildlife
def option1():
    print ("Add new wildlife entry:")
    species_id = input ("Species I.D. (I.D. used internally): \n")
    common_name = input ("Common Name: \n")
    scientific_name = input ("Scientific Name: \n")
    typical_habitats = input ("Typical Habitats: \n")
    estimated_population = input ("Estimated Population: \n")
    date_and_time = input ("Date and Time of Sighting (required format '%d/%m/%Y %H:%M' e.g. 26/08/2023 21:10): \n")
    location = input ("Location of Sighting: \n")
    notes = input ("Notes: \n")

    sighting = SpeciesSighting (species_id, common_name, scientific_name, typical_habitats, estimated_population, date_and_time, location, notes)
    update_sheet(sighting)
    print (f" added: {sighting}")
    enter()

# # #Delete wildlife
def option2():
    wildlife_list()
    selection2 = int(input("Enter the number for the entry you would like to delete: \n"))
    delete(selection2)
    enter()

# # #View wildlife
def option3():
    wildlife_list()
    selection3 = int(input("Enter the number for the entry you would like to view: \n"))
    print(wildlife.row_values(selection3 + 2))
    enter()

# # #Update wildlife
def option4():
    print("Update Wildlife Entry")
    wildlife_list()
    
    # Ask the user to choose the entry they want to update.
    entry_num = int(input("Enter the number of the entry you want to update: "))
    entry_data = all_data1()[entry_num + 1]  # +1 to skip the header row

    # Create a temporary object from the current data
    tmp_sighting = SpeciesSighting(*entry_data)  # Using * to unpack the list elements 

    # Update the object using its method
    tmp_sighting.update()

    # Update the chosen entry with the new details in the spreadsheet.
    worksheet = SHEET.worksheet("Wildlife")
    row_to_update = entry_num + 2  # +2 to account for 0 based indexing and header row.
    range_label = f"A{row_to_update}:H{row_to_update}" 
    worksheet.update(range_label, [tmp_sighting.to_list()])  # Wrap the list in another list 
    print("Entry has been updated!")
    enter()
# # #Size of list

def option5():
    total = len(all_data1()) - 1 # -1 for header
    print(f"The list has a total of {total} entries")
    enter()

# # #Search by common name
def option6():
    search_common_name()
    enter()

# # #Search by scientific name
def option7():
    search_scientific_name()
    enter()

# # #Search by typical habitats
def option8():
    search_typical_habitat()
    enter()

# # #View full wildlife list
def option9():
    all_data()
    enter()

def enter():
    print("----------------------------------")
    print(input("Press Enter to continue..."))


#options of Menu
while True:
    menu()
    option = input("Pick an option: \n").strip()

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
        enter()
    elif option == "9":
        option9()

    elif option == "q":
        print("Program Dead")
        break
    else:
        print("Invalid!!! Please try again!!!")
        break


#this is a test