import uuid
import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "http://127.0.0.1:5000"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def test_listing_shows_role_salary_and_experience(page):
    page.goto(BASE_URL)
    card = page.locator('[data-job-id="qa-engineer"]')
    assert card.locator("h2").inner_text() == "QA Engineer"
    assert "4.5–4.8 LPA" in card.inner_text()
    assert "Fresher" in card.inner_text()

def test_job_link_opens_matching_role(page):
    page.goto(BASE_URL)
    page.get_by_role("link", name="View role").first.click()
    assert page.url.endswith("/jobs/qa-engineer")
    assert page.get_by_role("heading", name="QA Engineer").is_visible()

def test_empty_required_fields_are_blocked_by_browser(page):
    page.goto(f"{BASE_URL}/apply/qa-engineer")
    page.get_by_role("button", name="Submit application").click()
    assert page.locator("#name").evaluate("(el) => el.validity.valueMissing")

def test_invalid_email_is_blocked_by_browser(page):
    page.goto(f"{BASE_URL}/apply/qa-engineer")
    page.locator("#name").fill("Taylor Tester")
    page.locator("#email").fill("not-an-email")
    page.get_by_role("button", name="Submit application").click()
    assert page.locator("#email").evaluate("(el) => el.validity.typeMismatch")

def test_valid_application_shows_confirmation(page):
    email = f"qa-{uuid.uuid4().hex}@example.com"
    page.goto(f"{BASE_URL}/apply/qa-engineer")
    page.locator("#name").fill("Taylor Tester")
    page.locator("#email").fill(email)
    page.get_by_role("button", name="Submit application").click()
    assert page.get_by_role("status").inner_text().startswith("Thanks, Taylor Tester")

def test_duplicate_application_is_rejected(page):
    email = f"duplicate-{uuid.uuid4().hex}@example.com"
    for _ in range(2):
        page.goto(f"{BASE_URL}/apply/qa-engineer")
        page.locator("#name").fill("Jordan QA")
        page.locator("#email").fill(email)
        page.get_by_role("button", name="Submit application").click()
    assert page.get_by_role("alert").inner_text().startswith("An application already exists")\n