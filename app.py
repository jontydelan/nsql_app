from flask import Flask, render_template, request
from vanna_util.runmodel import get_vanna_rep

# from model.utils import Llama


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
model_served = ["Test", "Vanna", "Meta Llama"]


# two decorators, same function
@app.route("/", methods=["GET"])
def index():
    # if request.method=='GET':
    return render_template(template_name_or_list="home.html", model_served=model_served)


@app.route("/", methods=["POST"])
def index_search():
    try:
        # OpenAI 3.5 turbo
        if request.form["model_select"] == "Test":
            return_values = "Select * form THE_HEN_COMPANY"

        # OpenAI 3.5 turbo
        elif request.form["model_select"] == "Vanna":
            return_values = get_vanna_rep(request.form["searchText"])

        # Meta Code Llama
        elif request.form["model_select"] == "Meta Llama":
            return_values = "Not Implemented Due to load time on CPU"

        else:
            return_values = "No Selection made"

    except:
        return_values = "Issue with API connection, try angain later"
    return render_template(
        template_name_or_list="home.html",
        model_served=model_served,
        Back_end_payload=return_values,
    )


if __name__ == "__main__":
    app.run(debug=True)
