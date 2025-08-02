"""
Basic test to verify framework setup
"""
import pytest

def test_basic_framework():
    """Basic test to verify pytest is working"""
    assert True, "Basic test should pass"

def test_import_pytest():
    """Test that pytest can be imported"""
    import pytest
    assert pytest is not None

def test_import_playwright():
    """Test that playwright can be imported"""
    import playwright
    assert playwright is not None

def test_import_pytest_bdd():
    """Test that pytest-bdd can be imported"""
    import pytest_bdd
    assert pytest_bdd is not None

@pytest.mark.smoke
def test_basic_smoke():
    """Basic smoke test"""
    assert 1 + 1 == 2