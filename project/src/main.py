import os
import shutil

from copystatic import copy_files_recursive
from generator import  generate_pages_recursive
def main():
    from_path = 'content'
    template_path = 'template.html'
    dest_path = 'public'

    os.makedirs(dest_path,exist_ok = True)
    generate_pages_recursive(from_path, template_path, dest_path)

    print("Page generation completed. You can now start your web server.")

if __name__ == "__main__":
    main()