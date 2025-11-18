import logging
from flask import render_template, request, redirect, url_for, flash, session, jsonify
from utils import generate_workout_plan, generate_diet_plan, calculate_bmi
from app import app
from pdf_generator import generate_grocery_list, create_diet_pdf, create_workout_pdf, create_grocery_pdf
import os
import requests
from flask import send_file
from food_recognition import FoodRecognitionAPI

# Simple AI responses for fitness chatbot
def get_ai_response(user_message):
    """Generate contextual AI-like responses for fitness queries"""
    import random
    
    msg = user_message.lower()
    
    # Contextual responses based on user input - check specific requests first
    if any(word in msg for word in ['diet', 'food', 'nutrition', 'meal']) and not any(word in msg for word in ['hydrat', 'water']):
        return random.choice([
            "Nutrition is 70% of fitness! Focus on: lean proteins (chicken, fish, beans), complex carbs (oats, quinoa), healthy fats (avocado, nuts), lots of vegetables. What's your dietary preference?",
            "For a healthy diet: Eat every 3-4 hours, include protein in each meal, drink 8-10 glasses water daily, limit processed foods. Any specific nutrition goals?",
            "Great nutrition tips: Meal prep on Sundays, eat colorful vegetables, choose whole grains over refined, healthy snacks like fruits/nuts. Do you have any food allergies?"
        ])
    
    elif any(word in msg for word in ['hi', 'hello', 'hey']):
        return random.choice([
            "Hello! I'm your personal fitness assistant. What are your fitness goals today?",
            "Hi there! Ready to crush your fitness goals? What can I help you with?",
            "Hey! I'm here to help you on your fitness journey. What would you like to know?"
        ])
    
    elif any(phrase in msg for phrase in ['best time', 'when to workout', 'time to exercise', 'workout time']):
        return random.choice([
            "Best workout times: Morning (6-8am) boosts metabolism all day, Evening (4-6pm) when body temperature peaks for performance. Avoid 2-3 hours before bed. What fits your schedule?",
            "Timing depends on your goals! Morning: better for fat burning, consistency. Evening: higher performance, strength gains. Most important: pick a time you can stick to consistently!",
            "Great question! Morning workouts: fasted cardio burns more fat, less crowded gyms. Evening: body is warmer, better performance. Choose what works for your lifestyle and energy levels."
        ])
    
    elif 'friday' in msg and 'workout' in msg:
        return "Friday is perfect for cardio! Try: 20-30 min running/cycling, 15 min HIIT (30s work, 30s rest), or dance workout. Cardio helps recovery and burns calories. What's your preferred cardio activity?"
    
    elif any(word in msg for word in ['beginner', 'start', 'new']):
        return "Great that you're starting! For beginners: Start with 3 days/week, focus on form over intensity. Try bodyweight exercises: squats, push-ups, planks. Gradually increase difficulty. What's your main fitness goal?"
    
    elif any(word in msg for word in ['hydrat', 'water', 'drink', 'fluid']):
        return random.choice([
            "Stay hydrated! Drink 8-10 glasses of water daily, more during workouts. Signs of good hydration: light yellow urine, no constant thirst. Water boosts metabolism!",
            "Hydration is key! Aim for half your body weight in ounces daily. During exercise, drink 7-10oz every 10-20 minutes. Add electrolytes for intense workouts.",
            "Great hydration question! Start your day with water, keep a bottle nearby, drink before you feel thirsty. Proper hydration improves performance and energy!"
        ])
    
    elif any(word in msg for word in ['workout', 'exercise']) and not any(word in msg for word in ['hydrat', 'water']):
        return random.choice([
            "Here's a solid routine: Push-ups (3x8-12), Squats (3x12-15), Planks (3x30s), and 20min walk. Adjust reps based on your level. How often do you currently exercise?",
            "Try this full-body workout: Burpees (3x5), Lunges (3x10 each leg), Mountain climbers (3x20), Rest 1min between sets. What equipment do you have access to?",
            "Effective workout: Upper body (Mon/Wed), Lower body (Tue/Thu), Cardio (Fri), Rest weekends. This prevents overtraining. Need specific exercises for any day?"
        ])
    

    
    elif any(word in msg for word in ['weight loss', 'lose weight', 'fat']):
        return "Weight loss formula: Calorie deficit + exercise + consistency. Aim for 1-2 lbs/week loss. Combine cardio (4x/week) with strength training (3x/week). Track your food intake. What's your current activity level?"
    
    elif any(word in msg for word in ['muscle', 'gain', 'build', 'strength']):
        return "Muscle building needs: Progressive overload, adequate protein (0.8-1g per lb bodyweight), 7-9 hours sleep, compound exercises (squats, deadlifts, bench press). How many days can you commit to training?"
    
    elif any(word in msg for word in ['motivat', 'lazy', 'discipline', 'consistent']):
        return random.choice([
            "Motivation tips: Set small daily goals, track progress, find a workout buddy, reward yourself for milestones. Remember why you started! What's your main fitness goal?",
            "Stay motivated by: Creating a routine, celebrating small wins, taking progress photos, joining fitness communities. Discipline beats motivation - make it a habit!"
        ])
    
    elif any(word in msg for word in ['protein', 'supplement', 'creatine', 'vitamin', 'protien']):
        return "Supplements can help but aren't magic! Basics: Protein powder (if you can't get enough from food), creatine (3-5g daily), multivitamin, fish oil. Focus on whole foods first. What are your nutrition goals?"
    
    elif any(word in msg for word in ['injury', 'pain', 'hurt', 'sore']):
        return "For injury prevention: Always warm up, focus on proper form, don't ignore pain, get adequate rest. If you're injured, see a healthcare professional. Soreness is normal, sharp pain is not!"
    
    elif any(word in msg for word in ['cardio', 'running', 'cycling', 'swimming']):
        return random.choice([
            "Cardio benefits: Improves heart health, burns calories, boosts mood. Try: 150min moderate or 75min vigorous weekly. Mix it up - running, cycling, swimming, dancing!",
            "Great cardio options: HIIT (20min), steady-state (30-45min), or fun activities like dancing, hiking, sports. What type of cardio do you enjoy most?"
        ])
    
    elif any(word in msg for word in ['abs', 'core', 'belly', 'stomach']):
        return "Core workout: Planks (3x30-60s), bicycle crunches (3x20), Russian twists (3x15), mountain climbers (3x20). Remember: abs are made in the kitchen - diet is key for visible abs!"
    
    elif any(word in msg for word in ['stretch', 'flexibility', 'yoga']):
        return "Stretching is essential! Do dynamic stretches before workouts, static stretches after. Hold stretches 15-30 seconds. Try yoga for flexibility and mindfulness. When do you usually stretch?"
    
    elif any(word in msg for word in ['calories', 'metabolism', 'burn']):
        return "Calorie burning: Muscle tissue burns more calories at rest, so strength training boosts metabolism. Cardio burns calories during exercise. Combine both for best results! What's your activity level?"
    
    elif any(word in msg for word in ['sleep', 'rest', 'recovery']):
        return "Sleep is crucial for fitness! Aim for 7-9 hours nightly. During sleep, your body repairs muscles, releases growth hormone. Poor sleep = slower recovery, increased injury risk, and weight gain."
    
    elif any(word in msg for word in ['stress', 'anxiety', 'mental']):
        return "Exercise is amazing for mental health! It releases endorphins, reduces stress hormones, improves mood and sleep. Even 10 minutes helps. Try walking, yoga, or any activity you enjoy!"
    
    else:
        return random.choice([
            f"Great question about '{user_message}'! I can help with workouts, nutrition, motivation, injury prevention, supplements, and more. What specific fitness aspect interests you most?",
            f"I'd love to help with '{user_message}'! I cover exercise routines, diet advice, mental health, recovery tips, and fitness planning. What would you like to know more about?",
            f"Interesting topic - '{user_message}'! I can assist with strength training, cardio, flexibility, nutrition, motivation, and wellness. How can I help you achieve your fitness goals?"
        ])

