import sys
sys.path.insert(0, ".")
from functions.get_file_content import get_file_content
from config import MAX_CHARS

def test_lorem_truncation():
    print("Test: get_file_content('calculator', 'lorem.txt') (truncation)")
    content = get_file_content("calculator", "lorem.txt")
    print(f"  Length: {len(content)}")
    if f'truncated at {MAX_CHARS} characters' in content:
        print("  Truncation message found!")
    else:
        print("  Truncation message NOT found!")
    print()

def test_other_cases():
    cases = [
        ("main.py", "main.py"),
        ("pkg/calculator.py", "pkg/calculator.py"),
        ("/bin/cat", "/bin/cat (should error)"),
        ("pkg/does_not_exist.py", "pkg/does_not_exist.py (should error)")
    ]
    for file_path, desc in cases:
        print(f"Test: get_file_content('calculator', '{file_path}')")
        content = get_file_content("calculator", file_path)
        if isinstance(content, str) and content.startswith("Error:"):
            print(f"  {content}")
        else:
            print(f"  Length: {len(content)}")
            print(f"  First 100 chars: {content[:100]!r}")
        print()

if __name__ == "__main__":
    test_lorem_truncation()
    test_other_cases()
