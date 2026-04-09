import pytest
from dash import Dash, html
from dash.testing.composite import DashComposite
from selenium.webdriver.chrome.options import Options
from dash.testing.application_runners import ThreadedRunner

@pytest.fixture
def dash_app():
    app = Dash(__name__)
    app.layout = html.Div([
        html.H1("Hello Dash!"),
        html.Div(id="my-div")
    ])
    return app

@pytest.fixture
def dash_duo(request, dash_app):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    with DashComposite(
        server=ThreadedRunner(dash_app),
        browser="chrome",
        headless=True,
        options=options
    ) as dc:
        yield dc

# -----------------------------
# Tests
# -----------------------------
def test_header_present(dash_duo):
    dash_duo.wait_for_element("h1")
    header_text = dash_duo.find_element("h1").text
    assert header_text == "Hello Dash!"

def test_div_present(dash_duo):
    dash_duo.wait_for_element("#my-div")
    div = dash_duo.find_element("#my-div")
    assert div is not None