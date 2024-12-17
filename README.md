  Reverse Video App
    Overview:
The Reverse Video App allows users to upload a video, which is then processed to create a reversed version of the video. The application utilizes a Flask backend with Python for video processing, and a responsive frontend built with HTML, CSS, and JavaScript.

Features
	Upload a video file for reversal.
	Process the video on the server side.
	Play the reversed video directly in the browser.
	Responsive design suitable for various devices.
	Technologies Used
Frontend:
	HTML
	CSS
	JavaScript
Backend:
	Flask (Python)
	Video Processing:
	OpenCV for video frame manipulation
	MoviePy for audio handling and video writing
Other Libraries:
	NumPy for numerical operations
Installation
Prerequisites
Python 3.x installed on your machine.
Required Python packages (listed in requirements.txt).
Ensure you have the necessary libraries for video processing.
Clone the Repository
	bash git clone https://github.com/vamsiKampani/Reverse-app.git cd reverse-video-app

Set Up the Backend
	Create a virtual environment (optional but recommended):

bash python -m venv venv source venv/bin/activate # On Windows use venv\Scripts\activate

Install the required Python packages:

bash pip install -r requirements.txt

Run the Application
Start the Flask server:

bash python app.py

Open your browser and navigate to http://localhost:5000 to access the app.

How It Works
File Upload:

Users can upload a video file through a web form. The file input is styled to enhance user experience.
Video Processing:

Upon submission, the video file is sent to the backend where it is temporarily saved.
The reverse_video function is invoked, which performs the following:
Extracts audio from the uploaded video (if present).
Reads and reverses the video frames using OpenCV.
Reverses the extracted audio using the scipy.io.wavfile library, if applicable.
Combines the reversed video and audio using MoviePy and saves the final output.

Result Display:
The reversed video is then sent back to the frontend, where it is displayed in a video player for the user to watch.
Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.