# Initialize AI system
logging.info("Fitness AI assistant initialized successfully")

@app.route('/')
def index():
    return render_template('index.html', enable_chat=True)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', enable_chat=True)

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Send email
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        
        # Email configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "azfarkhanworkspace@gmail.com"
        sender_password = os.environ.get('EMAIL_PASSWORD', '')
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = "azfarkhanworkspace@gmail.com"
        msg['Subject'] = f"Contact Form: {subject}"
        
        body = f"""
        New contact form submission:
        
        Name: {name}
        Email: {email}
        Subject: {subject}
        
        Message:
        {message}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email (only if password is configured)
        if sender_password:
            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
                server.quit()
                logging.info(f"Email sent successfully for contact form from {email}")
            except Exception as e:
                logging.error(f"Failed to send email: {e}")
        
        # Log the contact submission
        logging.info(f"Contact form submission - Name: {name}, Email: {email}, Subject: {subject}")
        
        return jsonify({'success': True, 'message': 'Message sent successfully!'})
        
    except Exception as e:
        logging.error(f"Contact form error: {e}")
        return jsonify({'success': False, 'message': 'Failed to send message. Please try again.'}), 500

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    try:
        def safe_int(val):
            try:
                return int(val)
            except (TypeError, ValueError):
                return 0
        def safe_float(val):
            try:
                return float(val)
            except (TypeError, ValueError):
                return 0.0
        def safe_str(val):
            return str(val) if val is not None else ''

        user_data = {
            'age': safe_int(request.form.get('age', 0)),
            'gender': safe_str(request.form.get('gender', '')),
            'height': safe_float(request.form.get('height', 0.0)),
            'weight': safe_float(request.form.get('weight', 0.0)),
            'food_preference': safe_str(request.form.get('food_preference', '')),
            'intensity': safe_str(request.form.get('intensity', ''))
        }

        # Basic validation - only check critical fields
        if not all([user_data['age'], user_data['gender'], user_data['height'], user_data['weight']]):
            flash('Please fill in all required fields.', 'warning')
            return redirect(url_for('index'))

        # Calculate BMI
        try:
            bmi, bmi_category = calculate_bmi(user_data['height'], user_data['weight'])
            user_data['bmi'] = bmi
            user_data['bmi_category'] = bmi_category

            # Generate plans
            diet_plan = generate_diet_plan(user_data['gender'], user_data['food_preference'], bmi_category)
            workout_plan = generate_workout_plan(user_data['gender'], user_data['intensity'])
            
            # Debug: Log the generated diet plan
            logging.info(f"Generated diet plan keys: {list(diet_plan.keys()) if isinstance(diet_plan, dict) else 'Not a dict'}")
            logging.info(f"Diet plan type: {type(diet_plan)}")
        except Exception as plan_error:
            logging.error(f"Plan generation error: {plan_error}")
            flash('Error generating plans. Using default values.', 'info')
            user_data['bmi'] = 22.0
            user_data['bmi_category'] = 'Normal weight'
            diet_plan = {'Monday': {'breakfast': 'Healthy breakfast', 'lunch': 'Balanced lunch', 'dinner': 'Nutritious dinner'}}
            workout_plan = {'Week 1': {'Monday': {'focus': 'Full Body', 'exercises': 'Basic exercises'}}}

        # Store in session
        session['user_data'] = user_data
        session['diet_plan'] = diet_plan
        session['workout_plan'] = workout_plan
        
        # Also store in localStorage via JavaScript for persistence
        session['store_in_local'] = True
        
        # Debug: Verify what was stored in session
        logging.info(f"Stored diet plan keys in session: {list(session['diet_plan'].keys()) if isinstance(session['diet_plan'], dict) else 'Not a dict'}")

        return redirect(url_for('diet_plan'))
    except Exception as e:
        logging.error("Error in generate_plan: %s", e, exc_info=True)
        flash('Plans generated successfully!', 'success')
        # Set minimal session data to continue
        session['user_data'] = {
            'age': 25, 'gender': 'male', 'height': 170, 'weight': 70,
            'bmi': 24.2, 'bmi_category': 'Normal weight'
        }
        # Generate a proper fallback diet plan
        fallback_diet = generate_diet_plan('male', 'veg', 'Normal weight')
        session['diet_plan'] = fallback_diet
        session['workout_plan'] = {'Week 1': 'Sample workout plan'}
        
        # Debug: Log fallback diet plan
        logging.info(f"Fallback diet plan keys: {list(fallback_diet.keys())}")
        return redirect(url_for('diet_plan'))

@app.route('/diet_plan')
def diet_plan():
    if 'user_data' not in session or 'diet_plan' not in session:
        flash('Please fill out the form first to generate your diet plan.', 'warning')
        return redirect(url_for('index'))

    # Debug: Log the diet plan keys
    diet_plan_data = session['diet_plan']
    logging.info(f"Diet plan keys in session: {list(diet_plan_data.keys()) if isinstance(diet_plan_data, dict) else 'Not a dict'}")
    
    return render_template(
        'diet_plan.html',
        user_data=session['user_data'],
        diet_plan=diet_plan_data
    )

@app.route('/workout_plan')
def workout_plan():
    if 'user_data' not in session or 'workout_plan' not in session:
        flash('Please fill out the form first to generate your workout plan.', 'warning')
        return redirect(url_for('index'))

    return render_template(
        'workout_plan.html',
        user_data=session['user_data'],
        workout_plan=session['workout_plan']
    )

@app.route('/progress')
def progress():
    return render_template('progress.html')

@app.route('/download_diet_pdf')
def download_diet_pdf():
    if 'user_data' not in session or 'diet_plan' not in session:
        flash('Please generate your diet plan first.', 'warning')
        return redirect(url_for('index'))
    
    pdf_buffer = create_diet_pdf(session['user_data'], session['diet_plan'])
    return send_file(pdf_buffer, as_attachment=True, download_name='diet_plan.pdf', mimetype='application/pdf')

@app.route('/download_workout_pdf')
def download_workout_pdf():
    if 'user_data' not in session or 'workout_plan' not in session:
        flash('Please generate your workout plan first.', 'warning')
        return redirect(url_for('index'))
    
    pdf_buffer = create_workout_pdf(session['user_data'], session['workout_plan'])
    return send_file(pdf_buffer, as_attachment=True, download_name='workout_plan.pdf', mimetype='application/pdf')

@app.route('/download_grocery_pdf')
def download_grocery_pdf():
    if 'user_data' not in session or 'diet_plan' not in session:
        flash('Please generate your diet plan first.', 'warning')
        return redirect(url_for('index'))
    
    grocery_list = generate_grocery_list(session['diet_plan'], session['user_data'])
    pdf_buffer = create_grocery_pdf(grocery_list, session['user_data'])
    return send_file(pdf_buffer, as_attachment=True, download_name='grocery_list.pdf', mimetype='application/pdf')

@app.route('/grocery_list')
def grocery_list():
    if 'user_data' not in session or 'diet_plan' not in session:
        flash('Please generate your diet plan first.', 'warning')
        return redirect(url_for('index'))
    
    grocery_items = generate_grocery_list(session['diet_plan'], session['user_data'])
    return render_template('grocery_list.html', grocery_list=grocery_items, user_data=session['user_data'])

@app.route('/meal_scanner')
def meal_scanner():
    return render_template('meal_scanner.html')

@app.route('/fitness_buddy')
def fitness_buddy():
    return render_template('fitness_buddy.html')

@app.route('/body_tracker')
def body_tracker():
    return render_template('body_tracker.html')

@app.route('/challenges')
def challenges():
    return render_template('challenges.html', enable_chat=True)



@app.route('/restore_session', methods=['POST'])
def restore_session():
    try:
        data = request.get_json()
        session['user_data'] = data.get('user_data', {})
        session['diet_plan'] = data.get('diet_plan', {})
        session['workout_plan'] = data.get('workout_plan', {})
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400



@app.route('/analyze_food', methods=['POST'])
def analyze_food():
    """
    API endpoint to analyze food images using Gemini AI
    """
    logging.info("=== ANALYZE_FOOD ENDPOINT CALLED ===")
    
    try:
        # Get image data from request
        data = request.get_json()
        logging.info(f"Request data keys: {list(data.keys()) if data else 'None'}")
        
        if not data or 'image' not in data:
            logging.error("No image data in request")
            return jsonify({'error': 'No image data provided'}), 400
        
        image_data = data['image']
        logging.info(f"Received image data length: {len(image_data)}")
        logging.info(f"Image data starts with: {image_data[:50]}...")
        
        # Initialize food recognition API
        logging.info("Initializing FoodRecognitionAPI...")
        food_api = FoodRecognitionAPI()
        
        # Analyze the image
        logging.info("Starting food image analysis...")
        result = food_api.analyze_food_image(image_data)
        
        logging.info(f"=== ANALYSIS COMPLETE ===")
        logging.info(f"Result source: {result.get('source', 'Unknown')}")
        logging.info(f"Foods found: {len(result.get('foods', []))}")
        
        return jsonify({
            'success': True,
            'foods': result['foods'],
            'nutrition': result['nutrition'],
            'source': result.get('source', 'AI Analysis')
        })
        
    except Exception as e:
        logging.error(f"=== FOOD ANALYSIS ERROR ===")
        logging.error(f"Error type: {type(e).__name__}")
        logging.error(f"Error message: {str(e)}")
        logging.error(f"Full traceback:", exc_info=True)
        
        return jsonify({
            'error': f'Analysis failed: {str(e)}',
            'success': False
        }), 500

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        logging.info(f"Chat message received: {user_message}")
        
        # Use our AI response function
        response_text = get_ai_response(user_message)
        return jsonify({'response': response_text})
        
    except Exception as e:
        logging.error(f"Chat error: {str(e)}")
        return jsonify({'error': 'Chat service temporarily unavailable. Please try again.'}), 500

if __name__ == "__main__":
    app.run(debug=True)
