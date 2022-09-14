from element_xpath_svb import *

'''sanity'''


def test_sanity(setup):
    hp_sign_in_page_button(setup).click()
    sip_enter_your_email(setup).send_keys(email_list[0])
    sip_enter_your_password(setup).send_keys(password_list[0])
    sip_sign_in_page_button(setup).click()
    mp_marking_kids_meal(setup).click()
    time.sleep(1)
    assert mp_sanity_assert_marking_kids_meal(setup).is_displayed()
    scroll_down(setup)
    time.sleep(1)
    mp_reserve(setup).click()
    time.sleep(1)
    assert sum1_sanity_assert_price(setup).text == '39'
    assert sum1_sanity_assert_subtotal(setup).text == 'Subtotal: 39$'
    assert sum1_sanity_assert_service(setup).text == 'Service: 3.9$'
    assert sum1_sanity_assert_total(setup).text == 'Total: 42.9$'
    sum1_send_button(setup).click()
    assert sum2_sanity_assert_price(setup).text == 'Total: 42.9$'
    assert sum2_assert_tabel_no(setup).text == '1'
    assert sum2_assert_timer(setup).is_displayed()


'''sign in fun test'''


def test_1_1_forgot_password(setup):
    hp_sign_in_page_button(setup).click()
    sip_forgot_password_button(setup).click()
    fp_forgot_password_enter_your_email(setup).send_keys(email_list[0])
    fp_forgot_password_reset_button(setup).click()
    assert assert_alert(setup)


def test_1_2_sip_sign_in_icloud(setup):
    hp_sign_in_page_button(setup).click()
    sip_enter_your_email(setup).send_keys(email_list[3])
    sip_enter_your_password(setup).send_keys(password_list[0])
    sip_sign_in_page_button(setup).click()
    assert mp_assert_log_out_button(setup).is_displayed()


def test_1_3_sign_in_walla_mail(setup):
    hp_sign_in_page_button(setup).click()
    sip_enter_your_email(setup).send_keys(email_list[4])
    sip_enter_your_password(setup).send_keys(password_list[0])
    sip_sign_in_page_button(setup).click()
    assert mp_assert_log_out_button(setup).is_displayed()


def test_1_4_sip_sign_in_with_co_il(setup):
    hp_sign_in_page_button(setup).click()
    sip_enter_your_email_co_il(setup).send_keys(email_list[1])
    sip_enter_your_password(setup).send_keys(password_list[0])
    sip_sign_in_page_button(setup).click()


def test_1_5_sip_sign_in_yahoo_mail(setup):
    hp_sign_in_page_button(setup).click()
    sip_enter_your_email(setup).send_keys(email_list[5])
    sip_enter_your_password(setup).send_keys(password_list[0])
    sip_sign_in_page_button(setup).click()
    assert mp_assert_log_out_button(setup).is_displayed()


'''sign in eh test'''


def test_1_6_email_address_without_strudel(setup):
    hp_sign_in_page_button(setup).click()
    sip_enter_your_email_without_strudel(setup).send_keys(email_list[2])
    sip_enter_your_password(setup).send_keys(password_list[0])
    sip_sign_in_page_button(setup).click()
    assert assert_alert(setup)


def test_1_7_sign_in_with_incorrect_password(setup):
    hp_sign_in_page_button(setup).click()
    sip_enter_your_email(setup).send_keys(email_list[0])
    sip_sign_in_with_incorrect_password(setup).send_keys(password_list[1])
    sip_sign_in_page_button(setup).click()
    assert assert_alert(setup)


'''sign up fun test '''


def test_2_1_sign_up_with_first_name_that_contains_7_chars(setup):
    hp_sing_up_page_button(setup).click()
    sup_first_name_8_chart(setup).send_keys(first_name_list[0])
    sup_last_name(setup).send_keys(last_name_list[0])
    alternate_mail(setup).send_keys((alternate_mails(5) + '@gmail.com'))
    sup_create_password(setup).send_keys(password_list[0])
    sup_confirm_password(setup).send_keys(password_list[0])
    setup.save_screenshot("/Users/evyatarhamami/PycharmProjects/pytest/save_screenshot/test_2_1.png")
    sup_sign_up_button(setup).click()
    assert mp_assert_log_out_button(setup).is_displayed()


def test_2_2_sign_up_with_last_name_that_contains_8_chars(setup):
    hp_sing_up_page_button(setup).click()
    sup_first_name(setup).send_keys(first_name_list[1])
    sup_last_name_8_chart(setup).send_keys(last_name_list[1])
    alternate_mail(setup).send_keys((alternate_mails(5) + '@gmail.com'))
    sup_create_password(setup).send_keys(password_list[0])
    sup_confirm_password(setup).send_keys(password_list[0])
    setup.save_screenshot("/Users/evyatarhamami/PycharmProjects/pytest/save_screenshot/test_2_2.png")
    sup_sign_up_button(setup).click()
    mp_assert_log_out_button(setup).is_displayed()


