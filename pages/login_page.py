class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = "#username"
        self.password = "#password"
        self.login_btn = "#login"

    def navigate(self):
        self.page.goto("https://example.com/login")

    def login(self, user, pwd):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_btn)

    def is_dashboard_visible(self):
        return self.page.locator("#dashboard").is_visible()
