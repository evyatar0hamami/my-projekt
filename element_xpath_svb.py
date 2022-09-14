import time
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
import string


@pytest.fixture()
def setup():
    driver = webdriver.Chrome("/Users/evyatarhamami/Desktop/selenium/chromedriver")
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(3)
    yield driver
    time.sleep(2)
    driver.quit()


email_list = ['wtwqt@gmail.com', 'wtwqt@gmail.com', 'wallawallawalla.co.il', 'icloudicloud@icloud.com',
              'wallawalla@walla.com', 'yahooyahoo@yahoo.com']

password_list = ['qqqqqq', 'qqqqq', 'qqqqqqqqqqqqqqq']


first_name_list = ['qqqqqqqq', 'qqqqqq', 'QQQQQQ']


last_name_list = ['qqqqqq', 'qqqqqqqq', 'QQQQQQ']


def alternate_mails(y):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(y))


print((alternate_mails(5) + '@gmail.com'))


def alternate_name(a):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(a))


print((alternate_name(5)))


def scroll_down(setup):
    return setup.execute_script("window.scrollTo(0,document.body.scrollHeight)")


'''hp = home page'''


def hp_sign_in_page_button(setup):
    return setup.find_element_by_xpath("//button[text()='Sign In']")


def hp_sing_up_page_button(setup):
    return setup.find_element_by_xpath("//BUTTON[text()='Sign Up']")


'''sip = sing in page'''


def sip_enter_your_email(setup):
    return setup.find_element_by_xpath('//input[@class = "form-control"][1]')


def sip_enter_your_email_co_il(setup):
    return setup.find_element_by_xpath('//input[@class = "form-control"][1]')


def sip_enter_your_email_without_strudel(setup):
    return setup.find_element_by_xpath('//input[@class = "form-control"][1]')


def alternate_mail(setup):
    return setup.find_element_by_xpath('//input[@required=""][1]')


def sip_enter_your_password(setup):
    return setup.find_element_by_xpath('//input[@class="form-control"][2]')


def sip_sign_in_with_incorrect_password(setup):
    return setup.find_element_by_xpath('//input[@class="form-control"][2]')


def sip_sign_in_page_button(setup):
    return setup.find_element_by_xpath('//BUTTON[text()="Sign in"]')


def sip_forgot_password_button(setup):
    return setup.find_element_by_xpath('//A[@id="forgotId"]')


'''fp = forgot password'''


def fp_forgot_password_enter_your_email(setup):
    return setup.find_element_by_xpath('//INPUT[@id="inputForgotPassword"]')


def fp_forgot_password_reset_button(setup):
    return setup.find_element_by_xpath('//BUTTON[text()="Reset Password"]')


'''sup = sing up page'''


def sup_confirm_unmatch_password(setup):
    return setup.find_element_by_xpath("//input[@required=''][3]")


def sup_first_name_8_chart(setup):
    return setup.find_element_by_xpath("//input[@class='form-control'][1]")


def sup_last_name_8_chart(setup):
    return setup.find_element_by_xpath("(//INPUT[@class='form-control'])[2]")


def sup_last_name(setup):
    return setup.find_element_by_xpath("//input[@class='form-control'][2]")


def sup_create_password(setup):
    return setup.find_element_by_xpath("//input[@required=''][2]")


def sup_confirm_password(setup):
    return setup.find_element_by_xpath("//input[@required=''][3]")


def sup_create_password_15_chart(setup):
    return setup.find_element_by_xpath("//input[@required=''][2]")


def sup_confirm_password_15_chart(setup):
    return setup.find_element_by_xpath("//input[@required=''][3]")


def sup_first_name(setup):
    return setup.find_element_by_xpath("//input[@class='form-control'][1]")


def sup_first_name_in_capital_letters(setup):
    return setup.find_element_by_xpath("//input[@class='form-control'][1]")


def sup_last_name_in_capital_letters(setup):
    return setup.find_element_by_xpath("//input[@class='form-control'][2]")


def sup_create_password_in_capital_letters(setup):
    return setup.find_element_by_xpath("//input[@required=''][2]")


def sup_confirm_password_in_capital_letters(setup):
    return setup.find_element_by_xpath("//input[@required=''][3]")


def sup_sign_up_button(setup):
    return setup.find_element_by_xpath("//button[text()='Sign Up']")


'''mp = manu page'''


def mp_marking_combo_meal(setup):
    return setup.find_element_by_xpath("(//div[@class='card-body'])[1]")


def mp_marking_kids_meal(setup):
    return setup.find_element_by_xpath("(//DIV[@class='col-md-8'])[2]")


def mp_marking_burger(setup):
    return setup.find_element_by_xpath("(//div[@class='card-body'])[3]")


