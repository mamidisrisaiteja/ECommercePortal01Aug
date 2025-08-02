"""
Test runner for cart module tests
"""
import pytest
from pytest_bdd import scenarios

# Load scenarios from feature file
scenarios('../features/cart.feature')

# Import step definitions to register them
from step_definitions.test_cart_steps import *
from step_definitions.test_authentication_steps import *

class TestCart:
    """Test class for cart scenarios"""
    pass