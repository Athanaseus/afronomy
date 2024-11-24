import subprocess

def test_hello_with_name():
    # Test the `--name` option
    result = subprocess.run(
        ['python', 'afronomy/afronomy/apps/hello.py', '--name', 'Afronomy'],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "Hello Afronomy"

def test_hello_prompt():
    # Test the prompt input
    result = subprocess.run(
        ['python', 'afronomy/afronomy/apps/hello.py'],
        input='Athanaseus\n',
        capture_output=True,
        text=True
    )
    assert result.stdout.strip().endswith("Hello Athanaseus")
