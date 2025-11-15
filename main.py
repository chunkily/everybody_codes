# Usage: uv run main.py <quest_number>
import sys
import shutil


if __name__ == "__main__":
    quest_num = sys.argv[1]
    # cp -r template quest{arg}
    shutil.copytree("template", f"quest{quest_num}")

    # Replace "questXX" in *.py files with "quest{arg}"
    for i in range(1, 4):
        file_path = f"quest{quest_num}/part{i}.py"
        with open(file_path, "r") as f:
            content = f.read()
        content = content.replace("questXX", f"quest{quest_num}")
        with open(file_path, "w") as f:
            f.write(content)
    print(f"Created quest{quest_num} directory with template files.")
