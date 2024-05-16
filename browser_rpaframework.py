from RPA.Browser.Selenium import Selenium




def open_browser(url, download_dir=None, headless=False):
    """Abrir navegador"""
    browser = Selenium()
    options = sys.modules['selenium.webdriver'].ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-logging")
    options.add_argument("--intl.accept_languages\=pt-BR")
    browser.set_download_directory(download_dir)
    browser.open_available_browser(url, options=options, headless=headless)

    return browser
