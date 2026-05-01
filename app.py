from flask import Flask, render_template, request, jsonify, send_file
from fpdf import FPDF
from dotenv import load_dotenv
from google import genai
import os
import json
import datetime
import sqlite3

load_dotenv()

app = Flask(__name__)

# ✅ Gemini client (NEW SDK)
<<<<<<< HEAD
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
=======
client = genai.Client(api_key=os.getenv(GEMINI_API_KEY"))
>>>>>>> 1314dd2c1c4821460c1f9af81342a5d06e938fb2


# ---------------- DATABASE ---------------- #

def init_db():
    conn = sqlite3.connect('soc.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS analyses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT,
                  log_input TEXT,
                  severity TEXT,
                  attack_type TEXT,
                  mitre_technique TEXT,
                  analysis TEXT)''')
    conn.commit()
    conn.close()


def save_analysis(log_input, severity, attack_type, mitre, analysis):
    conn = sqlite3.connect('soc.db')
    c = conn.cursor()
    c.execute('''INSERT INTO analyses 
                 (timestamp, log_input, severity, attack_type, mitre_technique, analysis)
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
               log_input[:500], severity, attack_type, mitre, analysis))
    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect('soc.db')
    c = conn.cursor()
    c.execute('SELECT * FROM analyses ORDER BY id DESC LIMIT 20')
    rows = c.fetchall()
    conn.close()
    return rows


# ---------------- AI ANALYSIS ---------------- #

def analyze_log_with_ai(log_text):
    system_prompt = """You are an expert SOC analyst.
Analyze the security log and respond ONLY in valid JSON format:

{
    "attack_detected": true or false,
    "attack_type": "name of attack",
    "severity": "Critical/High/Medium/Low/Info",
    "mitre_technique": "T#### - Name or N/A",
    "mitre_tactic": "Tactic name or N/A",
    "affected_system": "system from log",
    "summary": "2-3 sentence explanation",
    "indicators": ["indicator1", "indicator2"],
    "immediate_actions": ["action1", "action2", "action3"],
    "investigation_steps": ["step1", "step2", "step3"],
    "false_positive_chance": "High/Medium/Low",
    "confidence": "percentage"
}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=system_prompt + "\n\nAnalyze this log:\n\n" + log_text
        )

        response_text = response.text

        # Clean markdown if present
        if "```json" in response_text:
            response_text = response_text.split("```json")[1].split("```")[0]
        elif "```" in response_text:
            response_text = response_text.split("```")[1].split("```")[0]

        return json.loads(response_text.strip())

    except Exception as e:
        return {
            "attack_detected": False,
            "attack_type": "Error",
            "severity": "Info",
            "mitre_technique": "N/A",
            "mitre_tactic": "N/A",
            "affected_system": "Unknown",
            "summary": str(e),
            "indicators": [],
            "immediate_actions": ["Check API / logs"],
            "investigation_steps": ["Debug error"],
            "false_positive_chance": "Unknown",
            "confidence": "0%"
        }


# ---------------- ROUTES ---------------- #

@app.route('/')
def index():
    history = get_history()
    return render_template('index.html', history=history)


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    log_text = data.get('log', '')

    if not log_text.strip():
        return jsonify({'error': 'No log provided'})

    result = analyze_log_with_ai(log_text)

    save_analysis(
        log_text,
        result.get('severity', 'Unknown'),
        result.get('attack_type', 'Unknown'),
        result.get('mitre_technique', 'N/A'),
        result.get('summary', '')
    )

    return jsonify(result)


@app.route('/history')
def history():
    rows = get_history()
    history_list = []
    for row in rows:
        history_list.append({
            'id': row[0],
            'timestamp': row[1],
            'severity': row[3],
            'attack_type': row[4],
            'mitre': row[5]
        })
    return jsonify(history_list)


@app.route('/export_pdf', methods=['POST'])
def export_pdf():
    data = request.get_json()
    analysis = data.get('analysis', {})

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 15, 'AI SOC ANALYST REPORT', 0, 1, 'C')

    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 8, f"Generated: {datetime.datetime.now()}", 0, 1, 'C')

    pdf.ln(5)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f"Severity: {analysis.get('severity', 'N/A')}", 0, 1)

    pdf.multi_cell(0, 6, analysis.get('summary', 'N/A'))

    path = "/tmp/report.pdf"
    pdf.output(path)

    return send_file(path, as_attachment=True)


# ---------------- MAIN ---------------- #

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
