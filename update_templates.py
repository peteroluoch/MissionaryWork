import os

def update_template_extends(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and filepath.endswith('.html'):
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Replace {% extends 'base.html' %} with {% extends 'shared/base.html' %}
            if "{% extends 'base.html' %}" in content:
                content = content.replace("{% extends 'base.html' %}", "{% extends 'shared/base.html' %}")
                
                # Write the updated content back to the file
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"Updated {filepath}")
            
            # Replace {% include 'footer.html' %} with {% include 'shared/footer.html' %}
            if "{% include 'footer.html' %}" in content:
                content = content.replace("{% include 'footer.html' %}", "{% include 'shared/footer.html' %}")
                
                # Write the updated content back to the file
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"Updated footer in {filepath}")

# Update templates in the missionary_work directory
update_template_extends('templates/missionary_work')
