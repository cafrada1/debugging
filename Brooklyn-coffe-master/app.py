from flask import Flask, render_template

PORT = 8080

app = Flask(__name__)

@app.route("/")
def home():
    platos = [
        {
            "nombre": "Bake Potato Pizza",
            "precio_entero": "20",
            "precio_centavos": "50",
            "imagen": "/images/gallery_9.jpeg",
            "descripcion": """
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                """,
        },
        {
            "nombre": "Salted Fried Chicken",
            "precio_entero": "19",
            "precio_centavos": "00",
            "imagen": "/images/gallery_8.jpeg",
            "descripcion": """
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quos nihil cupiditate ut vero alias quaerat inventore molestias vel suscipit explicabo.
                """,
        },
        {
            "nombre": "Italian Sauce Mushroom",
            "precio_entero": "17",
            "precio_centavos": "99",
            "imagen": "images/gallery_7.jpeg",
            "descripcion": """
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quos nihil cupiditate ut vero alias quaerat inventore molestias vel suscipit explicabo.
                """,
        },
        {
            "nombre": "Fried Potato w/ Garlic",
            "precio_entero": "22",
            "precio_centavos": "50",
            "imagen": "/images/gallery_6.jpeg",
            "descripcion": """
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quos nihil cupiditate ut vero alias quaerat inventore molestias vel suscipit explicabo.
                """,
        },
    ]
    return render_template('index.html', platos=platos)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

@app.route("/menu")
def menu():
    lista = {}
    return render_template('menu.html', lista=lista)

@app.route("/reservation")
def reservation():
    return render_template('reservation.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run("127.0.0.1", port=PORT, debug=True)