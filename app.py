from flask import Flask, request, jsonify, send_file, send_from_directory
import os
from reverse_video import reverse_video  # Ensure this function is implemented correctly

app = Flask(__name__)

# Create directories for uploads and outputs if they don't exist
UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Serve the frontend HTML file
@app.route('/')
def index():
    """Serve the main frontend HTML file."""
    return send_from_directory('static', 'index.html')

@app.route('/process-video', methods=['POST'])
def process_video():
    """Handle video upload, processing, and returning the reversed video."""
    if 'video' not in request.files:
        return jsonify({"error": "No video file provided"}), 400
    
    video_file = request.files['video']
    
    # Define input and output paths
    input_path = os.path.join(UPLOAD_DIR, video_file.filename)
    output_path = os.path.join(OUTPUT_DIR, f"reversed_{video_file.filename}")

    # Save uploaded video to input path
    try:
        video_file.save(input_path)
    except Exception as e:
        return jsonify({"error": f"Failed to save video: {str(e)}"}), 500

    # Call the reverse_video model to process the file
    try:
        reverse_video(input_path, output_path)
    except Exception as e:
        return jsonify({"error": f"Processing error: {str(e)}"}), 500
    
    # Return the output file to the frontend
    try:
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": f"Failed to send file: {str(e)}"}), 500

if __name__ == "__main__":
    # Run the app on all available IPs and allow easy debugging
    app.run(host='0.0.0.0', port=5000, debug=False)
