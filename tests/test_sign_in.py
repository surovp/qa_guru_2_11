from model.pages.github_page import given_open_page, \
    click_button_sign_in,\
    click_button_hamburger,\
    check_header_sign_in


def test_signin_desktop():
    given_open_page()
    click_button_sign_in()
    check_header_sign_in()


def test_signin_mobile(browser_config_mobile):
    given_open_page()
    click_button_hamburger()
    click_button_sign_in()
    check_header_sign_in()
