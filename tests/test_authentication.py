"""
Test runner for authentication module tests
"""
import pytest
from pytest_bdd import scenarios

# Import step definitions to register them
from step_definitions.test_authentication_steps import *

# Load scenarios from the feature file
scenarios('../features/authentication.feature')

class TestAuthentication:
    """Test class for authentication scenarios"""
    pass