from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    # This Chromedriver link needs to be updated based on local file structure.
    driver = webdriver.Chrome(executable_path='C:\Selenium\chromedriver_win32\chromedriver.exe')
    driver.implicitly_wait(30)
    driver.maximize_window()
    print("Opening Shady Oaks Home Page")

    # If new pythonanywhere site is used, update this hard-coded value.
    driver.get("http://aghermanek.pythonanywhere.com")
    print("Got to Home Page")

    #first page objects
    login_button = driver.find_element_by_css_selector("#myHeader > span > p > a")

    login_button.click()
    print("Log in button clicked")

    #second page objects
    username_button = driver.find_element_by_css_selector("#id_username")
    password_button = driver.find_element_by_css_selector("#id_password")
    submit_button = driver.find_element_by_css_selector("body > div > form > input[type='submit']:nth-child(4)")

    username_button.send_keys("instructor")
    print("username input entered")

    password_button.send_keys("instructor1a")
    print("password input entered")

    submit_button.click()
    print("Submit button clicked")

    driver.implicitly_wait(30)

    header = driver.find_element_by_css_selector("body > div.page-container > h2")

    if header.is_displayed():
        print("Reached Home page with successful login!")

    else:
        print("Login Failed. Try Again.")
        driver.close()

    #logout functionality

    logout_button = driver.find_element_by_css_selector("#myHeader > span > p > a")

    logout_button.click()
    print("Clicked logout button")

    driver.implicitly_wait(10)

    logout_header = driver.find_element_by_css_selector("body > div > h2")

    if logout_header.is_displayed():
        print("Reached Logout page successfully!")
        driver.close()

    else:
        print("Logout Failed.")
        driver.close()

if __name__ == "__main__":
   main()
