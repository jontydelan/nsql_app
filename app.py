from flask import Flask, render_template, request
app = Flask(__name__)

# two decorators, same function
@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('home.html')
    else:
        # app.logger.log(level=1,msg=request)
        return_values = "Value form Back end"+ request.form['searchText']
        # print(return_values)
        return render_template('home.html', Back_end_payload=return_values)

if __name__ == '__main__':
    app.run(debug=True)
