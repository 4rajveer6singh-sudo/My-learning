from flask import Flask

# Initialize the Flask application
app = Flask(__name__)


# Define the home page route
@app.route("/")
def home():
  return "<h1>Hello! This web app is running live from my phone! 🚀</h1>"


# Run the server locally
if __name__ == "__main__":
  app.run(debug=True, port=5000)
