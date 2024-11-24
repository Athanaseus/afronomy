import subprocess
from afronomy.apps.hello import hello

def test_hello_with_function():
    # Test the hello() function
    result = hello('Afronomy')
    assert result == "Hello Africalim"

def test_hello_prompt():
    # Test the prompt input
    result = subprocess.run(
        ['hello', 'hello'],
        input='Athanaseus\n',
        capture_output=True,
        text=True
    )
    assert result.stdout.strip().endswith("Hello Athanaseus")

#def test_hello_with_name():
#    # Test the `--name` option
#    result = subprocess.run(
#        ['hello', '--name', 'Afronomy'],
#        capture_output=True,
#        text=True
#    )
#    assert result.stdout.strip() == "Hello Afronomy"
