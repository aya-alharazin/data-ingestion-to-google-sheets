from flask import Flask, request
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# ---------- Google Sheets ----------
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=scopes
)

client = gspread.authorize(creds)
sheet = client.open_by_key("10LnRcF12BXFhBwBHx1rKiNAxIpJJRA_0ZsmjY4_oA44").sheet1


def parse_message(message):
    data = {}
    lines = message.strip().split("\n")

    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()

    return data


@app.route("/", methods=["GET"])
def form():
    return """
    <h3>الصقي الرسالة هنا</h3>
    <form method="POST" action="/submit">
        <textarea name="message" rows="12" cols="60"></textarea><br><br>
        <button type="submit">إرسال</button>
    </form>
    """


@app.route("/submit", methods=["POST"])
def submit():
    message = request.form.get("message")
    data = parse_message(message)

    row = [
        data.get("الاسم", ""),
        data.get("فرع الجامعة", ""),
        data.get("تخصصك", ""),
        data.get("رقم الشعبة", ""),
        data.get("المستوى", ""),
        "لا",
        data.get("رقم واتس (للتواصل)", ""),
        f"https://wa.me/{data.get('رقم واتس (للتواصل)', '')}",
        data.get("المواد الي حاب تشترك/ي فيها", "")
    ]

    sheet.append_row(row)
    return "✅ تم حفظ البيانات بنجاح"


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

