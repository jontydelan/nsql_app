from flask import Flask, render_template, request
from vanna_util.runmodel import get_vanna_rep
# from model.utils import Llama

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# two decorators, same function
@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('home.html', model_served=['Vanna','Meta Llama'])
    else:
        try:
            # OpenAI 3.5 turbo
            if request.form['model_select'] == 'Vanna':
                return_values = get_vanna_rep(request.form['searchText'])
                
            # Meta Code Llama
            if request.form['model_select'] == 'Meta Llama':
                return_values = "Not Implemented Due to load time on CPU"
        except:
            return_values = "Issue with API connection, try angain later"
        return render_template('home.html', Back_end_payload=return_values,)

if __name__ == '__main__':
    app.run(debug=True)
