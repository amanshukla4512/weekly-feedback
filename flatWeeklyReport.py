from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


roll_no = input("Enter University Roll Number: ")
pswd = input("Enter Password: ")


driver = webdriver.Chrome("C:\\Users\\Aman Shukla\\AppData\\Local\\Temp\\Temp1_chromedriver_win32.zip\\chromedriver.exe")  # eg: C:\\Users\\xyz\\Desktop\\chromedriver.exe


platform_used = "Google Classroom, Whatsapp, Google Forms"


driver.set_page_load_timeout(60)
driver.get("https://makaut1.ucanapply.com/smartexam/public/")
driver.find_element_by_class_name("databox-sky").click()
driver.implicitly_wait(10)

#login
rollField = driver.find_element_by_id("username")
time.sleep(1)
for i in range(0, len(roll_no)):
    rollField.send_keys(roll_no[i])
pswdField = driver.find_element_by_id("password")
time.sleep(1)
for i in range(0, len(pswd)):
    pswdField.send_keys(pswd[i])
driver.find_element_by_class_name("btn-success").click()


driver.implicitly_wait(10)
driver.find_element_by_link_text("Weekly Activity Report").click()    # opens form to be filled
driver.implicitly_wait(10)


# data for FLAT

flat = {
    "assignment on previous work": "2020-03-20 101",
    "myhill nerode theorem": "2020-03-23 102",
    "assignment on myhill nerode theorem": "2020-03-24 102",
    "equivalence of two automata": "2020-03-25 102",
    "NFA with empty moves": "2020-03-26 102",
    "DFA to grammar and vice versa": "2020-03-27 102",
    "assignment on DFA to grammar conversion": "2020-03-30 103",
    "pumping lemma on regular language": "2020-03-31 103",
    "questions on regular expression": "2020-04-02 103",
    "solution of the questions given on regular expression": "2020-04-03 103",
    "doubt cleaning session on regular expression": "2020-04-06 104",
    "context free grammar (CFG) - derivations": "2020-04-07 104",
    "quiz on regular expression": "2020-04-08 104",
    "CFG - ambiguity": "2020-04-09 104",
    "CFG - simplification": "2020-04-13 104",
    "CFG - simplification continued": "2020-04-15 105",
    "CFG - Chomsky normal form": "2020-04-17 105",
    "CFG - Greibach normal form": "2020-04-18 105",
    "quiz on CFG": "2020-04-21 106",
    "pumping lemma for CFL with assignment": "2020-04-23 106",
    "assignment on CFG": "2020-04-27 107",

}

for key in flat:
    # week
    drp = Select(driver.find_element_by_id("week"))
    drp.select_by_value(flat[key][11:])

    # semcode
    drp = Select(driver.find_element_by_id("SEMCODE"))
    drp.select_by_value("SM04")

    # course
    driver.find_element_by_css_selector("[data-id='COURSECD']").click()  # course
    driver.find_element_by_css_selector("[data-original-index='1']").click()

    # subject
    drp = Select(driver.find_element_by_id("SUBJECTCODE"))
    drp.select_by_value("SU00016088")  # for flat

    # topic covered
    driver.find_element_by_id("topic_covered").click()
    driver.find_element_by_id("topic_covered").send_keys(key)

    # platform_used
    driver.find_element_by_id("platform_used").send_keys(platform_used)

    # teacher
    drp = Select(driver.find_element_by_id("class_taken_by"))
    drp.select_by_value("181264")  # for Namrata Mam

    # date-time
    driver.execute_script("document.getElementById('date_tme').removeAttribute('readonly', 0);")
    date_time = driver.find_element_by_id("date_tme")
    date_time.clear()
    date_time.send_keys(flat[key][0:10] + " 11:00")

    # Lecture Link
    driver.find_element_by_id("record_lecture_upload_link").send_keys("NA")
    driver.find_element_by_id("duration_in_min").send_keys("60")
    driver.find_element_by_id("post_class_interraction_note").send_keys("Google Classroom")
    driver.find_element_by_id("assignment_received").send_keys("IN GOOGLE CLASSROOM")
    driver.find_element_by_id("assignment_submitted").send_keys("IN GOOGLE CLASSROOM")
    driver.find_element_by_id("test_attended_if_any").send_keys("NO")
    driver.find_element_by_id("daily_self_acitvity").send_keys("Reading Materials and Revision")
    driver.find_element_by_id("remark").send_keys("Good")
    driver.find_element_by_id("btnSubmit").click()
    time.sleep(2)
    driver.get("https://makaut1.ucanapply.com/smartexam/public/student/week-report-activity/create")


