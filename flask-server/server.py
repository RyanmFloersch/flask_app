from flask import Flask

# Creating app instance
app = Flask(__name__)

# Members API Route
@app.route("/members")
# Create
def members():
        # Returning a json of members array
        return {"members": ["Members1", "Members2","Members3","Members4"]}

# Condition to run app
if __name__ == "__main__":
        # debug=true for development
        app.run(debug=True)