def test_2_3_sign_with_first_name_in_capital_letters(setup):
    hp_sing_up_page_button(setup).click()
    sup_first_name_in_capital_letters(setup).send_keys(first_name_list[2])
    sup_last_name(setup).send_keys(last_name_list[0])
    alternate_mail(setup).send_keys((alternate_mails(5) + '@gmail.com'))
    sup_create_password(setup).send_keys(password_list[0])
    sup_confirm_password(setup).send_keys(password_list[0])
    setup.save_screenshot("/Users/evyatarhamami/PycharmProjects/pytest/save_screenshot/test_2_3.png")
    sup_sign_up_button(setup).click()
    time.sleep(3)
    mp_assert_log_out_button(setup).is_displayed()


def test_2_4_sign_with_last_name_in_capital_letters(setup):
    hp_sing_up_page_button(setup).click()
    sup_first_name(setup).send_keys(first_name_list[1])
    sup_last_name_in_capital_letters(setup).send_keys(last_name_list[2])
    alternate_mail(setup).send_keys((alternate_mails(5) + '@gmail.com'))
    sup_create_password(setup).send_keys(password_list[0])
    sup_confirm_password(setup).send_keys(password_list[0])
    setup.save_screenshot("/Users/evyatarhamami/PycharmProjects/pytest/save_screenshot/test_2_4.png")
    sup_sign_up_button(setup).click()
    mp_assert_log_out_button(setup).is_displayed()


def test_2_5_sign_in_with_password_in_capital_letters(setup):
    hp_sing_up_page_button(setup).click()
    sup_first_name(setup).send_keys("qqqqqq")
    sup_last_name(setup).send_keys("qqqqqq")
    alternate_mail(setup).send_keys((alternate_mails(5) + '@gmail.com'))
    sup_create_password_in_capital_letters(setup).send_keys('QQQQQQ')
    sup_confirm_password_in_capital_letters(setup).send_keys('QQQQQQ')
    setup.save_screenshot("/Users/evyatarhamami/PycharmProjects/pytest/save_screenshot/test_2_5.png")
    sup_sign_up_button(setup).click()
    mp_assert_log_out_button(setup).is_displayed()


'''sign up eh test'''


def test_2_6_sign_up_password_and_password_confirm_dont_match(setup):
    hp_sing_up_page_button(setup).click()
    sup_first_name(setup).send_keys(first_name_list[0])
    sup_last_name(setup).send_keys(last_name_list[1])
    alternate_mail(setup).send_keys((alternate_mails(5) + '@gmail.com'))
    sup_create_password(setup).send_keys(password_list[0])
    sup_confirm_unmatch_password(setup).send_keys(password_list[1])
    setup.save_screenshot("/Users/evyatarhamami/PycharmProjects/pytest/save_screenshot/test_2_6.png")
    sup_sign_up_button(setup).click()
    assert assert_alert(setup)


def test_2_7_sign_in_with_15_chars_passwords(setup):
    hp_sing_up_page_button(setup).click()
    sup_first_name(setup).send_keys(first_name_list[0])
    sup_last_name(setup).send_keys(last_name_list[1])
    alternate_mail(setup).send_keys((alternate_mails(5) + '@gmail.com'))
    sup_create_password_15_chart(setup).send_keys(password_list[2])
    sup_confirm_password_15_chart(setup).send_keys(password_list[2])
    setup.save_screenshot("/Users/evyatarhamami/PycharmProjects/pytest/save_screenshot/test_2_7.png")
    sup_sign_up_button(setup).click()
    assert assert_alert(setup)


'''Reservation and confirm reservation fun test'''


def test3_1_canceled_meal_selection(setup):
    hp_sign_in_page_button(setup).click()
    sip_enter_your_email(setup).send_keys(email_list[0])
    sip_enter_your_password(setup).send_keys(password_list[0])
    sip_sign_in_page_button(setup).click()
    mp_marking_kids_meal(setup).click()
    mp_marking_kids_meal(setup).click()
    assert mp_assert_reserve(setup)


def test_3_2_logout(setup):
    hp_sign_in_page_button(setup).click()
    sip_enter_your_email(setup).send_keys(email_list[0])
    sip_enter_your_password(setup).send_keys(password_list[0])
    sip_sign_in_page_button(setup).click()
    time.sleep(2)
    scroll_down(setup)
    time.sleep(2)
    mp_log_out(setup).click()
    assert hp_sign_in_page_button(setup).is_displayed()


