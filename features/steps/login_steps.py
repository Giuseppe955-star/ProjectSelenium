from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

@given('I navigate to the OrangeHRM login page')
def step_impl(context):
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    context.driver = webdriver.Chrome(options=options)
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    sleep(3)

@when('I enter valid username and password')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
    context.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")

@when('I click the login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
    sleep(5)

@then('I should see the dashboard page')
def step_impl(context):
    dashboard_text = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").text
    assert "Admin" in dashboard_text
    context.driver.quit()