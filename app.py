import os

# Define the path to the bulletins directory
bulletins_dir = './bulletins'
toc_file_path = './Table_Of_Contents.md'

# Start the table of contents content
toc_content = """# Security Bulletins

Below are notifications for security and privacy events within NVIDIA Open Source applications.

| Date       | Subject |
|------------|---------|
"""

for bulletin_file in sorted(os.listdir(bulletins_dir)):
    if bulletin_file.endswith('.md'):
        with open(os.path.join(bulletins_dir, bulletin_file), 'r') as file:
            lines = file.readlines()
            date = "N/A"
            subject = "N/A"
            for line in lines:
                if "**Updated" in line:
                    date = line.split('**')[1].strip()
                if line.startswith("# Security Bulletin:"):
                    subject = line[len("# Security Bulletin:"):].strip()
                    
            toc_content += f"| {date} | [{subject}]({os.path.join(bulletins_dir, bulletin_file)}) |\n"

with open(toc_file_path, 'w') as toc_file:
    toc_file.write(toc_content)
