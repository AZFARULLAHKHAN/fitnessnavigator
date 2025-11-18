from flask import request, jsonify
from food_recognition import FoodRecognitionAPI
import base64
import logging
from app import app

@app.route('/analyze_food', methods=['POST'])
def analyze_food():
    """
    API endpoint to analyze food images using Google Vision + Gemini
    """
    try:
        # Get image data from request
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({'error': 'No image data provided'}), 400
        
        image_data = data['image']
        logging.info("Received food image for analysis")
        
        # Initialize food recognition API
        food_api = FoodRecognitionAPI()
        
        # Analyze the image
        result = food_api.analyze_food_image(image_data)
        
        logging.info(f"Food analysis result: {result}")
        
        return jsonify({
            'success': True,
            'foods': result['foods'],
            'nutrition': result['nutrition'],
            'source': result.get('source', 'AI Analysis')
        })
        
    except Exception as e:
        logging.error(f"Food analysis error: {str(e)}")
        return jsonify({
            'error': f'Analysis failed: {str(e)}',
            'success': False
        }), 500