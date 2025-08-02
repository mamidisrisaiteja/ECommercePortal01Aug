"""
Sample test script to verify framework setup
"""
import sys
import os

# Add project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

def test_imports():
    """Test if all required imports work"""
    try:
        import pytest
        print("✓ pytest imported successfully")
        
        import yaml
        print("✓ yaml imported successfully")
        
        from playwright.sync_api import sync_playwright
        print("✓ playwright imported successfully")
        
        from pytest_bdd import scenarios, given, when, then
        print("✓ pytest-bdd imported successfully")
        
        # Test config loading
        config_path = os.path.join(project_root, 'config.yaml')
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        print("✓ config.yaml loaded successfully")
        print(f"  Base URL: {config.get('base_url')}")
        
        print("\n✅ All imports and configurations are working correctly!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_page_objects():
    """Test if page objects can be imported"""
    try:
        from pages.base_page import BasePage
        from pages.login_page import LoginPage
        from pages.products_page import ProductsPage
        from pages.cart_page import CartPage
        print("✓ All page objects imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Page object import error: {e}")
        return False

def test_project_structure():
    """Test if project structure is correct"""
    expected_dirs = ['pages', 'features', 'step_definitions', 'tests', 'utilities', 'TestData']
    expected_files = ['config.yaml', 'conftest.py', 'requirements.txt', 'README.md']
    
    missing_dirs = []
    missing_files = []
    
    for dir_name in expected_dirs:
        if not os.path.exists(os.path.join(project_root, dir_name)):
            missing_dirs.append(dir_name)
    
    for file_name in expected_files:
        if not os.path.exists(os.path.join(project_root, file_name)):
            missing_files.append(file_name)
    
    if missing_dirs:
        print(f"❌ Missing directories: {missing_dirs}")
    else:
        print("✓ All required directories present")
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
    else:
        print("✓ All required files present")
    
    return len(missing_dirs) == 0 and len(missing_files) == 0

if __name__ == "__main__":
    print("🚀 Testing Framework Setup...")
    print("=" * 50)
    
    structure_ok = test_project_structure()
    imports_ok = test_imports()
    page_objects_ok = test_page_objects()
    
    print("\n" + "=" * 50)
    if structure_ok and imports_ok and page_objects_ok:
        print("🎉 Framework setup is complete and ready to use!")
        print("\nNext steps:")
        print("1. Run tests: pytest")
        print("2. Run specific module: pytest -m auth")
        print("3. Generate HTML report: pytest --html=reports/report.html")
    else:
        print("⚠️ Framework setup has some issues. Please check the errors above.")
