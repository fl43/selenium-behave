import time

@given('I go to the Salesforce login page')
def go_to_login_form(context):
    context.browser.get('https://trailhead-iaam-dev-ed.my.salesforce.com')

@then('the title should be "{text}"')
def verify_title(context, text):
    title = context.browser.title
    assert text == title

@when('I enter my credentials')
def enter_credentials(context):
    context.browser.find_element_by_id('username').send_keys('lazy.beaver@nttdata.com.iaam')
    context.browser.find_element_by_id('password').send_keys('fl3salesforce4')

@when('I click login')
def click_login(context):
    context.browser.find_element_by_id('Login').click()

@then('I should see the home page')
def see_home_page(context):
    # context.browser.implicitly_wait(20)
    time.sleep(10)
    title = context.browser.title
    assert "Home | Salesforce" == title
