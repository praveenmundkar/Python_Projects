""" Installing Required modules
    pip install selenium
    pip install webdriver_manager """


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager                    # ChromeDriveManager will automatically deal with the driver required
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())                  # installing the driver required

driver.maximize_window()                                                    # Maximizing the Window

driver.get("https://www.careerguide.com/career-options")                    # Getting the server


r = driver.find_elements(By.XPATH, "//h2[contains(@class,'c-font-bold')]")  # Scraping the categories of Jobs
sub_r = driver.find_elements(By.XPATH, "//ul[contains(@class,'c-content-list-1')]")  # Scraping the sub-categories of Jobs

category = []                                                               # Initializing empty list to store categories
sub_category = []                                                           # Initializing empty list to store categories
for ele in r:
    category.append(ele.text)
for ele in sub_r:
    sub_category.append(ele.text)
ss = 0
nn = 0
for cat in category:
    print(cat)                                                               # Printing the category
    list_of_sub_jobs = sub_category[nn].split("\n")
    print(list_of_sub_jobs)                                                  # Jobs under the category printed by line 29
    nn += 1
    print("-"*100)
    driver.get("https://in.linkedin.com/jobs")                                 # Getting the linkedin server to scrap required data
    driver.find_element(By.XPATH, "//input[contains(@name,'location')]").clear()        # clear if there is any auto-input
    driver.find_element(By.XPATH, "//input[contains(@name,'location')]").send_keys("India")                # Sending location key as india
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Search job titles or companies')]").send_keys(list_of_sub_jobs[0])            # Sending subcategory key as input
    driver.find_element(By.XPATH, "//button[contains(@data-searchbar-type,'JOBS')]").click()                                                # Click search job button                                                  # scraping the results
    job_title_list = []
    company_list = []
    location_list = []

    """ Scraping the data from the results obtained after we clicked on search jobs button """

    job_titles = driver.find_elements(By.XPATH, "//h3[contains(@class,'base-search-card__title')]")
    companies = driver.find_elements(By.XPATH, "//h4[contains(@class,'base-search-card__subtitle')]")
    locations = driver.find_elements(By.XPATH, "//span[contains(@class,'job-search-card__location')]")

    """ Storing the respective info. i.e job titles to the respective empty list created """

    for job in job_titles:
        job_title_list.append(job.text)
    for company in companies:
        company_list.append(company.text)
    for location in locations:
        location_list.append(location.text)
    mm = 0

    """ Scraping the links of the jobs to get more about them by iterating one by one i.e company description, no. of employees, headquater location of the respective company"""

    links = driver.find_elements(By.XPATH, "//a[contains(@class,'base-card__full-link')]")

    """ Iterating the links scraped to get the data required and then display them """

    for link in links:
        employees_locations = []
        f_e = []
        desc = ""

        """ Using try block to ensure if we do not get the company page or any redirected sesions can be handled easily """

        try:
            link.click()                                                                                                                        # Click the result
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, "//a[contains(@class,'topcard__org-name-link')]").click()                                             # click company profile link

            """ Handling the new created window i.e the child window """

            childwindow = driver.window_handles[1]
            parentwindow = driver.window_handles[0]
            driver.switch_to.window(childwindow)                                                                                                 # Switching to the child window

            desc = driver.find_element(By.XPATH, "//p[contains(@class,'about-us__description')]")                                                # scrape description

            desc = desc.text

            fe = driver.find_elements(By.XPATH, "//dd[contains(@class,'basic-info-item__description')]")                                         # Scraping their info. i.e no. of employees and headquater location
            for fe in fe:
                # print(fe.text)
                f_e.append(fe)
            employees_locations.append(f_e[2])
            employees_locations.append(f_e[3])
            driver.implicitly_wait(5)

            """ Printing the Information that we required from our desired output """

            print(job_title_list[mm])
            print(company_list[mm])
            print(location_list[mm])
            print("Description about the company", desc)
            print("No of employees", employees_locations[0].text)
            print("Headquaters at :: ", employees_locations[1].text)
            mm = mm + 1
            links = ""
            print("*"*100)
            print("*"*100)
            driver.close()                                                                      # Closing the child window which is now no. longer required to avoid conflicting errors due to the window
            driver.switch_to.window(parentwindow)                                               # Re-switching to the parent window

        except:
            print("occurred some error")                                                        # The errors may be like while we click on company page by line 75 it may get unwanted popup windows or the page may not available, etc
            print("*" * 100)
            print("*" * 100)
            pass

        finally:
            break                                                    # break by getting one job profile(i.e sub-category) for each category 🔲 NOTE  ::: REMOVE THE finally BLOCK to get every JOB info of each CATEGORY


driver.quit()                                                        # Exit the program by closing all windows

