'''
Created on May 17, 2016

@author: seanbarow
'''
from root.myHoovers import MyHoovers

class HooversGrabber(MyHoovers):
    '''
    Sub class of MyHoovers to handle the special case of the hoover search for prospectGrabber
    '''
    def hooverSearch(self, myText):
        MyHoovers.hooverSearch(self, myText)
        
        input('Select the right company')
        
        # Go to View More People
        morePeopleElem = self.browser.find_element_by_link_text('View More People')
        morePeopleElem.click()
    
        
