""" Installing Required modules
    pip install selenium
    pip install webdriver_manager """

from selenium import webdriver
from webdriver_manager.chrome import \
    ChromeDriverManager  # ChromeDriveManager will automatically deal with the driver required
from selenium.webdriver.common.by import By
import mysql.connector

conn = mysql.connector.connect(user="root", host="localhost", password="Rocky@222", database="mydata")
cursor = conn.cursor()

cursor.execute("truncate table categories")
cursor.execute("truncate table subcategories")
cursor.execute("truncate table states")
cursor.execute("truncate table company_details")
cursor.execute("truncate table jobs")
conn.commit()

driver = webdriver.Chrome(ChromeDriverManager().install())  # installing the driver required

driver.maximize_window()  # Maximizing the Window

category = []  # Initializing empty list to store categories
sub_category = []  # Initializing empty list to store categories


def login(email, password):
    url = "https://www.linkedin.com/"
    driver.get(url)
    driver.implicitly_wait(5)
    # driver.maximize_window()
    driver.find_element_by_id('session_key').send_keys(email)
    driver.find_element_by_id('session_password').send_keys(password)
    driver.find_element_by_class_name('sign-in-form__submit-button').click()
    driver.implicitly_wait(5)


def extract_cat_sub_cat():
    driver.get("https://www.careerguide.com/career-options")  # Getting the server

    r = driver.find_elements(By.XPATH, "//h2[contains(@class,'c-font-bold')]")  # Scraping the categories of Jobs
    sub_r = driver.find_elements(By.XPATH,
                                 "//ul[contains(@class,'c-content-list-1')]")  # Scraping the sub-categories of Jobs

    for ele in r:
        category.append(ele.text)
    for ele in sub_r:
        sub_category.append(ele.text)

    return category, sub_category


extract_cat_sub_cat()
login("movietrailerscom7@gmail.com", "Qwerty@123")

nn = 0
bb = 0
for cat in category[0:10]:
    print(cat)  # Printing the category
    list_of_sub_jobs = sub_category[nn].split("\n")
    print(list_of_sub_jobs)  # Jobs under the category printed by line 29
    print("-" * 100)
    driver.get("https://www.linkedin.com/jobs/")  # Getting the linkedin server to scrap required data
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,
                        "//section[contains(@class,'msg-overlay-bubble-header__details flex-row align-items-center ml1')]").click()
    driver.find_element(By.XPATH, "// input[contains( @ id, 'jobs-search-box-key')]").send_keys(list_of_sub_jobs[0])

    driver.find_element(By.XPATH, "//input[contains(@id,'jobs-search-box-location')]").send_keys("India")
    driver.find_element(By.XPATH, "//button[contains(@class,'jobs-search-box__submit-button')]").click()

    job_title_list = []
    company_list = []
    location_list = []

    """ Scraping the data from the results obtained after we clicked on search jobs button """

    job_titles = driver.find_elements(By.XPATH,
                                      "//a[contains(@class,'disabled ember-view job-card-container__link job-card-list__title')]")
    companies = driver.find_elements(By.XPATH,
                                     "//a[contains(@class,'job-card-container__link job-card-container__company-name ember-view')]")
    locations = driver.find_elements(By.XPATH, "//li[contains(@class, 'job-card-container__metadata-item')]")

    """ Storing the respective info. i.e job titles to the respective empty list created """

    for job in job_titles:
        job_title_list.append(job.text)
    for company in companies:
        company_list.append(company.text)
    for location in locations:
        location_list.append(location.text)

    mm = 0
    for profile in companies[0:1]:
        try:
            profile.click()
        except:
            profile.click()
        driver.implicitly_wait(5)
        about = driver.find_elements(By.XPATH,
                                     "//a[contains(@class, 't-16 t-bold t-black--light org-page-navigation__item-anchor ember-view pv3 ph4')]")
        for ab in about:
            ab.click()
            break
        driver.implicitly_wait(5)
        try:
            description = driver.find_element(By.XPATH,
                                              "//p[contains(@class, 'break-words white-space-pre-wrap mb5 text-body-small t-black--light')]")
        except:
            for ab in about:
                ab.click()
                break
            description = driver.find_element(By.XPATH,
                                              "//p[contains(@class, 'break-words white-space-pre-wrap mb5 text-body-small t-black--light')]")
        description = description.text

        description_f = ""
        for char in description:
            if char != '\n' and char != '\r':
                description_f = description_f + char
            else:
                description_f = description_f + ' '

        # print(description.text)
        other_info = driver.find_elements(By.XPATH, "//dd[contains(@class, 'text-body-small t-black--light')]")
        no_of_employees = other_info[2].text
        headquaters = other_info[4].text
        states = location_list[0].split()
        state = states[1]

        cursor.execute("INSERT INTO categories(sr_no, category) VALUES(%s,%s)", (bb + 1, cat))

        cursor.execute("INSERT INTO subcategories (sr_no, subcategory) VALUE (%s, %s)", (bb + 1, list_of_sub_jobs[0]))

        bb += 1
        cursor.execute("insert into states(sr_no, state) values (%s, %s)", (bb + 1, state))

        cursor.execute("INSERT INTO Jobs(Company, Job_Position, Location) VALUES(%s, %s ,%s)",
                       (company_list[mm], job_title_list[mm], location_list[mm]))

        cursor.execute("INSERT INTO Company_Details(Name, Description, State, Subcategory) VALUES(%s, %s, %s, %s)",
                       (company_list[mm], description_f, state, list_of_sub_jobs[0]))
        conn.commit()

        mm += 1

    nn += 1

driver.quit()