# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 00:08:43 2017
Select secret santa pairings from set of names and email out results
@author: rmcin
"""
import random
import smtplib
def make_pairings(names):
    '''
    Use random generators to determine the secret santa pairings
    '''
    num_players = len(names)
    results = []
    index = 0
    while index < num_players:
        pairing = random.randint(0,num_players - 1)
        if results.count(pairing) == 0 and pairing != index:
            results.append(pairing)
            names[index][2] = names[pairing][0]
            index += 1
    return names

def email_results(from_addr, password, name, email, pairing):
   '''
   Sends an email to the given address, greeting with the name and enclosing the pairing
   '''
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.ehlo()
   server.starttls()
   server.login(from_addr, password)
   msg = "Subject: Secret Santa\nHey Loser (a.k.a " + name + ")!\n\nGuess who you got for secret santa? Yea, that's right, none other but " + pairing + ". I know, I know, I'm sorry, that they're lame.\n Anyways, get to shopping! Christmas won't buy itself!\n\nLove,\n\nYour Friendly Neighborhood Code Mom <3"
   server.sendmail(from_addr, email, msg)
   server.quit()

#matrix of players: a row is made up of a name, email, and paired name
players = [
        ["Rachel", "rmcintosh777@gmail.com", ""],
        ["Emily", "Care.emily.h@gmail.com", ""],
        ["Akash", "beherakash@gmail.com", ""],
        ]
#use random number generator to determine the pairings
make_pairings(players)
print(players)
#email out results
#get coordinator email login credentials
from_addr = input("Enter the email you would like to send this from: ")
password = input("Enter the password for this account: ")
for row in players:
    name = row[0]
    email = row[1]
    pairing = row[2]
    email_results(from_addr, password, name, email, pairing)
    




