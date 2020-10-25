from flask import Flask, render_template, request, session, redirect
from main import video_search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('web1html.html')


@app.route('/', methods=['POST'])
def my_form_response():
    test = video_search()
    response = request.form['Search']
    yotube_link = request.form['Copy link']
    time_stamp = test.algorithm(test.filtering_list(test.pass_json_for_getting_list()), response, test.load_model())
    upgraded_link="https://www.youtube.com/embed/"+yotube_link[32:]
    yotube_link = upgraded_link +'?start=' + str(int(time_stamp))
    print(yotube_link)
    return render_template('video_frame.html', yotube_link = yotube_link )


if __name__ == "__main__":
    app.run(debug = True)