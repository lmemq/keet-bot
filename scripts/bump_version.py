import re
import sys

def bump_version(version):
    major, minor, patch = map(int, version.split('.'))
    patch += 1
    return f"{major}.{minor}.{patch}"

def update_version_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    version_match = re.search(r'version\s*=\s*(\d+\.\d+\.\d+)', content)
    if version_match:
        current_version = version_match.group(1)
        new_version = bump_version(current_version)
        updated_content = content.replace(current_version, new_version)

        with open(file_path, 'w') as file:
            file.write(updated_content)
        print(f"Version updated from {current_version} to {new_version}")
    else:
        print("Version not found in the file.")
        sys.exit(1)

if __name__ == "__main__":
    update_version_in_file('../setup.cfg')