def mp_marking_vegan(setup):
    return setup.find_element_by_xpath("(//div[@class='card-body'])[4]")


def mp_marking_sides(setup):
    return setup.find_element_by_xpath("(//DIV[@class='card-body'])[5]")


def mp_reserve(setup):
    return setup.find_element_by_xpath("//button[2]")


def mp_log_out(setup):
    return setup.find_element_by_xpath("//BUTTON[text()=' Log out ']")


def mp_assert_reserve(setup):
    return setup.find_element_by_xpath("//button[2]")


def mp_sanity_assert_marking_kids_meal(setup):
    return setup.find_element_by_xpath("//button[@class = 'btn btn-primary'][2]")


def mp_assert_log_out_button(setup):
    return setup.find_element_by_xpath("//BUTTON[text()=' Log out ']")


'''summary1 = sum1'''


def sum1_send_button(setup):
    return setup.find_element_by_xpath("//BUTTON[text()='Send']")


def sum1_sanity_assert_price(setup):
    return setup.find_element_by_xpath("(//DIV[@class='col-6'])[4]")


def sum1_sanity_assert_subtotal(setup):
    return setup.find_element_by_xpath("(//LABEL)[2]")


def sum1_sanity_assert_service(setup):
    return setup.find_element_by_xpath("(//LABEL)[3]")


def sum1_sanity_assert_total(setup):
    return setup.find_element_by_xpath("//div[@class = 'col-6'][6]")

def sum1_4_3_assert_price1(setup):
    return setup.find_element_by_xpath("(//DIV[@class='col-6'][text()='45'])[1]")


def sum1_4_3_assert_price2(setup):
    return setup.find_element_by_xpath("(//DIV[text()='45'])[2]")


def sum1_4_3_assert_subtotal(setup):
    return setup.find_element_by_xpath("//*/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[4]/div[2]/label[1]")


def sum1_4_3_assert_service(setup):
    return setup.find_element_by_xpath("//*/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[4]/div[2]/label[2]")


def sum2_4_3_assert_total(setup):
    return setup.find_element_by_xpath("//*/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/h2[1]")


def sum1_4_4_assert_price1(setup):
    return setup.find_element_by_xpath("//DIV[@class='col-6'][text()='59']")


def sum1_4_4_assert_price2(setup):
    return setup.find_element_by_xpath("//DIV[@class='col-6'][text()='45']")


def sum1_4_4_assert_price3(setup):
    return setup.find_element_by_xpath("//DIV[text()='12']")


def sum1_4_4_assert_subtotal(setup):
    return setup.find_element_by_xpath("(//LABEL)[4]")


def sum1_4_4_assert_service(setup):
    return setup.find_element_by_xpath("(//LABEL)[5]")


def sum1_4_5_assert_price1(setup):
    return setup.find_element_by_xpath("(//DIV[@class='col-6'])[4]")


def sum1_4_5_assert_price2(setup):
    return setup.find_element_by_xpath("//DIV[@class='col-6'][text()='39']")


def sum1_4_5_assert_subtotal(setup):
    return setup.find_element_by_xpath("(//LABEL)[3]")


def sum1_4_5_assert_service(setup):
    return setup.find_element_by_xpath("(//LABEL)[4]")


def sum1_4_5_assert_total(setup):
    return setup.find_element_by_xpath("//div[@class = 'col-6'][6]")


def sum1_table_no_box_2_mael(setup):
    return setup.find_element_by_xpath("(//INPUT[@min='1'])[3]")


def sum1_4_6_assert_marking_vegan(setup):
    return setup.find_element_by_xpath("//BUTTON[@class='btn btn-primary'][text()=' Reserve ']") == False


def sum1_3_7_quantity_up_button(setup):
    return setup.find_element_by_xpath('//INPUT[@index="0"]')


'''summary2 = sum2'''


def sum2_sanity_assert_price(setup):
    return setup.find_element_by_xpath("(//H2)[1]")


def sum2_assert_tabel_no(setup):
    return setup.find_element_by_xpath("//*/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/h3[2]")


def sum2_assert_timer(setup):
    return setup.find_element_by_xpath("//SPAN/self::SPAN")


def sum2_4_5_assert_price(setup):
    return setup.find_element_by_xpath("(//H2)[1]")


def sum2_4_4_assert_price(setup):
    return setup.find_element_by_xpath("(//H2)[1]")

def assert_alert(setup):
    WebDriverWait(setup, 5).until(EC.alert_is_present())
    alert = setup.switch_to.alert
    alert_text = setup.switch_to.alert.text
    time.sleep(1)
    setup.switch_to.alert.accept()
    return alert_text




