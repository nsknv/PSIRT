import os
from datetime import datetime

bulletins_dir = './bulletins'
toc_file_path = './Table_Of_Contents.md'

toc_content = """# Security Bulletins

Below are notifications for security and privacy events within NVIDIA Open Source applications.

| Date       | Type     | Subject |
|------------|----------|---------|
"""

for bulletin_file in sorted(os.listdir(bulletins_dir)):
    if bulletin_file.endswith('.md'):
        with open(os.path.join(bulletins_dir, bulletin_file), 'r') as file:
            lines = file.readlines()
            date = "N/A"
            type_ = "N/A"
            subject = "N/A"
            for line in lines:
                if line.startswith("**Updated"):
                    date = line.split('**')[1].strip()
                if line.startswith("# Security Bulletin:"):
                    subject = line[len("# Security Bulletin:"):].strip()
                if line.startswith("**Severity:"):
                    type_ = line.split('**')[1].strip()
                    
            toc_content += f"\n| {date} | {type_} | [{subject}]({os.path.join(bulletins_dir, bulletin_file)}) |"

with open(toc_file_path, 'w') as toc_file:
    toc_file.write(toc_content)
