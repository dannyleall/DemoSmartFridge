from selenium import webdriver
#this is the bridge between our code and the web (chrome)

from selenium.webdriver.common.keys import Keys
# this allows to actually use keyboard buttons

from selenium.webdriver.common.action_chains import ActionChains
#allows for actions like mouse hover, drag and drop

import time
# we use this to keep the browser open

def AutoBuy():
    
    try:
        # internet is variable and launches chrome driver
        internet = webdriver.Chrome()
        action = ActionChains(internet)
        
        # goes to amazon login        
        internet.get('https://www.amazon.com/')
        time.sleep(1)
        FirstDropDown = internet.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[3]/div/a[2]')
    
        # makes mouse hover over "accounts"
        action.move_to_element(FirstDropDown).perform()
    
        # clicks sign in button after hovering over the accounts drop down
        time.sleep(1)
        SignIn = internet.find_element_by_xpath('/html/body/div[1]/header/div/div[3]/div[3]/div[2]/div/div[1]/div/a/span')
        SignIn.click()
        
        # enters the username into the text box
        time.sleep(1)
        EnterUsername = internet.find_element_by_xpath('//*[@id="ap_email"]')
        EnterUsername.send_keys('automationtempproject@gmail.com')
        
        time.sleep(1)
        Continue = internet.find_element_by_xpath('//*[@id="continue"]')
        Continue.click()
        
        time.sleep(1)
        EnterPassword = internet.find_element_by_xpath('//*[@id="ap_password"]')
        EnterPassword.send_keys('automation123')
        
        time.sleep(1)
        LogIn = internet.find_element_by_xpath('//*[@id="signInSubmit"]')
        LogIn.click()
        
        time.sleep(1)
        Search = internet.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
        Search.send_keys('bananas')
        
        time.sleep(1)
        Find = internet.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
        Find.click()
        
        time.sleep(1)
        SortDropDown = internet.find_element_by_xpath('//*[@id="a-autoid-0-announce"]/span[1]')
        SortDropDown.click()
        
        time.sleep(1)
        lowToHigh = internet.find_element_by_xpath('//*[@id="s-result-sort-select_1"]')
        lowToHigh.click()
        
        time.sleep(1)
        itemBuy = internet.find_element_by_link_text('Fresh Organic Bananas Approximately 3 Lbs 1 Bunch of 6-9 Bananas')
        itemBuy.click()
        
        time.sleep(1)
        addToCart = internet.find_element_by_xpath('//*[@id="add-to-cart-button"]')
        addToCart.click()
        
        time.sleep(1)

        return True
        
    except:
        print('Error while trying to add item to cart.')
        return False