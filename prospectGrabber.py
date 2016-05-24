'''
Created on Mar 22, 2016

@author: seanbarow
'''
from root.hooversGrabber import HooversGrabber

# Open a Hoover's instance to find the correct email address
handler = HooversGrabber()

company = input('What company are we targeting?')

# Search Hoovers
handler.hooverSearch(company)

allrows = handler.prospector()

headers = ['First Name', 'Last Name', 'Company', 'Email Address', 'Title', 'Street', 'City', 'State', 'Zip/PostalCode', 'Country', 'Lead Status']   
filename = 'output' + company + '.csv'
handler.csvCreator(headers, filename, allrows)     

handler.closeBrowser()        
