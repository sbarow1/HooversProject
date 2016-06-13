'''
Created on May 13, 2016

@author: seanbarow
'''
import time
from selenium import webdriver
import csv
from selenium.common.exceptions import NoSuchElementException
from mySiteObject import MySiteObject

class MyHoovers(MySiteObject):
    '''
    This class contains the functions I use to interact with Hoovers
    '''
    def __init__(self, keyfile='/users/seanbarow/git/hooversproject/hooversproject/src/root/keyfile.txt'):
        '''
        Constructor
        '''
        MySiteObject.__init__(self, keyfile)
        
        # Open a Hoover's instance to find the correct email address
        self.browser = webdriver.Chrome('/users/seanbarow/pySean/chromedriver')
        self.browser.get('https://subscriber.hoovers.com/H/login/login.html')
        time.sleep(5)
        try:
            hooverUserElem = self.browser.find_element_by_css_selector('input#j_username.textInput')
            hooverUserElem.send_keys(self.username)
            hooverPassElem = self.browser.find_element_by_css_selector('input#j_password.textInput')
            hooverPassElem.send_keys(self.password)
            hooverPassElem.submit()
            time.sleep(5)
        except Exception as E:
            self.closeBrowser()
            print(E)
        
    def prospector(self):
        '''
        This grabs the Prospects information from the contact page
        '''
        rows = []
        counter = 0
        while True:
            answer = input('Do you have a prospect?')
            if answer == 'y':
                # Grab Name
                try:
                    firstName = self.browser.find_element_by_css_selector('span.given-name').text
                    lastName  = self.browser.find_element_by_css_selector('span.family-name').text                
                    title     = self.browser.find_element_by_css_selector('span.title').text
                    company   = self.browser.find_element_by_class_name('org').text
                    street    = self.browser.find_element_by_css_selector('div.street-address').text
                    city      = self.browser.find_element_by_css_selector('span.locality').text
                    state     = self.browser.find_element_by_css_selector('abbr.region').text
                    zipCode   = self.browser.find_element_by_css_selector('span.postal-code').text
                    country   = self.browser.find_element_by_css_selector('div.country-name').text               
                except NoSuchElementException:
                    print('One of the elements does not exist')
                    continue
                try:
                    emailAddr = self.browser.find_element_by_css_selector('a.email').text
                except NoSuchElementException:
                    decision = input('No email, is that okay?')
                    if decision == 'y':
                        emailAddr = 'None'
                    else:
                        continue
                print('%s %s %s %s %s %s %s %s %s' % (firstName, lastName, emailAddr, title, street, city, state, zipCode, country))
                counter += 1
                print('Count = %s' % counter)
                rows.append([firstName, lastName, company, emailAddr, title, street, city, state, zipCode, country, 'open'])
            else:
                break
        return rows 
     
    def hooverSearch(self, myText):
        '''
        This will search Hoovers for the correct page
        '''
        hooverSearchElem = self.browser.find_element_by_name('searchValue')
        hooverSearchElem.send_keys(myText)
        hooverSearchElem.submit()
        
    # TODO: Change this to a sub class of MyHoovers that extends MyHoovers.hooverSearch method with the below and a call
    # to the MyHoovers.hooverSearch.
    def hooverViewMorePeople(self):
        input('Select the right company')

        # Go to View More People
        morePeopleElem = self.browser.find_element_by_link_text('View More People')
        morePeopleElem.click()
               
    def csvCreator(self, header, filename, rows):
        '''
        This creates a csv output file with the specified header information, filename and rows
        '''
        with open(filename, 'w', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(header)
            f_csv.writerows(rows)
            
