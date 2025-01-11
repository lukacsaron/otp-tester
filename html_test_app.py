# app.py

from quart import Quart, render_template, request, redirect, url_for
import logging

app = Quart(__name__, static_folder='static')

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("teletrade_parser.log")
    ]
)
logger = logging.getLogger('TestOTPApp')

# Route to display the OTP form
@app.route('/otp', methods=['GET'])
async def otp_form():
    return await render_template('otp_form.html')

# Route to handle OTP submission
@app.route('/submit_otp', methods=['POST'])
async def submit_otp():
    otp = (await request.form).get('otp')
    if not otp:
        logger.warning("OTP submission without OTP.")
        return await render_template('otp_response.html', error="OTP is required.", otp=None), 400
    logger.info(f"Received OTP: {otp}")
    # Here you can add logic to validate the OTP or process it as needed
    # For demonstration, we'll assume the OTP is always valid
    return await render_template('otp_response.html', otp=otp)

# Optional: Home route to redirect to /otp
@app.route('/', methods=['GET'])
async def home():
    return redirect(url_for('otp_form'))

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5001, debug=True)
    except Exception as e:
        logger.critical(f"Unhandled exception: {e}")
