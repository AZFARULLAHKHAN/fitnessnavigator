from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from io import BytesIO
import datetime

def generate_grocery_list(diet_plan, user_data):
    """Generate comprehensive monthly grocery list based on personalized diet plan"""
    
    # Determine intensity level for quantities
    intensity = user_data.get('intensity', 'intermediate')
    food_preference = user_data.get('food_preference', 'non-veg')
    
    grocery_items = {
        '🥚 PROTEIN SOURCES': {
            'Eggs': '120 eggs (4 weeks avg – 3–4 per day)',
            'Toor dal': '2 kg',
            'Moong dal': '1.5 kg', 
            'Masoor dal': '1 kg',
            'Chole': '2 kg',
            'Rajma': '1.5 kg',
            'Sprouts (Moong + chana)': '1.5 kg (dry)'
        },
        '🌾 CARBS & GRAINS': {
            'Wheat / Atta': '10–12 kg (all levels)',
            'Oats': '2–4 kg',
            'Bread (brown/whole wheat)': '8–12 packets/month',
            'Poha': '2 kg',
            'Sooji': '1.5 kg',
            'Dalia': '2 kg',
            'Khichdi (rice + dal mix)': '3–4 kg (optional)'
        },
        '🥜 HEALTHY FATS & NUTS': {
            'Almonds': '1.5 kg',
            'Peanuts': '2 kg',
            'Roasted chana': '2 kg',
            'Cashews': '500 g',
            'Peanut Butter': '2–3 large jars',
            'Olive oil': '1 L',
            'Groundnut oil': '3–4 L',
            'Sunflower oil': '3–4 L'
        },
        '🍅 VEGETABLES (Monthly)': {
            'Spinach': '2–4 kg',
            'Methi': '2 kg',
            'Cabbage': '3–4 kg',
            'Potatoes': '6 kg',
            'Onions': '6–8 kg',
            'Tomatoes': '6–7 kg',
            'Carrots': '2–3 kg',
            'Beans': '2–3 kg',
            'Lauki / tinda': '3–4 kg',
            'Cauliflower': '2–3 heads',
            'Capsicum': '2.5–3 kg',
            'Cucumber': '3–4 kg',
            'Pumpkin': '1–2 kg',
            'Lemon': '50 pcs',
            'Ginger': '1 kg',
            'Green chillies': '500 g'
        },
        '🍉 FRUITS (Weekly Purchase)': {
            'Banana': '30–40 pcs',
            'Apple': '15–20 pcs',
            'Orange': '3–4 kg',
            'Pomegranate': '2–3 kg',
            'Pineapple': '2 pcs',
            'Avocado': 'optional 6–8 pcs',
            'Seasonal fruits': '3–4 kg/week'
        },
        '🥛 DAIRY': {
            'Milk': '30–40 L/month',
            'Curd': '10–15 kg/month',
            'Paneer': 'Listed in protein sources',
            'Buttermilk': '10–15 packets'
        },
        '🔥 SPICES & EXTRAS': {
            'Salt, black salt': 'As needed',
            'Turmeric': 'As needed',
            'Chilli powder': 'As needed',
            'Coriander powder': 'As needed',
            'Jeera': 'As needed',
            'Chia seeds': '1–2 kg',
            'Honey': '1 large bottle',
            'Coffee powder': '250–500 g',
            'Tea': '500 g',
            'Black pepper': 'As needed',
            'Oregano': 'optional',
            'Electrolyte powder': '2–3 packets'
        },
        '💧 HYDRATION': {
            'Water bottles': 'if needed',
            'Electrolytes': 'As needed',
            'Coconut water': 'optional'
        }
    }
    
    # Add non-vegetarian items if applicable
    if food_preference == 'non-veg':
        grocery_items['🥚 PROTEIN SOURCES'].update({
            'Chicken': f'{"4–5 kg total" if intensity == "intermediate" else "3–4 kg total" if intensity == "easy" else "5–6 kg total"}',
            'Fish': '1.5–3 kg (optional depending on weekly plan)',
            'Mutton': 'Optional'
        })
    
    # Add paneer for vegetarians or intermediate non-veg
    if food_preference == 'veg' or intensity == 'intermediate':
        grocery_items['🥚 PROTEIN SOURCES']['Paneer'] = f'{"2.5 kg/month" if intensity == "intermediate" else "2 kg/month" if intensity == "easy" else "3 kg/month"}'
    
    # Adjust rice quantity based on intensity
    rice_quantity = {
        'easy': '5–6 kg',
        'intermediate': '7–8 kg', 
        'hardcore': '8–10 kg'
    }
    grocery_items['🌾 CARBS & GRAINS']['Rice'] = rice_quantity.get(intensity, '7–8 kg')
    
    return grocery_items


