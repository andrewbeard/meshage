# Tests for meshage

This directory contains comprehensive unit tests for the meshage library.

## Test Structure

### Unit Tests (unittest-based)
- `test_config.py` - Tests for the `MQTTConfig` class and configuration management
- `test_message.py` - Tests for the base `MeshtasticMessage` class and encryption (requires meshtastic)
- `test_textmessage.py` - Tests for the `MeshtasticTextMessage` class (requires meshtastic)
- `test_nodeinfomessage.py` - Tests for the `MeshtasticNodeInfoMessage` class (requires meshtastic)
- `test_integration.py` - Integration tests for complete workflows (requires meshtastic)

### Pytest Tests
- `test_pytest_style.py` - Pytest-style tests demonstrating alternative testing approach (requires meshtastic)
- `conftest.py` - Pytest configuration and fixtures

## Running Tests

### Quick Start (Recommended)
Run basic tests:
```bash
python3 run_tests_simple.py
```

### Using the test runner script
```bash
python3 run_tests.py
```

### Using unittest directly
```bash
# Set PYTHONPATH and run specific tests
PYTHONPATH=src python3 -m unittest tests.test_basic -v
PYTHONPATH=src python3 -m unittest tests.test_config -v

# Run all tests (may fail due to missing dependencies)
python3 -m unittest discover tests
```

### Using pytest
```bash
# Install pytest and dependencies
uv add --group dev pytest pytest-asyncio pytest-cov

# Run all tests (may fail due to missing dependencies)
uv run pytest tests/

# Run with coverage
uv run pytest --cov=src/meshage tests/

# Run specific test file
uv run pytest tests/test_config.py

# Run with verbose output
uv run pytest -v tests/
```

### Using uv to run tests
```bash
# Run tests using uv
uv run pytest tests/

# Run with coverage
uv run pytest --cov=src/meshage tests/
```

## Test Dependencies

### Required for all tests:
- Python 3.13+
- Standard library modules (unittest, os, sys, etc.)

### Required for full test suite:
- `meshtastic>=2.7.0` - Meshtastic protocol library (required)
- `cryptography>=45.0.5` - Encryption library (required)
- `pytest>=8.0.0` - Modern testing framework
- `pytest-asyncio>=0.24.0` - Async test support
- `pytest-cov>=5.0.0` - Coverage reporting

## Test Coverage

The tests cover:

1. **Configuration Management** ✅
   - Default configuration values
   - Environment variable loading
   - Configuration file loading
   - Property calculations (userid, topic, key, etc.)

2. **Message Classes** (requires meshtastic)
   - Text message creation and encoding
   - Node info message creation
   - Message ID generation and uniqueness
   - Packet creation and encryption
   - Service envelope creation

3. **Encryption** (requires meshtastic)
   - AES encryption with CTR mode
   - Nonce generation
   - Payload encryption and decryption

4. **Integration** (requires meshtastic)
   - Complete message workflows
   - Multiple message types
   - Configuration consistency
   - Error handling

5. **Edge Cases**
   - Empty strings
   - Unicode text
   - Special characters
   - Long messages
   - Invalid inputs

## Current Status

✅ **Working Tests:**
- Configuration tests (`test_config.py`)
- All tests run without external dependencies

✅ **All tests require meshtastic dependency:**
- Message encryption tests
- Text message tests
- Node info message tests
- Integration tests
- Pytest-style tests

## Adding New Tests

When adding new functionality to the library:

1. Create corresponding unit tests in the appropriate test file
2. Add integration tests if the feature involves multiple components
3. Include both positive and negative test cases
4. Test edge cases and error conditions
5. Update this README if adding new test categories

## Test Best Practices

- Use descriptive test method names
- Include docstrings explaining what each test does
- Test both success and failure scenarios
- Use fixtures for common setup
- Mock external dependencies
- Test edge cases and boundary conditions
- Ensure tests can run independently

## Troubleshooting

### Missing meshtastic dependency
If you see `ModuleNotFoundError: No module named 'meshtastic'`, install the dependency:
```bash
uv add meshtastic cryptography
```

### Import errors
Make sure to set the PYTHONPATH:
```bash
export PYTHONPATH=src
python3 -m unittest tests.test_basic
```

### Configuration issues
Tests are designed to work with the actual configuration loading mechanism. If you have environment variables or config files that override defaults, the tests will use those values. 