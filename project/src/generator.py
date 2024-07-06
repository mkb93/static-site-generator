import os
import markdown

def extract_title(markdown_text):
  for line in markdown_text.split('\n'):
    if line.startswith('# '):
      return line[2:]
  raise Exception("No h1 header tag found")

def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")
  with open(from_path, 'r') as f:
    markdown_content = f.read()
  with open(template_path, 'r') as f:
    template_content = f.read()

  html_content = markdown.markdown(markdown_content)
  title = extract_title(markdown_content)
  html_page = template_content.replace('{{ Title }}', title)
  html_page = html_page.replace('{{ Content }}', html_content)
  os.makedirs(os.path.dirname(dest_path), exist_ok=True)
  with open(dest_path, 'w') as f:
    f.write(html_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  entries = os.listdir(dir_path_content)
  for entry in entries:
    full_path = os.path.join(dir_path_content, entry)
    relative_path = os.path.relpath(full_path, dir_path_content)
    dest_full_path = os.path.join(dest_dir_path,relative_path)
    if os.path.isfile(full_path) and entry.endswith('.md'):
      html_path = os.path.join(dest_dir_path, relative_path.replace('.md', '.html'))
      os.makedirs(os.path.dirname(html_path), exist_ok=True)
      generate_page(full_path, template_path, html_path)
    elif os.path.isdir(full_path):
      os.makedirs(dest_full_path, exist_ok=True)
      generate_pages_recursive(full_path, template_path, dest_full_path)