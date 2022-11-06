from flask import Flask


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def test():
    return 'This is My First CI-CD pipeline test'


if __name__ == "__main__":
    app.run(debug=True)