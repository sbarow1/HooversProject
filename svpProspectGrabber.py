'''
Created on May 2, 2016

@author: seanbarow
'''
import root.myHoovers

# Open a Hoover's instance to find the correct email address
handler = root.myHoovers.MyHoovers('keyfile.txt')

# Get the saved search that we want
handler.driver.get('http://subscriber.hoovers.com/H/search/runSavedSearch.html?searchId=35849970294&runSearch=true')

#rows = []
#counter = 0
# Create the csv Writer
#while True:
           
#        answer = input('Do you have a prospect?')
#        if answer == 'y':
#            # Grab Name
#            try:
#                firstName = driverH.find_element_by_css_selector('span.given-name').text
#                lastName = driverH.find_element_by_css_selector('span.family-name').text                
#                title = driverH.find_element_by_css_selector('span.title').text
#                street = driverH.find_element_by_css_selector('div.street-address').text
#                company = driverH.find_element_by_class_name('org').text
#                city = driverH.find_element_by_css_selector('span.locality').text
#                state = driverH.find_element_by_css_selector('abbr.region').text
#                zipCode = driverH.find_element_by_css_selector('span.postal-code').text
#                country = driverH.find_element_by_css_selector('div.country-name').text               
#            except NoSuchElementException:
#                print('One of the elements does not exist')
#                continue
#            try:
#                emailAddr = driverH.find_element_by_css_selector('a.email').text
#            except NoSuchElementException:
#                decision = input('No email, is that okay?')
#                if decision == 'y':
#                    emailAddr = 'None'
#                else:
#                    continue
#            print('%s %s %s %s %s %s %s %s %s %s' % (firstName, lastName, company, emailAddr, title, street, city, state, zipCode, country))
#            counter += 1
#            print('Count = %s' % counter)
#            rows.append([firstName, lastName, company, emailAddr, title, street, city, state, zipCode, country, 'open'])
#        else:
#            break
allrows = handler.prospector()

headers = ['First Name', 'Last Name', 'Company', 'Email Address', 'Title', 'Street', 'City', 'State', 'Zip/PostalCode', 'Country', 'Lead Status']   
filename = input('Give me a filename')
handler.csvCreator(headers, filename, allrows)    

handler.closeBrowser()        