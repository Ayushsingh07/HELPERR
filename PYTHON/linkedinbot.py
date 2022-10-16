import os, random, sys, time
from selenium import webdriver
from bs4 import BeautifulSoup
browser = webdriver.Chrome(r'/Users/aryansharma/Desktop/linkedin bot-2/chromedriver')
browser.get('https://www.linkedin.com/uas/login')
file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]
elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()
visitingProfileID = '/in/aarya-tadvalkar-092650193/'
fullLink = 'https://www.linkedin.com' + visitingProfileID
browser.get(fullLink)
visitedProfiles = []
profilesQueued = []

def getNewProfileIDs(soup, profilesQueued):
    profilesID = []
    print("printing soup", soup)
    
    pav = soup.find(id='ember456')
    
    print(pav)

    
    all_links = pav.findAll('a', {'class': 'ember-view pv-browsemap-section__member align-items-center'})
    for link in all_links:
        userID = link.get('href')
        if((userID not in profilesQueued) and (userID not in visitedProfiles)):
            profilesID.append(userID)
    return profilesID

getNewProfileIDs(BeautifulSoup(browser.page_source, features="html.parser"), profilesQueued)
['/in/saransh-kotha-567a84182/',
 '/in/sonali-bedade-0519071ab/',
 '/in/shreya-mali-1a6456191/',
 '/in/advait-raut-6a060616b/',
 '/in/swati-tiwari12/',
 '/in/srishti-s-agrawal/',
 '/in/preyashgothane/',
 '/in/mohini-chaudhari-b77a74155/',
 '/in/ketan-mankar/',
 '/in/shubhra-masurkar-940a3a1a4/']
profilesQueued = getNewProfileIDs(BeautifulSoup(browser.page_source), profilesQueued)
while profilesQueued:
    try:
        visitingProfileID = profilesQueued.pop()
        visitedProfiles.append(visitingProfileID)
        fullLink = 'https://www.linkedin.com' + visitingProfileID
        browser.get(fullLink)

        browser.find_element_by_class_name('pv-s-profile-actions').click()

        browser.find_element_by_class_name('mr1').click()

        customMessage = "Hello, I have found mutual interest area and I would be more than happy to connect with you. Kindly, accept my invitation. Thanks!"
        elementID = browser.find_element_by_id('custom-message')
        elementID.send_keys(customMessage)

        browser.find_element_by_class_name('ml1').click()

        
        with open('visitedUsers.txt', 'a') as visitedUsersFile:
            visitedUsersFile.write(str(visitingProfileID)+'\n')
        visitedUsersFile.close()

        
        soup = BeautifulSoup(browser.page_source)
        try: 
            profilesQueued.extend(getNewProfileIDs(soup, profilesQueued))
        except:
            print('Continue')

        
        time.sleep(random.uniform(3, 7)) 

        if(len(visitedProfiles)%50==0):
            print('Visited Profiles: ', len(visitedProfiles))

        if(len(profilesQueued)>100000):
            with open('profilesQueued.txt', 'a') as visitedUsersFile:
                visitedUsersFile.write(str(visitingProfileID)+'\n')
            visitedUsersFile.close()
            print('100,000 Done!!!')
            break;
    except:
        print('error')
