# clean_warnings.py
import re

def remove_stderr_divs(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove entire stderr output divs
    pattern = r'<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="application/vnd\.jupyter\.stderr"[^>]*>.*?</div>'
    
    cleaned_content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

remove_stderr_divs('notebook.html')
print("Removed stderr divs from notebook.html")