import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file relative to the working directory and returns its output. Supports passing command-line arguments to the script.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional command-line arguments to pass to the Python script",
            ),
        },
        required=["file_path"],
    ),
)


def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # Build the command to run
        command = ["python", target_file]
        if args:
            command.extend(args)

        # Run the subprocess
        result = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30
        )

        # Build output string
        output_lines = []
        
        if result.returncode != 0:
            output_lines.append(f"Process exited with code {result.returncode}")
        
        if not result.stdout and not result.stderr:
            output_lines.append("No output produced")
        else:
            if result.stdout:
                output_lines.append(f"STDOUT: {result.stdout}")
            if result.stderr:
                output_lines.append(f"STDERR: {result.stderr}")
        
        return "\n".join(output_lines)

    except subprocess.TimeoutExpired:
        return "Error: Process execution timed out after 30 seconds"
    except Exception as e:
        return f"Error: executing Python file: {e}"
