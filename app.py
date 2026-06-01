"""Hamdrill Enterprises — Flask site (static content, Formspree contact)."""

import os

from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-change-me-in-production")

# Update in .env when you create a Formspree form
FORMSPREE_ACTION = os.getenv(
    "FORMSPREE_ACTION",
    "https://formspree.io/f/YOUR_FORM_ID",
)
WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER", "263242705863")
FORMSPREE_CONFIGURED = "YOUR_FORM_ID" not in FORMSPREE_ACTION


@app.context_processor
def inject_globals():
    return {
        "formspree_action": FORMSPREE_ACTION,
        "formspree_configured": FORMSPREE_CONFIGURED,
        "whatsapp_url": f"https://wa.me/{WHATSAPP_NUMBER}",
        "whatsapp_display": os.getenv("WHATSAPP_DISPLAY", "+263 (242) 705863"),
        "contact_email": os.getenv("CONTACT_EMAIL", "administration@hondehgroup.com"),
        "site_name": "Hamdrill Enterprises",
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/operations")
def operations():
    return render_template("operations.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/sustainability")
def sustainability():
    return render_template("sustainability.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    port = int(os.getenv("PORT", "5001"))
    app.run(debug=debug, host="0.0.0.0", port=port)
