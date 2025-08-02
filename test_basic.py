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
    try:
        import playwright
        assert playwright is not None
        print(f"✅ Playwright imported successfully: {playwright.__version__}")
    except ImportError as e:
        pytest.fail(f"Failed to import playwright: {e}")

def test_import_pytest_bdd():
    """Test that pytest-bdd can be imported"""
    try:
        import pytest_bdd
        assert pytest_bdd is not None
        print(f"✅ pytest-bdd imported successfully: {pytest_bdd.__version__}")
    except ImportError as e:
        pytest.fail(f"Failed to import pytest-bdd: {e}")

@pytest.mark.smoke
def test_basic_smoke():
    """Basic smoke test"""
    assert 1 + 1 == 2

def test_ci_environment():
    """Test CI environment setup"""
    import os
    print(f"CI Environment: {os.environ.get('CI', 'False')}")
    print(f"HEADLESS: {os.environ.get('HEADLESS', 'False')}")
    assert True