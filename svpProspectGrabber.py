'''
Created on May 2, 2016

@author: seanbarow
'''
import root.myHoovers

# Open a Hoover's instance to find the correct email address
handler = root.myHoovers.MyHoovers('keyfile.txt')

# Get the saved search that we want
handler.driver.get('http://subscriber.hoovers.com/H/search/runSavedSearch.html?searchId=35849970294&runSearch=true')

allrows = handler.prospector()

headers = ['First Name', 'Last Name', 'Company', 'Email Address', 'Title', 'Street', 'City', 'State', 'Zip/PostalCode', 'Country', 'Lead Status']   
filename = input('Give me a filename')
handler.csvCreator(headers, filename, allrows)    

handler.closeBrowser()        
