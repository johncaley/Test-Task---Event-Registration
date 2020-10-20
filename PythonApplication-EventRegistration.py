####################################################
#                                                  #
#   Project: Test Task - Event Registration        #
#   Author: John Caley                             #
#   Version: 1.0.0                                 #
#   Date: 10/20/2020                               #
#                                                  #
####################################################
import json

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Lead:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

ContactsList = []
LeadsList = []
RegistrantsList = []

#Create list of Contacts
ContactsList.append(Contact("Alice Brown", None, "1231112223"))
ContactsList.append(Contact("Bob Crown", "bob@crowns.com", None))
ContactsList.append(Contact("Carlos Drew", "carl@drewess.com", "3453334445"))
ContactsList.append(Contact("Doug Emerty", None, "4564445556"))
ContactsList.append(Contact("Egan Fair", "eg@fairness.com", "5675556667"))

#Create list of Leads
LeadsList.append(Lead(None, "kevin@keith.com", None))
LeadsList.append(Lead("Lucy", "lucy@liu.com", None))
LeadsList.append(Lead("Mary Middle", "mary@middle.com", "3331112223"))
LeadsList.append(Lead(None, None , "4442223334"))
LeadsList.append(Lead(None, "ole@olson.com", None))

#Create list of Registrants
RegistrantsList.append(json.loads('{ "name":"Lucy Liu", "email":"lucy@liu.com", "phone":"3210001112" }'))
RegistrantsList.append(json.loads('{ "name":"Doug", "email":"doug@emmy.com", "phone":"4564445556" }'))
RegistrantsList.append(json.loads('{ "name":"Uma Thurman", "email":"uma@thurs.com", "phone":null }'))


for i in RegistrantsList:
    match = False

    #Try to match registrant's email to our Contact list
    for j in ContactsList:  
        if (i["email"] == j.email and j.email != None):
            if (j.phone == None):
                j.phone = i["phone"]
            match = True
            break
    #Try to match registrant's phone to our Contacts list
    if (match == False):
        for j in ContactsList:  
            if (i["phone"] == j.phone and j.phone != None):
                if (j.email == None):
                    j.email = i["email"]
                match = True
                break

    #Try to match out LeadsList with email
    if (match == False):
        for j in LeadsList:
            if (i["email"] == j.email and j.email != None):
                name = i["name"]
                email = i["email"]
                phone = i["phone"]
                ContactsList.append(Contact(name, email, phone))
                LeadsList.remove(j)
                match = True
                break

    #Try to match our Leads with phone
    if (match == False):
        for j in LeadsList:
            if (i["phone"] == j.phone and j.phone != None):
                name = i["name"]
                email = i["email"]
                phone = i["phone"]
                ContactsList.append(Contact(name, email, phone))
                LeadsList.remove(j)
                match = True
                break

    #If no match is found, simply add it to ContactsList
    if (match == False):
        name = i["name"]
        email = i["email"]
        phone = i["phone"]
        ContactsList.append(Contact(name, email, phone))

#Write ContactList to text file
f = open('ContactList.txt', 'a')
for i in ContactsList:
    f.write(i.name + " | " + str(i.email) + " | " + str(i.phone) + "\n")
f.close()



  