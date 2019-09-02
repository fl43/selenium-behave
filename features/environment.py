import selenium.webdriver

def before_all(context):
  context.stopwatches = {}
  context.browser = None

def before_feature(context, feature):
    chrome_options = selenium.webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2 })
    browser = selenium.webdriver.Chrome(chrome_options = chrome_options)
    browser.maximize_window()
    browser.implicitly_wait(25)
    if context.browser is not None:
        context.browser.quit()
    context.browser = browser
    context.add_cleanup(browser.quit)

def after_feature(context, feature):
    context.browser.quit()
