import os
import logging
import threading
import uuid
import torch
from flask import Flask, render_template, request, jsonify, url_for
from diffusers import StableDiffusionPipeline

# --------------------------
# Flask App Configuration
app = Flask(__name__)

# Set the upload folder for storing generated images
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Ensure that the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Configure logging for debugging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load the Stable Diffusion Model

# Determine if a GPU (CUDA) is available, otherwise use CPU
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the Stable Diffusion model with appropriate device setting
logging.info("Loading Stable Diffusion model. This may take a while...")
try:
    stable_diffusion = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5"
    ).to(device)
    logging.info("Stable Diffusion model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading Stable Diffusion model: {e}")
    raise RuntimeError("Failed to load Stable Diffusion. Check if all dependencies are installed.")

# Function for Image Generation

def generate_image(prompt: str, filename: str):
    """
    Generates an image using Stable Diffusion based on the given prompt.
    
    :param prompt: Text prompt for image generation
    :param filename: Name of the file where the image will be saved
    """
    try:
        logging.info(f"Generating image for prompt: {prompt}")
        
        # Generate the image
        image = stable_diffusion(prompt, num_inference_steps=27, height=512, width=512).images[0]
        
        # Save the generated image to the upload folder
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(filepath)

        logging.info(f"Image saved successfully at {filepath}")

    except Exception as e:
        logging.error(f"Error generating image: {e}")

# Flask Routes
@app.route('/')
def index():
    """
    Home route: Displays the index page.
    """
    return render_template('index.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    """
    Route for generating images. Accepts POST requests with a text prompt.
    Returns the URL of the generated image.
    """
    if request.method == 'POST':
        # Retrieve the prompt from the request form
        prompt = request.form.get('prompt')

        if not prompt:
            logging.warning("No prompt provided.")
            return jsonify(error="Prompt cannot be empty"), 400

        # Generate a unique filename for the image
        filename = f"{uuid.uuid4().hex}.png"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        logging.info(f"Request received. Generating image with filename: {filename}")

        # Run image generation in a separate thread to prevent blocking
        thread = threading.Thread(target=generate_image, args=(prompt, filename))
        thread.start()

        # Return the image URL immediately so frontend can poll for updates
        return jsonify(file_url=url_for('static', filename=f'uploads/{filename}'))

    return render_template('generate.html')

@app.route('/history')
def history():
    """
    Route to display previously generated images.
    """
    try:
        # List all images in the upload folder
        image_files = os.listdir(app.config['UPLOAD_FOLDER'])
        image_urls = [url_for('static', filename=f'uploads/{img}') for img in image_files]
        return render_template('history.html', image_urls=image_urls)
    except Exception as e:
        logging.error(f"Error loading image history: {e}")
        return "Error loading history", 500
@app.route('/result')
def result():
    return render_template('result.html')
# Run Flask App
if __name__ == '__main__':
    logging.info("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True)