def create_diet_pdf(user_data, diet_plan):
    """Create PDF for diet plan"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], 
                                fontSize=24, spaceAfter=30, textColor=colors.blue)
    story.append(Paragraph("🍽️ Personalized Diet Plan", title_style))
    story.append(Spacer(1, 20))
    
    # User info
    user_info = f"""
    <b>Name:</b> User<br/>
    <b>Age:</b> {user_data['age']} years<br/>
    <b>Gender:</b> {user_data['gender'].title()}<br/>
    <b>Height:</b> {user_data['height']} cm<br/>
    <b>Weight:</b> {user_data['weight']} kg<br/>
    <b>BMI:</b> {user_data['bmi']:.1f} ({user_data['bmi_category']})<br/>
    <b>Food Preference:</b> {user_data['food_preference'].title()}<br/>
    <b>Generated on:</b> {datetime.datetime.now().strftime('%B %d, %Y')}
    """
    story.append(Paragraph(user_info, styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Diet plan
    for day, meals in diet_plan.items():
        story.append(Paragraph(f"<b>{day}</b>", styles['Heading2']))
        
        for meal_type, meal_info in meals.items():
            if isinstance(meal_info, dict):
                meal_text = meal_info.get('meal', 'Not specified')
                details = meal_info.get('details', '')
                calories = meal_info.get('calories', '')
            else:
                meal_text = str(meal_info)
                details = ''
                calories = ''
            
            story.append(Paragraph(f"<b>{meal_type.title()}:</b> {meal_text}", styles['Normal']))
            if details:
                story.append(Paragraph(f"<i>{details}</i>", styles['Normal']))
            if calories:
                story.append(Paragraph(f"<i>{calories}</i>", styles['Normal']))
            story.append(Spacer(1, 10))
        
        story.append(Spacer(1, 15))
    
    doc.build(story)
    buffer.seek(0)
    return buffer

def create_workout_pdf(user_data, workout_plan):
    """Create PDF for workout plan"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], 
                                fontSize=24, spaceAfter=30, textColor=colors.red)
    story.append(Paragraph("💪 Personalized Workout Plan", title_style))
    story.append(Spacer(1, 20))
    
    # User info
    user_info = f"""
    <b>Name:</b> User<br/>
    <b>Age:</b> {user_data['age']} years<br/>
    <b>Gender:</b> {user_data['gender'].title()}<br/>
    <b>Intensity Level:</b> {user_data['intensity'].title()}<br/>
    <b>Generated on:</b> {datetime.datetime.now().strftime('%B %d, %Y')}
    """
    story.append(Paragraph(user_info, styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Workout plan
    for week, days in workout_plan.items():
        story.append(Paragraph(f"<b>{week}</b>", styles['Heading2']))
        
        for day, workout in days.items():
            story.append(Paragraph(f"<b>{day} - {workout['focus']}</b>", styles['Heading3']))
            
            if 'exercises' in workout:
                for exercise in workout['exercises']:
                    if isinstance(exercise, dict):
                        name = exercise.get('name', 'Exercise')
                        details = exercise.get('details', '')
                        story.append(Paragraph(f"• <b>{name}:</b> {details}", styles['Normal']))
                    else:
                        story.append(Paragraph(f"• {exercise}", styles['Normal']))
            
            if 'notes' in workout:
                story.append(Paragraph(f"<i>Notes: {workout['notes']}</i>", styles['Normal']))
            
            story.append(Spacer(1, 15))
    
    doc.build(story)
    buffer.seek(0)
    return buffer

def create_grocery_pdf(grocery_list, user_data):
    """Create PDF for grocery list"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], 
                                fontSize=24, spaceAfter=30, textColor=colors.green)
    story.append(Paragraph("🛒 Monthly Grocery List", title_style))
    story.append(Paragraph("Based on your personalized diet plan", styles['Normal']))
    story.append(Spacer(1, 20))
    
    # User info
    user_info = f"""
    <b>Diet Plan for:</b> {user_data['gender'].title()}, {user_data['age']} years<br/>
    <b>Food Preference:</b> {user_data['food_preference'].title()}<br/>
    <b>Generated on:</b> {datetime.datetime.now().strftime('%B %d, %Y')}<br/>
    <b>Valid for:</b> 1 month (4 weeks)
    """
    story.append(Paragraph(user_info, styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Grocery categories
    for category, items in grocery_list.items():
        if items:  # Only show categories with items
            story.append(Paragraph(f"<b>{category}</b>", styles['Heading2']))
            
            # Create table for items with checkbox
            data = [['Item', 'Quantity', '✓']]
            for item, quantity in items.items():
                data.append([item, quantity, '☐'])
            
            table = Table(data, colWidths=[2.5*inch, 1.5*inch, 0.5*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            
            story.append(table)
            story.append(Spacer(1, 20))
    
    # Shopping tips
    story.append(Paragraph("<b>Shopping Tips:</b>", styles['Heading2']))
    tips = [
        "• Buy fresh vegetables and fruits weekly for better nutrition",
        "• Purchase proteins in bulk and freeze portions",
        "• Choose whole grain products when possible",
        "• Check expiry dates, especially for dairy products",
        "• Buy dry goods (dals, rice, atta) in bulk to save money",
        "• Store spices in airtight containers to maintain freshness",
        "• Plan weekly vegetable shopping based on meal prep schedule"
    ]
    
    for tip in tips:
        story.append(Paragraph(tip, styles['Normal']))
    
    # Add note about quantities
    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>Note:</b> Quantities are estimated for 4 weeks based on your diet plan and intensity level. Adjust according to your household size and consumption patterns.", styles['Normal']))
    
    doc.build(story)
    buffer.seek(0)
    return buffer