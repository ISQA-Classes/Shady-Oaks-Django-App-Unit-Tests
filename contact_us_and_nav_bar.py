import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome(executable_path="/Users/ckozeny/djangogirlscopy/myvenv/bin/chromedriver")

   def test_blog(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver 
       driver.get("http://shadyoaksgolfcourse.pythonanywhere.com") 
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='myHeader']/span/i").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='mySidebar']/a[5]").click()
       elem = driver.find_element_by_xpath("//*[@id='myHeader']/span/i").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='mySidebar']/a[4]").click()
       elem = driver.find_element_by_xpath("//*[@id='myHeader']/span/i").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='mySidebar']/a[5]").click()
       
       driver.get("http://shadyoaksgolfcourse.pythonanywhere.com/admin")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("http://shadyoaksgolfcourse.pythonanywhere.com")
       assert "Logged In"
       time.sleep(2)
       
       elem = driver.find_element_by_xpath("//*[@id='myHeader']/span/i").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='mySidebar']/a[5]").click()
       elem = driver.find_element_by_xpath("//*[@id='myHeader']/span/i").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='mySidebar']/a[4]").click()
       elem = driver.find_element_by_xpath("//*[@id='myHeader']/span/i").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='mySidebar']/a[5]").click()

       driver.get("http://shadyoaksgolfcourse.pythonanywhere.com/admin")
       elem = driver.find_element_by_xpath("//*[@id='user-tools']/a[3]").click()

       driver.get("http://shadyoaksgolfcourse.pythonanywhere.com")
       time.sleep(2) 


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()

