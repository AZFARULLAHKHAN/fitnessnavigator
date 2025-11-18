# FitnessNavigator

A comprehensive fitness tracking and planning application with AI-powered features.

## Features

- **Dashboard**: Track your fitness progress and goals
- **Workout Plans**: Personalized workout routines
- **Diet Planning**: Meal planning and nutrition tracking
- **Body Tracker**: Monitor body measurements and progress
- **AI Fitness Buddy**: Get personalized fitness advice
- **Meal Scanner**: Food recognition and calorie tracking
- **Social Challenges**: Compete with friends and community
- **Progress Tracking**: Detailed analytics and reports

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **AI Integration**: OpenAI API for fitness coaching
- **Food Recognition**: Computer vision for meal scanning

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## Project Structure

- `app.py` - Main Flask application
- `routes.py` - Application routes
- `templates/` - HTML templates
- `static/` - CSS, JavaScript, and images
- `food_recognition.py` - Food scanning functionality
- `pdf_generator.py` - Report generation
- `utils.py` - Utility functions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.