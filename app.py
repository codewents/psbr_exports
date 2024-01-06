from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        smtp_server = 'smtpout.secureserver.net'
        smtp_port = 465
        email_address = 'support@psbrexports.com'
        email_password = 'psbrexports@123'  
        to_address = request.json.get('to')
        subject = request.json.get('subject')
        message = request.json.get('message')

        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = to_address
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(email_address, email_password)
            server.sendmail(email_address, to_address, msg.as_string())

        return jsonify({'success': True}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
