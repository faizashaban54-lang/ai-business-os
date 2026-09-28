from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Business OS</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            color: #222;
        }

        .header {
            background: #111827;
            color: white;
            padding: 25px;
            text-align: center;
        }

        .container {
            max-width: 1000px;
            margin: 30px auto;
            padding: 20px;
        }

        .card {
            background: white;
            padding: 25px;
            margin-bottom: 20px;
            border-radius: 12px;
            box-shadow: 0 3px 12px rgba(0,0,0,0.08);
        }

        textarea {
            width: 100%;
            height: 120px;
            padding: 12px;
            box-sizing: border-box;
            border: 1px solid #ddd;
            border-radius: 8px;
            resize: vertical;
        }

        button {
            margin-top: 12px;
            padding: 12px 22px;
            background: #2563eb;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background: #1d4ed8;
        }

        .result {
            margin-top: 20px;
            background: #f1f5f9;
            padding: 15px;
            border-radius: 8px;
        }
    </style>
</head>

<body>

<div class="header">
    <h1>AI Business OS</h1>
    <p>Your AI-powered business assistant</p>
</div>

<div class="container">

    <div class="card">
        <h2>Business Assistant</h2>

        <form method="POST">
            <textarea
                name="message"
                placeholder="Write your business task here..."
                required
            ></textarea>

            <button type="submit">Run AI Assistant</button>
        </form>

        {% if result %}
        <div class="result">
            <h3>Result</h3>
            <p>{{ result }}</p>
        </div>
        {% endif %}
    </div>

    <div class="card">
        <h2>Business Tools</h2>
        <p>✓ Business Ideas</p>
        <p>✓ Marketing Assistant</p>
        <p>✓ Content Generator</p>
        <p>✓ Customer Support</p>
        <p>✓ Business Planning</p>
    </div>

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":
        message = request.form.get("message")

        result = (
            "Your request has been received. "
            "The AI engine will process this task."
        )

    return render_template_string(HTML, result=result)


if __name__ == "__main__":
    app.run(debug=True)
  
