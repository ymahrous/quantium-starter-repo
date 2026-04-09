import pytest
from dash import Dash
from dash.testing.application_runners import import_app

# import your Dash app from app.py
@pytest.fixture
def dash_app():
    app = import_app("app")
    return app

# Test 1: Check header
def test_header_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Soul Foods" in header.text

# Test 2: Check visualization
def test_graph_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

# Test 3: Check region picker
def test_region_picker_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    region_picker = dash_duo.find_element("#region-selector")
    assert region_picker is not None