import nltk
import re
from nltk.tokenize import word_tokenize

# Download punkt tokenizer (only first time)
nltk.download('punkt')
nltk.download('punkt_tab')


# tell nltk where to look for downloaded data
nltk.data.path.append(r"C:\nltk_data")
# Download punkt if not already downloaded
nltk.download('punkt', download_dir=r"C:\nltk_data")
nltk.download('punkt_tab', download_dir=r"C:\nltk_data")


# example text of a resume
resume_text = """
I am a B.Tech student with experience in Python, SQL, Machine Learning and Communication skills.
Worked on projects involving data analysis and web development using HTML, CSS, and JavaScript.
"""

#example keywords from job description 
keywords = ["python", "sql" ,"machine learning" ,"communication" ,"java" ,"teamwork" ]

# ----------- tokenization -----------------

# convert text to lowercase
resume_text_lower = resume_text.lower()

# tokenize
tokens = word_tokenize(resume_text_lower)
print(" tokens: ")
print(tokens)

# ----------- Highlight Keyword -------------

# highlight keywords found
highlighted = {}
for keyword in keywords :
  if keyword.lower() in resume_text_lower :
    highlighted[keyword] = resume_text_lower.count(keyword.lower())

print("✅ Keywords Found in Resume: ")
for k, v in highlighted.items():
  print(f"{k} -> {v} times")


# ---------- to show highlighted resume words -------------
highlighted_resume = resume_text
for keyword in keywords :
  highlighted_resume = re.sub(rf"(?i)\b{keyword}\b", keyword.upper(), highlighted_resume)

print("\nHighlighted Resume:\n")
print(highlighted_resume)  
