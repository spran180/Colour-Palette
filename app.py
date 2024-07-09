import openai
import json
from flask import Flask, render_template, request
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key=config["openai_api_key"]

app = Flask(__name__,
            template_folder='templates'
)

def get_colour(msg) :
  prompt=f""" 
   You are a colour palette generating assistant that generate the text prompts into colour palettes.
   Answer according to mood, theme and specific.
   colour pallete range is between 2 to 6 colours
   
   
   
   desired format: a JSON list of hexadecimal code.
   
   text: {msg}
   
   Answer:
   
   """
  response = openai.Completion.create(
    model="gpt-3.5-turbo-0125",
    prompt=prompt,
    max_tokens=100
    )
  colors = json.loads(response["choices"][0]["text"])
  return colors
   


@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    app.logger.info("Hit the post request")
    query = request.form.get("query")
    colors = get_colour(query)
    app.logger.info(colors)
    return {"colors": colors}


    #open ai request

    #return colour palette

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

