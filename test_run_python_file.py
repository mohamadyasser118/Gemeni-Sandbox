import sys
sys.path.insert(0, "..")

from functions.run_python_file import run_python_file


def run_test(working_dir, file_path, args=None, description=""):
    """Run a single test case and print formatted results."""
    if args:
        print(f'run_python_file("{working_dir}", "{file_path}", {args})')
    else:
        print(f'run_python_file("{working_dir}", "{file_path}")')
    
    result = run_python_file(working_dir, file_path, args)
    print(f"Result:")
    print(result)
    print()


if __name__ == "__main__":
    # Test 1: Run main.py without args (print usage)
    run_test("calculator", "main.py", description="main.py usage")
    
    # Test 2: Run main.py with calculator expression
    run_test("calculator", "main.py", ["3 + 5"], description="calculator with expression")
    
    # Test 3: Run tests.py
    run_test("calculator", "tests.py", description="run tests")
    
    # Test 4: Attempt path traversal
    run_test("calculator", "../main.py", description="path escape attempt")
    
    # Test 5: Nonexistent file
    run_test("calculator", "nonexistent.py", description="nonexistent file")
    
    # Test 6: Non-Python file
    run_test("calculator", "lorem.txt", description="non-Python file")
