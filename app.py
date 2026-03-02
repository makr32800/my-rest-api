import json
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/v1/customer-segment', methods=['GET'])
def get_data():
    try:
        # This opens your text file and reads the content
        with open('data.txt', 'r') as file:
            content = file.read()
            # This converts the text string into a Python dictionary
            data = json.loads(content)
        
        # This sends it back to your browser as a clean JSON response
        return jsonify(data)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Use the port assigned by the cloud provider, or 5000 as a backup
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)