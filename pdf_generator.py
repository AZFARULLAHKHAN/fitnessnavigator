from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from io import BytesIO
import datetime

def generate_grocery_list(diet_plan, user_data):
    """Generate enhanced grocery list from diet plan with better categorization"""
    grocery_items = {
        '🥩 Proteins': {},
        '🥬 Vegetables': {},
        '🍎 Fruits': {},
        '🌾 Grains & Cereals': {},
        '🥛 Dairy & Alternatives': {},
        '🥜 Nuts & Seeds': {},
        '🧂 Condiments & Spices': {},
        '🥤 Beverages': {},
        '🍯 Others': {}
    }
    
    # Track ingredients to avoid duplicates
    ingredient_count = {}
    
    # Extract ingredients from diet plan
    for day, meals in diet_plan.items():
        for meal_type, meal_info in meals.items():
            if isinstance(meal_info, dict) and 'meal' in meal_info:
                meal_text = meal_info['meal'].lower()
                details = meal_info.get('details', '').lower()
                full_text = f"{meal_text} {details}"
            else:
                full_text = str(meal_info).lower()
            
            # Enhanced protein categorization
            if any(word in full_text for word in ['chicken', 'fish', 'egg', 'tofu', 'beef', 'turkey', 'salmon', 'tuna', 'shrimp', 'beans', 'lentils']):
                if 'chicken' in full_text: grocery_items['🥩 Proteins']['Chicken breast (boneless)'] = '1.2 kg'
                if any(word in full_text for word in ['fish', 'salmon']): grocery_items['🥩 Proteins']['Fresh fish fillets'] = '800g'
                if 'egg' in full_text: grocery_items['🥩 Proteins']['Fresh eggs (large)'] = '18 pieces'
                if 'tofu' in full_text: grocery_items['🥩 Proteins']['Firm tofu'] = '600g'
                if 'beef' in full_text: grocery_items['🥩 Proteins']['Lean ground beef'] = '700g'
                if 'turkey' in full_text: grocery_items['🥩 Proteins']['Turkey breast'] = '600g'
                if 'tuna' in full_text: grocery_items['🥩 Proteins']['Canned tuna (in water)'] = '4 cans'
                if 'shrimp' in full_text: grocery_items['🥩 Proteins']['Fresh shrimp'] = '500g'
                if any(word in full_text for word in ['beans', 'chickpea', 'lentil']): 
                    grocery_items['🥩 Proteins']['Mixed dried beans'] = '500g'
                    grocery_items['🥩 Proteins']['Red lentils'] = '400g'
            
            # Enhanced vegetable categorization
            vegetables_found = []
            if 'spinach' in full_text: vegetables_found.append('Fresh spinach')
            if 'broccoli' in full_text: vegetables_found.append('Fresh broccoli')
            if 'carrot' in full_text: vegetables_found.append('Carrots')
            if any(word in full_text for word in ['bell pepper', 'pepper']): vegetables_found.append('Bell peppers (mixed colors)')
            if 'tomato' in full_text: vegetables_found.append('Fresh tomatoes')
            if 'cucumber' in full_text: vegetables_found.append('Cucumbers')
            if 'onion' in full_text: vegetables_found.append('Yellow onions')
            if 'garlic' in full_text: vegetables_found.append('Fresh garlic')
            if 'lettuce' in full_text: vegetables_found.append('Mixed lettuce')
            if 'avocado' in full_text: vegetables_found.append('Ripe avocados')
            if 'sweet potato' in full_text: vegetables_found.append('Sweet potatoes')
            
            if vegetables_found:
                grocery_items['🥬 Vegetables']['Fresh spinach'] = '300g'
                grocery_items['🥬 Vegetables']['Broccoli crowns'] = '2 pieces'
                grocery_items['🥬 Vegetables']['Carrots'] = '1 kg'
                grocery_items['🥬 Vegetables']['Bell peppers (assorted)'] = '6 pieces'
                grocery_items['🥬 Vegetables']['Fresh tomatoes'] = '1.5 kg'
                grocery_items['🥬 Vegetables']['Cucumbers'] = '4 pieces'
                grocery_items['🥬 Vegetables']['Yellow onions'] = '1 kg'
                grocery_items['🥬 Vegetables']['Fresh garlic'] = '2 bulbs'
                grocery_items['🥬 Vegetables']['Mixed salad greens'] = '500g'
            
            # Enhanced fruit categorization
            if any(word in full_text for word in ['apple', 'banana', 'berries', 'orange', 'fruit', 'lemon']):
                grocery_items['🍎 Fruits']['Bananas'] = '2 bunches'
                grocery_items['🍎 Fruits']['Apples (mixed varieties)'] = '1.5 kg'
                grocery_items['🍎 Fruits']['Mixed berries (fresh/frozen)'] = '750g'
                grocery_items['🍎 Fruits']['Oranges'] = '8 pieces'
                grocery_items['🍎 Fruits']['Lemons'] = '4 pieces'
            
            # Enhanced grains categorization
            if any(word in full_text for word in ['rice', 'oats', 'bread', 'quinoa', 'pasta']):
                grocery_items['🌾 Grains & Cereals']['Brown rice'] = '1.5 kg'
                grocery_items['🌾 Grains & Cereals']['Steel-cut oats'] = '750g'
                grocery_items['🌾 Grains & Cereals']['Whole grain bread'] = '2 loaves'
                if 'quinoa' in full_text: grocery_items['🌾 Grains & Cereals']['Organic quinoa'] = '600g'
                if 'pasta' in full_text: grocery_items['🌾 Grains & Cereals']['Whole wheat pasta'] = '750g'
            
            # Enhanced dairy categorization
            if any(word in full_text for word in ['milk', 'yogurt', 'cheese']):
                grocery_items['🥛 Dairy & Alternatives']['Greek yogurt (plain)'] = '1.5 kg'
                grocery_items['🥛 Dairy & Alternatives']['Low-fat milk'] = '2 liters'
                if 'cheese' in full_text: grocery_items['🥛 Dairy & Alternatives']['Mozzarella cheese'] = '300g'
                if 'almond' in full_text: grocery_items['🥛 Dairy & Alternatives']['Almond milk'] = '1 liter'
            
            # Nuts and seeds
            if any(word in full_text for word in ['nuts', 'almond', 'walnut', 'seeds']):
                grocery_items['🥜 Nuts & Seeds']['Mixed nuts (unsalted)'] = '400g'
                grocery_items['🥜 Nuts & Seeds']['Chia seeds'] = '200g'
                grocery_items['🥜 Nuts & Seeds']['Pumpkin seeds'] = '150g'
            
            # Condiments and spices
            if any(word in full_text for word in ['oil', 'vinegar', 'spices', 'salt', 'pepper']):
                grocery_items['🧂 Condiments & Spices']['Extra virgin olive oil'] = '750ml'
                grocery_items['🧂 Condiments & Spices']['Balsamic vinegar'] = '250ml'
                grocery_items['🧂 Condiments & Spices']['Sea salt'] = '1 container'
                grocery_items['🧂 Condiments & Spices']['Black pepper (ground)'] = '1 container'
                grocery_items['🧂 Condiments & Spices']['Mixed herbs & spices'] = 'As needed'
            
            # Beverages
            if any(word in full_text for word in ['water', 'tea', 'coffee']):
                grocery_items['🥤 Beverages']['Filtered water'] = '6 liters'
                grocery_items['🥤 Beverages']['Green tea bags'] = '1 box'
            
            # Others
            if any(word in full_text for word in ['honey', 'maple']):
                grocery_items['🍯 Others']['Raw honey'] = '350g'
                if 'maple' in full_text: grocery_items['🍯 Others']['Pure maple syrup'] = '250ml'
    
    # Remove empty categories
    return {k: v for k, v in grocery_items.items() if v}


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
    story.append(Paragraph("🛒 Weekly Grocery List", title_style))
    story.append(Spacer(1, 20))
    
    # User info
    user_info = f"""
    <b>Diet Plan for:</b> {user_data['gender'].title()}, {user_data['age']} years<br/>
    <b>Food Preference:</b> {user_data['food_preference'].title()}<br/>
    <b>Generated on:</b> {datetime.datetime.now().strftime('%B %d, %Y')}<br/>
    <b>Valid for:</b> 7 days
    """
    story.append(Paragraph(user_info, styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Grocery categories
    for category, items in grocery_list.items():
        if items:  # Only show categories with items
            story.append(Paragraph(f"<b>{category}</b>", styles['Heading2']))
            
            # Create table for items
            data = [['Item', 'Quantity']]
            for item, quantity in items.items():
                data.append([item, quantity])
            
            table = Table(data, colWidths=[3*inch, 1.5*inch])
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
        "• Buy fresh vegetables and fruits for better nutrition",
        "• Choose lean cuts of meat and fish",
        "• Opt for whole grain products when possible",
        "• Check expiry dates, especially for dairy products",
        "• Consider buying in bulk for non-perishable items"
    ]
    
    for tip in tips:
        story.append(Paragraph(tip, styles['Normal']))
    
    doc.build(story)
    buffer.seek(0)
    return buffer