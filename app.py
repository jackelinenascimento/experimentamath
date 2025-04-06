from flask import Flask, render_template

app = Flask(__name__)

# Fragmento único sobre a Lei de Benford
fragments = [
    {
        "id": 1,
        "title": "Lei de Benford",
        "content": "Descubra por que o número 1 aparece mais do que o 9 em dados reais "
                   "e como isso pode ser usado para detectar fraudes."
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/fragments")
def list_fragments():
    return render_template("fragments.html", fragments=fragments)

@app.route("/fragment/<int:id>")
def fragment_detail(id):
    fragment = next((f for f in fragments if f["id"] == id), None)
    if not fragment:
        return "<h1>Fragmento não encontrado</h1>", 404
    return render_template("fragment_detail.html", fragment=fragment)

if __name__ == "__main__":
    app.run(debug=True)
