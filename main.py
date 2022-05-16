from flask import Flask, render_template
#import yako3

app = Flask(__name__)

@app.route("/")
def home():
    return "pagina home teste 2"

@app.route("/yabu")
def contato():
    return render_template("lako.html",coisas_neox="yako3.neox_string",coisas_golden="yako3.golden_string")

if __name__ == "__main__":
    app.run()