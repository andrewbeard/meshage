"""
Pytest configuration and fixtures for the meshage tests.
"""

import os
import sys

import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from meshage.config import MQTTConfig


@pytest.fixture
def config():
    """Provide a test configuration instance."""
    return MQTTConfig()


@pytest.fixture
def sample_text():
    """Provide sample text for testing."""
    return "Hello, world!"


@pytest.fixture
def sample_long_text():
    """Provide sample long text for testing."""
    return "This is a longer message that might be used to test message handling with more content."


@pytest.fixture
def sample_unicode_text():
    """Provide sample unicode text for testing."""
    return "Hello 世界! 🚀"
