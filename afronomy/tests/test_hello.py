import os
import tempfile
import subprocess
from afronomy.apps.hello import hello, write_greeting_to_file

def test_hello_with_function():
    # Test the hello() function
    result = hello('Afronomy')
    assert result == "Hello Afronomy"

def test_hello_prompt():
    # Test the prompt input
    result = subprocess.run(
        ['hello', 'Athanaseus'],
        capture_output=True,
        text=True
    )

def test_write_greeting_to_file():
    # Use a temporary file for testing
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name

    try:
        # Call the function to write the greeting to the temporary file
        name = "Afronomy"
        write_greeting_to_file(name, file_path=temp_path)

        # Read back the content and verify it
        with open(temp_path, 'r') as file:
            content = file.read()
            assert content == hello(name)  # Ensure the content matches the expected greeting
    finally:
        # Cleanup: Remove the temporary file
        os.remove(temp_path)
