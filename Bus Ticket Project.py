#CSV imported
import csv

#Introducing the program
#Open menu, user chooses between User and Administrator
#Login Details for Admin, username - LewisG and password - password1

#I have used code from - https://stackoverflow.com/questions/62525164/python-how-to-store-a-username-password-from-input
#[Accessed on the 3/12/2025]

credentials = {}

with open('login_details.csv', mode = 'r') as file:
    loginCSV = csv.DictReader(file)
    for row in loginCSV:
        credentials[row['usernames']] = row['passwords']

def authenticate():
    username = input('Username: ')
    password = input('Password: ')
    return credentials.get(username) == password

print("Welcome to the bus ticket application")
print("For customer press C \nFor admin press A")

CorA = input("Are you a customer or admin?").strip().upper()

if CorA == "A":
    if authenticate():
        print("Welcome Admin!")
    else:
        print("Authentication failed")
        exit()
elif CorA == "C":
    print("Welcome User!")
else:
    print("Enter either C or A")

#The lists of the different category and top up choices that are within the program.

listOfCatClasses = []
listOfCategories = []
listOfCodes = []
listOfCategoryDesc = []
listOfTopUpTitles = []
listOfTopUpCodes = []
listOfTopUpDesc = []
listOfTopUpPrices = []
listOfTopUpEntTypes = []
listOfTopUpEntDates = []
listOfTopUpPassengers = []
listOfTopUpEntUnits = []
listOfTopUpEntValues = []

#Categroy class that contains the categories and category description.

class Category:
    def __init__(self, category, code, description):
        self.category = category
        self.code = code
        self.description = description
    def Getcategory(self):
        return self.category
    def Getcatcode(self):
        return self.code
    def Getdescription(self):
        return self.description

#Top up class contains all the choices involved with top up, e.g.: price, description, type.    

class TopUp:
    def __init__(self, topuptitles, topupcode, code, topdescription, topupprice, topupenttype, topupentdate, topuppassenger, topupentunit, topupentvalue):
        self.topuptitles = topuptitles
        self.topupcode = topupcode
        self.code = code
        self.topdescription = topdescription
        self.topupprice = topupprice
        self.topupenttype = topupenttype
        self.topupentdate = topupentdate
        self.topuppassenger = topuppassenger
        self.topupentunit = topupentunit
        self.topupentvalue = topupentvalue
    def Gettopup(self):
        return self.topuptitles
    def Gettopupcode(self):
        return self.topupcode
    def Getcategorycode(self):
        return self.code
    def Gettopdescription(self):
        return self.topdescription
    def Gettopupprice(self):
        return self.topupprice
    def Gettopupenttype(self):
        return self.topupenttype
    def Gettopupentdate(self):
        return self.topupentdate
    def Gettopuppassenger(self):
        return self.topuppassenger
    def Gettopupentunit(self):
        return self.topupentunit
    def Gettopupentvalue(self):
        return self.topupentvalue

with open('mobile_products.csv', mode = 'r') as file:
    csvFile = csv.DictReader(file)

#All the rows needed from the csv file for the program to produce the correct choices.
    
    for row in csvFile:
        category = row['category_title']
        categorydesc = row['category_description']
        code = row['category_id']
        topupcode = int(row['topup_id'])
        topuptypes = row['topup_title']
        topupdesc = row['topup_description']
        topupprice = row['topup_price_in_pence']
        topupenttype = row['topup_entitlement_type']
        topupentdate = row ['topup_entitlement_end_date']
        topuppassenger = row ['topup_passenger_class_name']
        topupentunit = row ['topup_entitlement_unit']
        topupentvalue = row ['topup_entitlement_value']
        
        if category not in listOfCategories:
            listOfCategories.append(category)
            listOfCategoryDesc.append(categorydesc)
            listOfCodes.append(code)
            cat1 = Category(category, code, categorydesc)
            listOfCatClasses.append(cat1)
            listOfTopUpCodes.append(topupcode)
            listOfTopUpDesc.append(topupdesc)
            listOfTopUpPrices.append(topupprice)
            listOfTopUpEntTypes.append(topupenttype)
            listOfTopUpEntDates.append(topupentdate)
            listOfTopUpPassengers.append(topuppassenger)
            listOfTopUpEntUnits.append(topupentunit)
            listOfTopUpEntValues.append(topupentvalue)
            topup = TopUp(topuptypes, topupcode, code, topupdesc, topupprice, topupenttype, topupentdate, topuppassenger, topupentunit, topupentvalue)
            listOfTopUpTitles.append(topup)
        else:
            listOfTopUpCodes.append(topupcode)
            listOfTopUpDesc.append(topupdesc)
            listOfTopUpPrices.append(topupprice)
            listOfTopUpEntTypes.append(topupenttype)
            listOfTopUpEntDates.append(topupentdate)
            listOfTopUpPassengers.append(topuppassenger)
            listOfTopUpEntUnits.append(topupentunit)
            listOfTopUpEntValues.append(topupentvalue)
            topup = TopUp(topuptypes, topupcode, code, topupdesc, topupprice, topupenttype, topupentdate, topuppassenger, topupentunit, topupentvalue)
            listOfTopUpTitles.append(topup)
        
#Program prints the category options and once an option is chosen the description is printed as well.        
           
for cat in listOfCatClasses:
    print("Enter",cat.Getcatcode(),"for",cat.Getcategory())

choice = int (input("Enter your choice "))
print("You chose ",listOfCatClasses[choice].Getcategory())
print("Category Description:", listOfCategoryDesc[choice])

#Program uses the category choice and prints the top up types within that category.
#Once a top up type has been chosen the program prints a description, price and whether the ticket is fixed or variable.

for tickettype in listOfTopUpTitles:
    if int(tickettype.Getcategorycode()) == choice:
        print("Enter",tickettype.Gettopupcode(),"for",tickettype.Gettopup())
topchoice = int(input("Enter the number you require "))
print("You have chosen ",listOfTopUpTitles[topchoice].Gettopup())
print("Top Up Descritpion:", listOfTopUpDesc[topchoice])
topprice = int(listOfTopUpPrices[topchoice])
print("The Price of this ticket is:","£",topprice/100)
print("This ticket is:", listOfTopUpEntTypes[topchoice])
print("Once activated this ticket is valid for:", listOfTopUpEntValues[topchoice], listOfTopUpEntUnits[topchoice])
print("This ticket expires:", listOfTopUpEntDates[topchoice])
print("This ticket is for:", listOfTopUpPassengers[topchoice])
