def wait_for_seconds(page, seconds=2):
    page.wait_for_timeout(seconds * 1000)
