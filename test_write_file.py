import sys
sys.path.insert(0, ".")

from functions.write_file import write_file


def run_test(working_dir, file_path, content, description):
    """Run a single test case and print formatted results."""
    print(f'write_file("{working_dir}", "{file_path}", "{content[:30]}...")')
    result = write_file(working_dir, file_path, content)
    print(f"    {result}")
    print()


if __name__ == "__main__":
    # Test 1: Overwrite existing file
    run_test("calculator", "lorem.txt", "wait, this isn't lorem ipsum", "overwrite lorem.txt")
    
    # Test 2: Write to new file in subdirectory (creates parent dirs)
    run_test("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet", "new file in pkg subdir")
    
    # Test 3: Attempt to write outside working directory
    run_test("calculator", "/tmp/temp.txt", "this should not be allowed", "path escape attempt")