def test_3_3_order_2_meal_burger_vegan(setup):
    hp_sign_in_page_button(setup).click()
    sip_enter_your_email(setup).send_keys(email_list[0])
    sip_enter_your_password(setup).send_keys(password_list[0])
    sip_sign_in_page_button(setup).click()
    mp_marking_burger(setup).click()
    mp_marking_vegan(setup).click()
    scroll_down(setup)
    time.sleep(2)
    mp_reserve(setup).click()
    assert sum1_4_3_assert_price1(setup).text == '45'
    assert sum1_4_3_assert_price2(setup).text == '45'
    assert sum1_4_3_assert_subtotal(setup).text == 'Subtotal: 90$'
    assert sum1_4_3_assert_service(setup).text == 'Service: 9$'
    sum1_send_button(setup).click()
    assert sum2_4_3_assert_total(setup).text == 'Total: 99$'
    assert sum2_assert_tabel_no(setup).text == '1'
    assert sum2_assert_timer(setup).is_displayed()


def test_3_4_order_3_meal_combo_meal_vegan_meal_sides(setup):
    hp_sign_in_page_button(setup).click()
    sip_enter_your_email(setup).send_keys(email_list[0])
    sip_enter_your_password(setup).send_keys(password_list[0])
    sip_sign_in_page_button(setup).click()
    mp_marking_combo_meal(setup).click()
    mp_marking_vegan(setup).click()
    scroll_down(setup)
    time.sleep(2)
    mp_marking_sides(setup).click()
    mp_reserve(setup).click()
    assert sum1_4_4_assert_price1(setup).text == '59'
    assert sum1_4_4_assert_price2(setup).text == '45'
    assert sum1_4_4_assert_price3(setup).text == '12'
    assert sum1_4_4_assert_subtotal(setup).text == 'Subtotal: 116$'
    assert sum1_4_4_assert_service(setup).text == 'Service: 11.6$'
    sum1_send_button(setup).click()
    assert sum2_4_4_assert_price(setup).text == 'Total: 127.6$'
    assert sum2_assert_tabel_no(setup).text == '1'
    sum2_assert_timer(setup).is_displayed()


def test_3_5_order_2_meal_vegan_kids_with_table_no_2(setup):
    hp_sign_in_page_button(setup).click()
    sip_enter_your_email(setup).send_keys(email_list[0])
    sip_enter_your_password(setup).send_keys(password_list[0])
    sip_sign_in_page_button(setup).click()
    mp_marking_vegan(setup).click()
    mp_marking_kids_meal(setup).click()
    scroll_down(setup)
    time.sleep(3)
    mp_reserve(setup).click()
    assert sum1_4_5_assert_price1(setup).text == '45'
    assert sum1_4_5_assert_price2(setup).text == '39'
    assert sum1_4_5_assert_subtotal(setup).text == 'Subtotal: 84$'
    assert sum1_4_5_assert_service(setup).text == 'Service: 8.4$'
    assert sum1_4_5_assert_total(setup).text == 'Total: 92.4$'
    sum1_table_no_box_2_mael(setup).clear()
    sum1_table_no_box_2_mael(setup).send_keys(2)
    time.sleep(2)
    setup.save_screenshot("/Users/evyatarhamami/PycharmProjects/pytest/save_screenshot/test_4_5.png")
    sum1_send_button(setup).click()
    assert sum2_4_5_assert_price(setup).text == '92.4'
    assert sum2_assert_tabel_no(setup).text == 'Table No 2'
    assert sum2_assert_timer(setup).is_displayed()


'''order eh test'''


def test_3_6_order_4_meal_combo_kids_burger_vegan(setup):
    hp_sign_in_page_button(setup).click()
    sip_enter_your_email(setup).send_keys(email_list[0])
    sip_enter_your_password(setup).send_keys(password_list[0])
    sip_sign_in_page_button(setup).click()
    mp_marking_combo_meal(setup).click()
    mp_marking_kids_meal(setup).click()
    mp_marking_burger(setup).click()
    mp_marking_vegan(setup).click()
    assert sum1_4_6_assert_marking_vegan(setup)


def test_3_7_enter_in_quantity_3(setup):
    hp_sign_in_page_button(setup).click()
    sip_enter_your_email(setup).send_keys(email_list[0])
    sip_enter_your_password(setup).send_keys(password_list[0])
    sip_sign_in_page_button(setup).click()
    mp_marking_kids_meal(setup).click()
    time.sleep(1)
    assert mp_sanity_assert_marking_kids_meal(setup)
    scroll_down(setup)
    time.sleep(1)
    mp_reserve(setup).click()
    time.sleep(1)
    assert sum1_sanity_assert_price(setup).text == '39'
    assert sum1_sanity_assert_subtotal(setup).text == 'Subtotal: 39$'
    assert sum1_sanity_assert_service(setup).text == 'Service: 3.9$'
    assert sum1_sanity_assert_total(setup).text == 'Total: 42.9$'
    sum1_3_7_quantity_up_button(setup).clear()
    sum1_3_7_quantity_up_button(setup).send_keys("3")
    sum1_send_button(setup).click()
    assert sum1_sanity_assert_service(setup).is_displayed()
