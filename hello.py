from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3952)
print("hello wold")

# Example usage
text = "I am learning python programming."
if "python" in text:
    print("The word 'python' is in the string!")
else:
    print("The word 'python' is not in the string.")

    #hello world
    #hi
    