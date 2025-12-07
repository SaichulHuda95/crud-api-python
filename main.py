from flask import Flask
from routes.user_routes import user_bp

app = Flask(__name__)

@app.route("/")
def root():
    return {"message": "API is running"}

app.register_blueprint(user_bp, url_prefix="/user")

if __name__ == "__main__":
    app.run(debug=True)