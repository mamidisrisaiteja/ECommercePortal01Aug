"""
Test runner for inventory module tests
"""
import pytest
from pytest_bdd import scenarios

# Load scenarios from feature file
scenarios('../features/inventory.feature')

# Import step definitions to register them
from step_definitions.test_inventory_steps import *
from step_definitions.test_authentication_steps import *

class TestInventory:
    """Test class for inventory scenarios"""
    pass