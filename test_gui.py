import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    # Initialize chrome driver
    options = Options()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options)

    # Maximize the window
    driver.maximize_window()

    yield driver

    # Close the browser
    driver.quit()


@allure.parent_suite("Minute Media")
@allure.suite("Tests for GUI features")
@allure.title("Assert 90min header menu")
@allure.description("Open 90min and assert the links visible")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Denis Krasilnikov")
def test_90min_menu(browser):
    browser.get("https://www.90min.com")

    allure.attach(
        browser.get_screenshot_as_png(), 
        name="Screenshot", 
        attachment_type=allure.attachment_type.PNG
    )

    # Define expected menu items
    expected_menu_items = [
        "Premier League",
        "Transfers",
        "Champions League",
        "FanVoice",
        "The Switch",
        "EFL",
        "La Liga",
        "Serie A",
        "More",
    ]

    # Find all header elements with class name "li_8cxs15"
    elements = browser.find_elements(By.CLASS_NAME, "li_8cxs15")

    # Extract text from each element and store in array
    actual_menu_items = [element.text for element in elements]

    # Loop over actual menu items and assert vs expected array
    failed_assertions = []

    for expected_item in expected_menu_items:
        try:
            with allure.step(f"Assert {expected_item}"):
                assert expected_item in actual_menu_items, \
                    f"Assert menu item: {expected_item}"
        except AssertionError as e:
            failed_assertions.append(expected_item)

    # Raise an exception if there are failed assertions
    if failed_assertions:
        raise AssertionError("Failed assertions:\n" 
                            + "\n".join(failed_assertions))
    

if __name__ == "__main__":
    pytest.main()
