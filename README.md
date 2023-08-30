![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)





Intro:
This program helps you to manage and record species sightings using a Google Sheet. With the power of Python combined with Google Sheets API, you can seamlessly keep track of wildlife sightings, search for specific entries, update or delete data, and more.

How to Use:
Setup Google Sheets API:
Before using the program, ensure that you have set up the Google Sheets API and have a 'creds.json' file. This JSON will authenticate the Python script to access the Google Sheet.
Here is the link for the goolge doc: https://docs.google.com/spreadsheets/d/16j14he0t61-asIWOEtErY5vUVeQQhXd-JbK1XRM40Lo/edit?usp=sharing

Run the program:
Execute the script, and you'll be presented with a menu offering various options from adding a wildlife entry to searching for entries based on specific criteria.


<img width="254" alt="image" src="https://github.com/RichRich087/Wildlife/assets/128620545/8026a3df-0e6b-4bcb-9894-34c7bd5af412">


Menu Options:
Choose from the following options:

Add wildlife
Delete wildlife
View wildlife
Update wildlife
Size of list
Search by common name
Search by scientific name
Search by typical habitats
View full wildlife list
Quit:
Enter 'q' anytime to exit the program.


Features
1. Google Sheets Integration:
Secure Connection: The program uses OAuth 2.0 to authenticate and authorize access to the Google Sheet named 'Wildlife', ensuring data safety and integrity.


<img width="899" alt="image" src="https://github.com/RichRich087/Wildlife/assets/128620545/2abf3668-d26c-4fb7-9790-cde72f1dda79">


Scopes and Permissions: It requires three distinct scopes: accessing spreadsheets, accessing drive files, and full drive access. This granularity ensures that the application can perform its operations without unnecessary permissions.

Real-time Sync: All changes made through the application reflect instantly on the Google Sheet, ensuring real-time synchronization.

Spreadsheet Operations: Multiple functionalities such as appending new rows, deleting rows, or retrieving data are made seamless with Google Sheet integration.

2. CRUD Operations:
Create (Add New Entries): Log new wildlife sightings. Each entry contains details such as species ID, common name, scientific name, habitats, estimated population, sighting date and time, location, and any additional notes.


<img width="233" alt="image" src="https://github.com/RichRich087/Wildlife/assets/128620545/c90a0d3f-cf05-415f-a700-3c79d50f36fc">


Read (View Entries): Users can view a particular wildlife sighting, view a list of all sightings, or even view the entire detailed list, offering flexibility in data visualization.


<img width="307" alt="image" src="https://github.com/RichRich087/Wildlife/assets/128620545/e8dbcf85-f060-46e5-8b0c-e74cfd7977b2">


Update (Modify Entries): An existing entry's details can be seamlessly updated. This includes all aspects of the entry, from the species ID to any additional notes.


<img width="284" alt="image" src="https://github.com/RichRich087/Wildlife/assets/128620545/323be76a-9fdf-4acf-aa74-094308389f6f">


Delete: Efficiently remove any entry from the list without affecting or losing other data.


<img width="319" alt="image" src="https://github.com/RichRich087/Wildlife/assets/128620545/0592f3e7-cd92-4fa1-9031-29bc03e82b42">


3. Search Features:
Versatile Searching: The application doesn’t limit users to searching entries by one criterion. It offers multiple search avenues:
Common Name: Directly search for a species using its commonly known name.


<img width="221" alt="image" src="https://github.com/RichRich087/Wildlife/assets/128620545/bcf13dac-7447-4251-aed1-02bf95542661">


Scientific Name: For more precision, search using the scientific nomenclature.


<img width="230" alt="image" src="https://github.com/RichRich087/Wildlife/assets/128620545/9a5a739b-90af-40de-b8f1-0b914461a2b5">


Typical Habitats: Find all species sighted in a particular habitat or environment.
Partial Match: The habitat search allows for partial matches, increasing the range of search results.


<img width="209" alt="image" src="https://github.com/RichRich087/Wildlife/assets/128620545/1adb49c7-b9dc-4c8f-9cbd-96118030cc3f">



5. Data Model (Class):
Encapsulation: The SpeciesSighting class serves as a blueprint for each wildlife sighting entry. It encapsulates vital attributes, ensuring data consistency and structure.

Flexibility: This class offers methods to:

Convert its attributes to a list for smooth integration with Google Sheets operations.
Update its attributes on the fly, ensuring that modifications to entries are straightforward.
String Representation: For better logging and printing, the class provides a string representation that summarizes the sighting.

5. Error Handling:
Connection Errors: If the program encounters any issues connecting to Google Sheets, the error is captured, a message is displayed, and the program gracefully exits.

Data Integrity: When expecting date-time entries, the program anticipates a specific format. It can handle deviations or errors in this format.

6. User-Friendly Menu System:
Interactive Menu: Upon launch, the application displays a menu, guiding users through various functionalities available.

Clear Instructions: Each menu option provides clear instructions, ensuring that users can easily understand and use the system.

Navigation: Users can navigate back to the main menu after completing an action, allowing for continuous operation without restarting the application.

Exit Mechanism: Users can exit the application gracefully using the designated 'quit' option.

Data Model
Attributes:
Species ID: A unique identifier for each species.
Common Name: The name by which the species is commonly known.
Scientific Name: The official scientific name of the species.
Habitats: The typical environments where the species can be found.
Estimated Population: A rough estimate of the species population.
Date and Time of Sighting: When the species was sighted.
Location of Sighting: The geographical location of the sighting.
Notes: Any additional information or notes about the sighting.





Deployment Using Heroku:
Make sure you have a Heroku account and Heroku CLI installed.
Commit your changes to your Git repository.
Create a new Heroku app: heroku create your-app-name.
Push your repository to Heroku: git push heroku master.
Ensure your environment variables (like those from creds.json) are set in the Heroku dashboard under your app's settings.
Deploy.

Testing:
Tested on a PEP8 linter there is some errors however they are more syntax related the program works as intended:

<img width="210" alt="image" src="https://github.com/RichRich087/Wildlife/assets/128620545/3748e3ef-8b1c-47fd-b825-f9bb746beaa5">

Tested in my local terminal and the Code Institute Heroku Terminal. Works as intended on both.

Bugs:
e.g. of source https://medium.com/@SrvZ/how-to-create-stunning-graphs-in-the-terminal-with-python-2adf9d012131
I wanted to add a graph to display population for each species. There is libraries that allow this such as Terminalplot or gnuplot. I looked at mulptiple different libraries and kept running into errors in regards to what codeanywhere allows.
We tried many things but kept running into issues with access. e.g we found out that codeanywhere utilizes Ubund based containers. 
So
apt update
worked.
apt install -y gnuplot
did not work due to access.
Codeanywhere utilizes as a default bash which we tried changing to sudo:
e.g.
sudo su - (to change to superuser)
sudo apt update
sudo apt install gnuplot
but we couldnt swap to sudo due to access issue. In future it might be worth while using a different IDE.
Ultimatly it would have been easiest using a jupyter notebook with a library such as matplotlib. However this rabbit hole was very much going outside of the scope of this assignment.

The most time consuming issue was a **very** simple one. In our while loop that runs all the options we had many if statements rather than using elif statements. A simple oversight. We incorrectly believed there was a issue with the enter function that we created and therefore spent a lot of time in the wrong section of the code trouble shooting.

