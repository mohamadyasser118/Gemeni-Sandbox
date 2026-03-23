#!/usr/bin/env python3
import sys
sys.path.insert(0, ".")

from functions.get_files_info import get_files_info


def run_test(working_dir, directory, description):
    """Run a single test case and print formatted results."""
    print(f'get_files_info("{working_dir}", "{directory}"):')
    result = get_files_info(working_dir, directory)
    
    if isinstance(result, str):
        # Error case
        print(f"    {result}")
    else:
        # Success case - result is a list of file dicts
        print(f"Result for {description}:")
        for file_info in sorted(result, key=lambda x: x['name']):
            print(f"  - {file_info['name']}: file_size={file_info['size']} bytes, is_dir=False")


if __name__ == "__main__":
    # Test 1: Current directory
    run_test("calculator", ".", "current directory")
    
    print()
    
    # Test 2: Subdirectory (pkg)
    run_test("calculator", "pkg", "'pkg' directory")
    
    print()
    
    # Test 3: Absolute path outside working directory
    run_test("calculator", "/bin", "'/bin' directory")
    
    print()
    
    # Test 4: Parent directory escape attempt
    run_test("calculator", "../", "'../' directory")