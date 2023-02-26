import nltk, os
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from flask import Flask, render_template, request
from tempfile import mkdtemp
nltk.download('punkt')
nltk.download('stopwords')


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])
def index():
 if request.method == "POST":

  # Define the abstract text
  abstract = request.form.get("example")

  # Tokenize the abstract text into sentences and words
  sentences = sent_tokenize(abstract)
  words = word_tokenize(abstract)

  # Define stop words to remove from the text
  stop_words = set(stopwords.words('english'))

  # Define empty variables for cause, objective, and summary
  cause = ""
  objective = ""
  summary = ""

  # Loop through each sentence in the abstract
  for sentence in sentences:
    # Check if the sentence contains the word "method"
    if "cause" in sentence.lower():
      # Extract the sentence as the method section
      cause = sentence.strip()
    
    # Check if the sentence contains the word "objective"
    if "objective" in sentence.lower():
      # Extract the sentence as the objective section
      objective = sentence.strip()
    
    # Check if the sentence contains the word "summary"
    if "summary" in sentence.lower():
      # Extract the sentence as the summary section
      summary = sentence.strip()

  # Remove stop words from the method, objective, and summary sections
  cause_words = [word for word in word_tokenize(cause) if word.lower() not in stop_words]
  objective_words = [word for word in word_tokenize(objective) if word.lower() not in stop_words]
  summary_words = [word for word in word_tokenize(summary) if word.lower() not in stop_words]

  # Join the words back into sentences
  cause = " ".join(cause_words)
  objective = " ".join(objective_words)
  summary = " ".join(summary_words)

  list = {"cause": cause, "objective": objective, "summary": summary}
  
  return render_template("data.html", list=list)
  
 else:
    return render_template("bla.html")
