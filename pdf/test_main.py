import re
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def clean_tts_text(input_file, output_file, max_chars=120, max_words=20):
    with open(input_file, 'r', encoding='utf-8') as infile:
        raw_lines = infile.readlines()
        
    cleaned_lines = []
    for line in raw_lines:
        line = line.strip()
        line = re.sub(r'\s+', ' ', line)
        
        if line:
            line  = line[0].upper() + line[1:]
            print(line)
        
        line = re.sub(r'\s+([?.!,])', r'\1', line) 
        
        if line and not re.search(r'[.?!]$', line):
            line += '.'  