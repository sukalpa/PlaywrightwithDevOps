from pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("admin", "password123")
    assert login.is_dashboard_visible()
