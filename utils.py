def calculate_bmi(height, weight):
    """
    Calculate BMI and return the category
    
    Args:
        height (float): Height in centimeters
        weight (float): Weight in kilograms
        
    Returns:
        tuple: (bmi_value, bmi_category)
    """
    # Convert height from cm to m
    height_m = height / 100
    
    # Calculate BMI
    bmi = weight / (height_m * height_m)
    bmi = round(bmi, 1)
    
    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category

def generate_diet_plan(gender, food_preference, bmi_category):
    """
    Generate a weekly diet plan based on gender, food preference, and BMI category
    
    Args:
        gender (str): 'male' or 'female'
        food_preference (str): 'veg' or 'non-veg'
        bmi_category (str): BMI category
        
    Returns:
        dict: Weekly diet plan
    """
    diet_plan = {}
    
    # Base calorie adjustment based on BMI category
    calorie_adjustment = 0
    if bmi_category == "Underweight":
        calorie_adjustment = 300  # Increase calories
    elif bmi_category == "Overweight" or bmi_category == "Obese":
        calorie_adjustment = -300  # Decrease calories
    
    # Base calorie needs (simplified)
    base_calories = 2000 if gender == "female" else 2500
    adjusted_calories = base_calories + calorie_adjustment
    
    # Generate plan for each day of the week
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    for day in days:
        if food_preference == "veg":
            diet_plan[day] = generate_veg_diet(day, gender, adjusted_calories, bmi_category)
        else:
            diet_plan[day] = generate_non_veg_diet(day, gender, adjusted_calories, bmi_category)
    
    return diet_plan

def generate_veg_diet(day, gender, calories, bmi_category):
    """Generate vegetarian diet for a specific day"""
    
    # Common vegetarian breakfast options
    breakfast_options = {
        "Monday": {
            "meal": "Oatmeal with fruits and nuts",
            "details": "1 cup oatmeal cooked with water, topped with 1 banana, 1 tbsp honey, and a handful of mixed nuts",
            "calories": "350-400 calories"
        },
        "Tuesday": {
            "meal": "Vegetable Omelet with Toast",
            "details": "2 egg omelet with spinach, tomatoes, and bell peppers, 1 slice of whole grain toast",
            "calories": "300-350 calories"
        },
        "Wednesday": {
            "meal": "Smoothie Bowl",
            "details": "Blend 1 frozen banana, 1/2 cup frozen berries, 1/2 cup Greek yogurt, and a splash of almond milk. Top with granola and chia seeds.",
            "calories": "350-400 calories"
        },
        "Thursday": {
            "meal": "Avocado Toast",
            "details": "2 slices of whole grain bread topped with mashed avocado, cherry tomatoes, and a sprinkle of salt and pepper",
            "calories": "300-350 calories"
        },
        "Friday": {
            "meal": "Vegetable Upma",
            "details": "1 cup semolina cooked with mixed vegetables (carrots, peas, beans) and spices",
            "calories": "300-350 calories"
        },
        "Saturday": {
            "meal": "Fruit Pancakes",
            "details": "2 whole grain pancakes topped with mixed berries and a drizzle of maple syrup",
            "calories": "400-450 calories"
        },
        "Sunday": {
            "meal": "Vegetable Poha",
            "details": "1 cup flattened rice cooked with peas, carrots, and mild spices",
            "calories": "300-350 calories"
        }
    }
    
    # Common vegetarian lunch options
    lunch_options = {
        "Monday": {
            "meal": "Chickpea Salad",
            "details": "2 cups mixed greens, 1/2 cup chickpeas, chopped vegetables, olive oil and lemon dressing",
            "calories": "400-450 calories"
        },
        "Tuesday": {
            "meal": "Vegetable Wrap",
            "details": "Whole grain wrap filled with hummus, mixed greens, cucumber, carrot, and bell peppers",
            "calories": "450-500 calories"
        },
        "Wednesday": {
            "meal": "Lentil Soup with Bread",
            "details": "1 cup lentil soup with vegetables, 1 slice whole grain bread",
            "calories": "400-450 calories"
        },
        "Thursday": {
            "meal": "Quinoa Bowl",
            "details": "1 cup cooked quinoa, roasted vegetables (broccoli, sweet potato, bell peppers), tahini dressing",
            "calories": "500-550 calories"
        },
        "Friday": {
            "meal": "Bean Burrito Bowl",
            "details": "Brown rice, black beans, corn, tomatoes, avocado, lime juice, and cilantro",
            "calories": "550-600 calories"
        },
        "Saturday": {
            "meal": "Pasta Primavera",
            "details": "1 cup whole grain pasta with sautéed seasonal vegetables and tomato sauce",
            "calories": "500-550 calories"
        },
        "Sunday": {
            "meal": "Vegetable Biryani",
            "details": "Brown rice cooked with mixed vegetables, spices, and garnished with fresh herbs",
            "calories": "500-550 calories"
        }
    }
    
    # Common vegetarian dinner options
    dinner_options = {
        "Monday": {
            "meal": "Vegetable Stir Fry with Tofu",
            "details": "Tofu cubes stir-fried with mixed vegetables (broccoli, carrots, bell peppers) in soy sauce, served over brown rice",
            "calories": "450-500 calories"
        },
        "Tuesday": {
            "meal": "Stuffed Bell Peppers",
            "details": "Bell peppers stuffed with quinoa, black beans, corn, and spices, baked with a touch of cheese on top",
            "calories": "400-450 calories"
        },
        "Wednesday": {
            "meal": "Vegetable Curry with Brown Rice",
            "details": "Mixed vegetable curry cooked in tomato gravy with Indian spices, served with 1/2 cup brown rice",
            "calories": "500-550 calories"
        },
        "Thursday": {
            "meal": "Buddha Bowl",
            "details": "Brown rice, roasted sweet potatoes, steamed broccoli, avocado slices, and tahini dressing",
            "calories": "500-550 calories"
        },
        "Friday": {
            "meal": "Zucchini Noodles with Pesto",
            "details": "Spiralized zucchini with homemade basil pesto, cherry tomatoes, and white beans",
            "calories": "400-450 calories"
        },
        "Saturday": {
            "meal": "Bean and Vegetable Soup",
            "details": "Hearty soup with mixed beans, vegetables, and herbs, served with a small whole grain roll",
            "calories": "450-500 calories"
        },
        "Sunday": {
            "meal": "Spinach and Mushroom Quesadilla",
            "details": "Whole grain tortilla filled with sautéed spinach, mushrooms, and a small amount of cheese",
            "calories": "400-450 calories"
        }
    }
    
    # Snack options
    snacks = {
        "Morning": {
            "meal": "Fruit and Nuts",
            "details": "1 apple or pear with a small handful of almonds",
            "calories": "150-200 calories"
        },
        "Evening": {
            "meal": "Yogurt Parfait",
            "details": "Greek yogurt topped with berries and a sprinkle of granola",
            "calories": "200-250 calories"
        }
    }
    
    # Return the diet plan for the day
    return {
        "breakfast": breakfast_options[day],
        "lunch": lunch_options[day],
        "dinner": dinner_options[day],
        "snacks": snacks
    }

def generate_non_veg_diet(day, gender, calories, bmi_category):
    """Generate non-vegetarian diet for a specific day"""
    
    # Common non-vegetarian breakfast options
    breakfast_options = {
        "Monday": {
            "meal": "Scrambled Eggs with Toast",
            "details": "2 scrambled eggs with spinach and tomatoes, 1 slice of whole grain toast",
            "calories": "350-400 calories"
        },
        "Tuesday": {
            "meal": "Greek Yogurt with Fruits and Granola",
            "details": "1 cup Greek yogurt, 1/2 cup mixed berries, 2 tbsp granola, and a drizzle of honey",
            "calories": "300-350 calories"
        },
        "Wednesday": {
            "meal": "Smoked Salmon Bagel",
            "details": "Whole grain bagel with cream cheese, smoked salmon, cucumber, and dill",
            "calories": "400-450 calories"
        },
        "Thursday": {
            "meal": "Protein Smoothie",
            "details": "Blend 1 scoop protein powder, 1 banana, 1 cup milk, and 1 tbsp peanut butter",
            "calories": "350-400 calories"
        },
        "Friday": {
            "meal": "Breakfast Burrito",
            "details": "Whole grain wrap filled with scrambled eggs, black beans, cheese, and salsa",
            "calories": "450-500 calories"
        },
        "Saturday": {
            "meal": "Chicken and Vegetable Omelette",
            "details": "3-egg omelette with diced chicken breast, bell peppers, and spinach",
            "calories": "400-450 calories"
        },
        "Sunday": {
            "meal": "Protein Pancakes",
            "details": "Protein-enriched pancakes topped with fresh berries and a dollop of Greek yogurt",
            "calories": "400-450 calories"
        }
    }
    
    # Common non-vegetarian lunch options
    lunch_options = {
        "Monday": {
            "meal": "Grilled Chicken Salad",
            "details": "Mixed greens, grilled chicken breast, cherry tomatoes, cucumber, red onion, balsamic vinaigrette",
            "calories": "450-500 calories"
        },
        "Tuesday": {
            "meal": "Tuna Sandwich",
            "details": "Whole grain bread, tuna mixed with light mayo, celery, and lettuce",
            "calories": "400-450 calories"
        },
        "Wednesday": {
            "meal": "Turkey and Avocado Wrap",
            "details": "Whole grain wrap with sliced turkey, avocado, lettuce, and mustard",
            "calories": "450-500 calories"
        },
        "Thursday": {
            "meal": "Chicken and Quinoa Bowl",
            "details": "Quinoa topped with grilled chicken, roasted vegetables, and a light tahini dressing",
            "calories": "500-550 calories"
        },
        "Friday": {
            "meal": "Salmon with Steamed Vegetables",
            "details": "Baked salmon fillet with steamed broccoli, carrots, and cauliflower",
            "calories": "450-500 calories"
        },
        "Saturday": {
            "meal": "Chicken Soup with Whole Grain Bread",
            "details": "Chicken soup with vegetables and a slice of whole grain bread on the side",
            "calories": "400-450 calories"
        },
        "Sunday": {
            "meal": "Lean Beef Stir Fry",
            "details": "Stir-fried lean beef strips with bell peppers, broccoli, and brown rice",
            "calories": "550-600 calories"
        }
    }
    
    # Common non-vegetarian dinner options
    dinner_options = {
        "Monday": {
            "meal": "Baked Fish with Roasted Vegetables",
            "details": "Baked white fish with lemon and herbs, served with roasted Brussels sprouts and carrots",
            "calories": "400-450 calories"
        },
        "Tuesday": {
            "meal": "Chicken Stir Fry",
            "details": "Chicken breast stir-fried with mixed vegetables (broccoli, snap peas, carrots) in a light sauce, served over brown rice",
            "calories": "500-550 calories"
        },
        "Wednesday": {
            "meal": "Grilled Salmon with Quinoa",
            "details": "Grilled salmon fillet with lemon and dill, served with quinoa and steamed asparagus",
            "calories": "500-550 calories"
        },
        "Thursday": {
            "meal": "Turkey Meatballs with Zucchini Noodles",
            "details": "Lean turkey meatballs in tomato sauce, served over spiralized zucchini",
            "calories": "450-500 calories"
        },
        "Friday": {
            "meal": "Shrimp and Vegetable Skewers",
            "details": "Grilled shrimp and vegetable skewers with a side of cauliflower rice",
            "calories": "400-450 calories"
        },
        "Saturday": {
            "meal": "Lean Beef and Vegetable Stew",
            "details": "Slow-cooked beef and vegetable stew with a small whole grain roll",
            "calories": "500-550 calories"
        },
        "Sunday": {
            "meal": "Roast Chicken with Sweet Potatoes",
            "details": "Roasted chicken breast with herbs, served with baked sweet potato and steamed green beans",
            "calories": "500-550 calories"
        }
    }
    
    # Snack options
    snacks = {
        "Morning": {
            "meal": "Protein Bar",
            "details": "One protein bar (look for options with at least 10g protein and under 200 calories)",
            "calories": "150-200 calories"
        },
        "Evening": {
            "meal": "Beef Jerky and Apple",
            "details": "1 oz beef jerky and a medium apple",
            "calories": "200-250 calories"
        }
    }
    
    # Return the diet plan for the day
    return {
        "breakfast": breakfast_options[day],
        "lunch": lunch_options[day],
        "dinner": dinner_options[day],
        "snacks": snacks
    }

def generate_workout_plan(gender, intensity):
    """
    Generate a monthly workout plan based on gender and intensity level
    
    Args:
        gender (str): 'male' or 'female'
        intensity (str): 'easy', 'intermediate', or 'hardcore'
        
    Returns:
        dict: Monthly workout plan
    """
    # Base workout plan structure with 4 weeks
    workout_plan = {
        "Week 1": {},
        "Week 2": {},
        "Week 3": {},
        "Week 4": {}
    }
    
    # Days of the week from Monday to Saturday
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    # For each week, generate exercises for each day
    for week in workout_plan:
        for day in days:
            workout_plan[week][day] = generate_daily_workout(day, gender, intensity, week)
    
    return workout_plan

def get_muscle_group_image(focus):
    """Get muscle group specific image URL"""
    image_map = {
        "Chest": "https://via.placeholder.com/1920x200/FF6B6B/ffffff?text=CHEST+WORKOUT",
        "Biceps": "https://via.placeholder.com/1920x200/4ECDC4/ffffff?text=BICEPS+WORKOUT",
        "Back": "https://via.placeholder.com/1920x200/45B7D1/ffffff?text=BACK+WORKOUT",
        "Triceps": "https://via.placeholder.com/1920x200/F7DC6F/000000?text=TRICEPS+WORKOUT",
        "Legs": "https://via.placeholder.com/1920x200/BB8FCE/ffffff?text=LEGS+WORKOUT",
        "Full Body": "https://via.placeholder.com/1920x200/58D68D/ffffff?text=FULL+BODY+WORKOUT",
        "Full Body Power": "https://via.placeholder.com/1920x200/58D68D/ffffff?text=FULL+BODY+POWER",
        "Cardio": "https://via.placeholder.com/1920x200/F1948A/ffffff?text=CARDIO+WORKOUT",
        "Active Recovery": "https://via.placeholder.com/1920x200/85C1E9/ffffff?text=ACTIVE+RECOVERY",
        "Rest and Recovery": "https://via.placeholder.com/1920x200/85C1E9/ffffff?text=REST+RECOVERY",
        "Back & Triceps": "https://via.placeholder.com/1920x200/45B7D1/ffffff?text=BACK+TRICEPS"
    }
    return image_map.get(focus, "https://via.placeholder.com/1920x200/007bff/ffffff?text=WORKOUT")

def get_exercise_video_url(name):
    video_map = {
        # Warm up
        "Warm up": "https://www.youtube.com/embed/xY9ZNWSziu8?si=lebIU5t4L9tEMk0J",
        "Light stretching": "https://www.youtube.com/embed/xY9ZNWSziu8?si=lebIU5t4L9tEMk0J",
        
        # Push variations
        "Push-ups": "https://www.youtube.com/embed/v9LABVJzv8A?si=-bdwjcujMV32QWka",
        "Push-ups (regular or modified)": "https://www.youtube.com/embed/v9LABVJzv8A?si=-bdwjcujMV32QWka",
        "Push-ups (modified)": "https://www.youtube.com/embed/v9LABVJzv8A?si=-bdwjcujMV32QWka",
        "Modified Push-ups": "https://www.youtube.com/embed/v9LABVJzv8A?si=-bdwjcujMV32QWka",
        
        # Chest exercises
        "Flat bench press": "https://www.youtube.com/embed/VmB1G1K7v94?si=l4Ye8bQKv4RL28xR",
        "Flat bench": "https://www.youtube.com/embed/VmB1G1K7v94?si=l4Ye8bQKv4RL28xR",
        "Incline dumbbell press": "https://www.youtube.com/embed/hChjZQhX1Ls?si=MUktTpjMSXnpZUUW",
        "Incline dumbbell flies": "https://www.youtube.com/embed/JSDpq14vCZ8?si=qIfmtEtKm0jkUkrF",
        "Incline dumbbell flyes": "https://www.youtube.com/embed/JSDpq14vCZ8?si=qIfmtEtKm0jkUkrF",
        "Cable flies": "https://www.youtube.com/embed/8Um35Es-ROE?si=BBHOVkTNGywEvWWg",
        "Cable flyes": "https://www.youtube.com/embed/8Um35Es-ROE?si=BBHOVkTNGywEvWWg",
        "Upper cable flies": "https://www.youtube.com/embed/eQ_NBB6OBH4?si=wjHkezklni6sROOf",
        "Upper cable flyes": "https://www.youtube.com/embed/eQ_NBB6OBH4?si=wjHkezklni6sROOf",
        "Butterfly chest dips": "https://www.youtube.com/embed/4la6BkUBLgo?si=dGAD2p-Dnlrf169p",
        "Chest dips": "https://www.youtube.com/embed/4la6BkUBLgo?si=dGAD2p-Dnlrf169p",
        "Incline bench press": "https://www.youtube.com/embed/8iPEnn-ltC8?si=AEWkpGjQTSVveCWg",
        "Incline bench": "https://www.youtube.com/embed/8iPEnn-ltC8?si=AEWkpGjQTSVveCWg",
        "Incline press": "https://www.youtube.com/embed/8iPEnn-ltC8?si=AEWkpGjQTSVveCWg",
        
        # Keep existing exercises
        "Diamond Push-ups": "https://www.youtube.com/embed/dYhQ05pUB0A?si=aRM1Idmspq3tauME",
        "Pike Push-ups": "https://www.youtube.com/embed/XckEEwa1BPI?si=d-Tny65kI-Pc5PeY",
        "Dips": "https://www.youtube.com/embed/rZl4D4p_nO4?si=EKkImmMjUla85XYD",
        "Wall Push-ups": "https://www.youtube.com/embed/EOf3cGIQpA4?si=0ymERtKh0TBii--y",
        "Clap Push-ups": "https://www.youtube.com/embed/EYwWCgM198U?si=SyXGdfTyN_REN8Fn",
        "Explosive Push-ups": "https://www.youtube.com/embed/_ICD84Bde4M?si=ZJp5KYNZGFbfQ4HP",
        
        # Back exercises
        "Bent over flies": "https://www.youtube.com/embed/GxVenNOYuo0?si=ZKHEZ8eIncQW36dp",
        "Bend over": "https://www.youtube.com/embed/GxVenNOYuo0?si=ZKHEZ8eIncQW36dp",
        "Butterfly dumbbell": "https://www.youtube.com/embed/YhIrOOsL4bA?si=BUmGzVrdpQHHcq0-",
        "Pull-ups": "https://www.youtube.com/embed/p40iUjf02j0?si=Aj1VY2_TNxbjbeiD",
        "Pull-ups/Assisted pull-ups": "https://www.youtube.com/embed/p40iUjf02j0?si=Aj1VY2_TNxbjbeiD",
        "Assisted pull-ups": "https://www.youtube.com/embed/p40iUjf02j0?si=Aj1VY2_TNxbjbeiD",
        "Lat pulldowns": "https://www.youtube.com/embed/WQasM7Jh9dQ?si=0WuND3d1SEosQto4",
        "Lats front": "https://www.youtube.com/embed/WQasM7Jh9dQ?si=0WuND3d1SEosQto4",
        
        # Bicep exercises
        "Bicep Curls": "https://www.youtube.com/embed/JyV7mUFSpXs?si=Kcl6c2mnwcejOpOf",
        "Bicep dumbbell": "https://www.youtube.com/embed/JyV7mUFSpXs?si=Kcl6c2mnwcejOpOf",
        "Bicep rod": "https://www.youtube.com/embed/kwG2ipFRgfo?si=6jEVVh2FAhupCAPJ",
        "Cable curls": "https://www.youtube.com/embed/UsaY33N4KEw?si=zXCLN_Gcyq5iInTr",
        "Cable curl": "https://www.youtube.com/embed/UsaY33N4KEw?si=zXCLN_Gcyq5iInTr",
        "Hammer Curls": "https://www.youtube.com/embed/BRVDS6HVR9Q?si=TW3WYtH3Fu2xYcjb",
        "Hammer curls": "https://www.youtube.com/embed/BRVDS6HVR9Q?si=TW3WYtH3Fu2xYcjb",
        "Hammer": "https://www.youtube.com/embed/BRVDS6HVR9Q?si=TW3WYtH3Fu2xYcjb",
        "Zig zag bar curls": "https://www.youtube.com/embed/6LrOTcr595A?si=sRLQgrVMjYTwmXC5",
        "Zig zag": "https://www.youtube.com/embed/6LrOTcr595A?si=sRLQgrVMjYTwmXC5",
        "Cable handle curls": "https://www.youtube.com/embed/NFzTWp2qpiE?si=Ju-KnjgwY7JWH0q0",
        "Cable handle": "https://www.youtube.com/embed/NFzTWp2qpiE?si=Ju-KnjgwY7JWH0q0",
        
        # Tricep exercises
        "Back triceps": "https://www.youtube.com/embed/ddOdLz3K5LU?si=2E-oFi6ayLhJuaV8",
        "Back tricep": "https://www.youtube.com/embed/ddOdLz3K5LU?si=2E-oFi6ayLhJuaV8",
        "Straight rod lying tricep extension": "https://www.youtube.com/embed/xFTF_wErf9o?si=glJyJuKDGa55o77Q",
        "Lying straight bar extension": "https://www.youtube.com/embed/xFTF_wErf9o?si=glJyJuKDGa55o77Q",
        "Single hand dumbbell tricep extension": "https://www.youtube.com/embed/ddOdLz3K5LU?si=2E-oFi6ayLhJuaV8",
        "Zig zag rod incline bench press": "https://www.youtube.com/embed/ddOdLz3K5LU?si=2E-oFi6ayLhJuaV8",
        "Cable reverse extension": "https://www.youtube.com/embed/ddOdLz3K5LU?si=2E-oFi6ayLhJuaV8",
        "Rope overhead extension": "https://www.youtube.com/embed/ddOdLz3K5LU?si=2E-oFi6ayLhJuaV8",
        "Back dips": "https://www.youtube.com/embed/ddOdLz3K5LU?si=2E-oFi6ayLhJuaV8",
        
        # Additional exercises
        "Flat dumbbell press": "https://www.youtube.com/embed/VmB1G1K7v94?si=l4Ye8bQKv4RL28xR",
        "Pec deck": "https://www.youtube.com/embed/4la6BkUBLgo?si=dGAD2p-Dnlrf169p",
        "Free weight squats": "https://www.youtube.com/embed/YaXPRqUwItQ?si=FIM0Mi-lNbfdrwsC",
        "Full squats": "https://www.youtube.com/embed/ec1a6PpEKrQ?si=hvYhLcGxOjtWu2Pc",
        "Leg press": "https://www.youtube.com/embed/yZmx_Ac3880?si=i6Si4uUtofLaEeZD",
        "Crunches": "https://www.youtube.com/embed/MKmrqcoCZ-M?si=Pba3VK7U8o27ATkl",
        "Frog jumps": "https://www.youtube.com/embed/SPxvbluj6vQ?si=8SiFKNiNIrAfKg8b",
        "Brisk walking": "https://www.youtube.com/embed/nmvVfgrExAg?si=ULj0SaHgCgfqSyzr",
        "Light walking": "https://www.youtube.com/embed/nmvVfgrExAg?si=ULj0SaHgCgfqSyzr",
        "Walking": "https://www.youtube.com/embed/nmvVfgrExAg?si=ULj0SaHgCgfqSyzr",
        "Reverse lats": "https://www.youtube.com/embed/SNiwpA13ZLU?si=Pi0hoXuDcpGKsRR9",
        "Mid back machine": "https://www.youtube.com/embed/RPxM76cp0Y8?si=q5gCKqFN636EbxQm",
        "Side dumbbell": "https://www.youtube.com/embed/XPPfnSEATJA?si=jcoRZznaDaniRTJ8",
        "Barbell rowing": "https://www.youtube.com/embed/T3N-TO4reLQ?si=VOuHuU5xz7X0hih5",
        "Front lat pulldown": "https://www.youtube.com/embed/SALxEARiMkw?si=WQB2jk7WD6esfmbi",
        "T-bar rows": "https://www.youtube.com/embed/hYo72r8Ivso?si=RdPMA6xvJNTqjKD6",
        "T bar": "https://www.youtube.com/embed/hYo72r8Ivso?si=RdPMA6xvJNTqjKD6",
        "Close grip pulldowns": "https://www.youtube.com/embed/IjoFCmLX7z0?si=3GD5W8BaNCwK0Wey",
        "Close grip lat pulldown": "https://www.youtube.com/embed/IjoFCmLX7z0?si=3GD5W8BaNCwK0Wey",
        "Side dumbbell rowing": "https://www.youtube.com/embed/5PoEksoJNaw?si=kx_eIVsEElQhuaZx",
        "Single dumbbell rowing": "https://www.youtube.com/embed/5PoEksoJNaw?si=kx_eIVsEElQhuaZx",
        "Weight squats": "https://www.youtube.com/embed/v_c67Omje48?si=dnTRJ4NZ6iBwSUsA",
        "Weighted lunges": "https://www.youtube.com/embed/Pbmj6xPo-Hw?si=-HV_Q98sRsKItQum",
        "Walking lunges": "https://www.youtube.com/embed/Pbmj6xPo-Hw?si=-HV_Q98sRsKItQum",
        "Hamstring leg press": "https://www.youtube.com/embed/tvS_kTb7nCE?si=aGHXj-FgG0lZ12qn",
        "Calf machine leg raises": "https://www.youtube.com/embed/KxEYX_cuesM?si=PRYi8eeskrY1YknM",
        "Reverse leg extension": "https://www.youtube.com/embed/oB3X0T0TG3E?si=_qYadzpvmjFFRT7E",
        "Reverse extension": "https://www.youtube.com/embed/oB3X0T0TG3E?si=_qYadzpvmjFFRT7E",
        "High intensity circuit": "https://www.youtube.com/watch?v=ml6cT4AZdqI",
        "HIIT cardio": "https://www.youtube.com/watch?v=ml6cT4AZdqI",
        "Cardio": "https://www.youtube.com/watch?v=ml6cT4AZdqI",

        # Squats, lunges, legs
        "Bodyweight Squats": "https://www.youtube.com/embed/eCnvnpG0TPs?si=zuGx4uNs2UXm0wzM",  # ScottHermanFitness
        "Walking Lunges": "https://www.youtube.com/embed/tQNktxPkSeE?si=m04Y8VreO5K4dxK0",  # ScottHermanFitness
        "Lunges": "https://www.youtube.com/embed/RwVXSUmiXAo?si=kOumIgcEeKh9ktCb",  # ScottHermanFitness
        "Glute Bridges": "https://www.youtube.com/embed/tqp5XQPpTxY?si=LfNmiS_c3u3TcAx2",  # ScottHermanFitness
        "Calf Raises": "https://www.youtube.com/embed/cPt_Op0uh5k?si=PSRGC9LC6OIVYaAl",  # ScottHermanFitness
        "Glute Kickbacks": "https://www.youtube.com/embed/D4gxkgZQkAg?si=EX7JYIQkksAH0ehB",  # ScottHermanFitness
        "Squat Jumps": "https://www.youtube.com/embed/2WDB_BKNkBg?si=yJZpwGf_LgHytXpI",  # ScottHermanFitness

        # Core
        "Planks": "https://www.youtube.com/embed/pvIjsG5Svck?si=O7KMftacLJaKgiWJ",  # Bowflex
        "Bicycle Crunches": "https://www.youtube.com/embed/TnWmPVYu1uw?si=89J0BHvFWiyfFJTW",  # Bowflex
        "Russian Twists": "https://www.youtube.com/embed/DJQGX2J4IVw?si=Uz-79Qcb46KyBfd6",  # Bowflex
        "Leg Raises": "https://www.youtube.com/embed/U4L_6JEv9Jg?si=ohd5vRklLivIOHJd",
        "Leg raises": "https://www.youtube.com/embed/U4L_6JEv9Jg?si=ohd5vRklLivIOHJd",

        # Back, arms, shoulders
        "Dumbbell Rows": "https://www.youtube.com/embed/jE43OmnBgLI?si=N9J77UB1bQqdobgy",  # ScottHermanFitness
        "Tricep Dips": "https://www.youtube.com/embed/7plJn7Ud-mg?si=NwBtiRyYTSteUBOi",  # ScottHermanFitness
        "Shoulder Press": "https://www.youtube.com/embed/0JfYxMRsUCQ?si=el1p1G1rXaH4Ebpf",  # ScottHermanFitness
        "Lateral Raises": "https://www.youtube.com/embed/mr2Ep0sSCIY?si=RKn0fZf33nmXtNxF",  # ScottHermanFitness
        "Bicep Curls": "https://www.youtube.com/embed/Nkl8WnH6tDU?si=Q5HXXGbxxsr8pW-v",  # ScottHermanFitness
        "Hammer Curls": "https://www.youtube.com/embed/BRVDS6HVR9Q?si=kRcaszwrNkgIa6nR",  # ScottHermanFitness
        "Superman Holds": "https://www.youtube.com/embed/z6PJMT2y8GQ?si=pV_ZSBTKbb2QxFWU",  # Redefining Strength

        # Cardio & HIIT
        "Brisk Walking": "https://www.youtube.com/embed/nmvVfgrExAg?si=ULj0SaHgCgfqSyzr",  # Walk at Home by Leslie Sansone
        "Brisk Walking or Light Jogging": "https://www.youtube.com/watch?v=Qn2D1K6r7yE",
        "Jogging or Cycling": "https://www.youtube.com/watch?v=Qn2D1K6r7yE",
        "Brisk Walking, Jogging, or Dancing": "https://www.youtube.com/watch?v=Qn2D1K6r7yE",
        "HIIT Circuit": "https://www.youtube.com/watch?v=ml6cT4AZdqI",  # MadFit
        "Circuit Training": "https://www.youtube.com/watch?v=U0bhE67HuDY",  # MadFit
        "Mountain Climbers": "https://www.youtube.com/watch?v=nmwgirgXLYM",  # Bowflex
        "Burpees": "https://www.youtube.com/watch?v=TU8QYVW0gDU",  # Bowflex
        "High knees": "https://www.youtube.com/watch?v=OAJ_J3EZkdY",  # Bowflex
        "Jumping jacks": "https://www.youtube.com/watch?v=c4DAnQ6DtF8",  # Bowflex

        # Mobility, stretching, yoga
        "Yoga": "https://www.youtube.com/watch?v=v7AYKMP6rOE",  # Yoga With Adriene
        "Yoga Flow": "https://www.youtube.com/watch?v=v7AYKMP6rOE",
        "Stretching": "https://www.youtube.com/watch?v=8JJ101D3knE",  # MadFit
        "Dynamic Stretching": "https://www.youtube.com/watch?v=8JJ101D3knE",
        "Light stretching": "https://www.youtube.com/watch?v=8JJ101D3knE",
        "Foam rolling": "https://www.youtube.com/watch?v=8caF1Keg2XU",  # Redefining Strength
        "Standing Side Leg Raises": "https://www.youtube.com/watch?v=2XZVxY5rG9M",  # ScottHermanFitness
        "Standing Side Bends": "https://www.youtube.com/watch?v=8JJ101D3knE",  # MadFit
        "Shoulder Rolls": "https://www.youtube.com/watch?v=8JJ101D3knE",  # MadFit
        "Cat-Cow Stretch": "https://www.youtube.com/watch?v=wBjj5F1yKp8",  # Yoga With Adriene
        "Hip Circles": "https://www.youtube.com/watch?v=8JJ101D3knE",  # MadFit
        "Arm Circles": "https://www.youtube.com/watch?v=8JJ101D3knE",  # MadFit
        "Dance": "https://www.youtube.com/watch?v=FHo9QaJ1DyI",  # The Fitness Marshall
    }
    default_url = "https://www.youtube.com/watch?v=dJlFmxiL11s"  # 20 min full body beginner workout (MadFit)
    return video_map.get(name, default_url)

def generate_daily_workout(day, gender, intensity, week):
    """Generate a daily workout based on day, gender, intensity, and week"""
    # Rest days
    if day == "Sunday":
        workout = {
            "focus": "Rest and Recovery",
            "exercises": [
                {"name": "Light stretching", "details": "Full body, 15-20 minutes"},
                {"name": "Foam rolling", "details": "Focus on tight areas, 10 minutes"},
                {"name": "Walking", "details": "Leisurely pace, 20-30 minutes (optional)"}
            ],
            "notes": "Allow your body to recover. Stay hydrated and get adequate sleep."
        }
    else:
        # Beginner intensity workouts
        if intensity == "easy":
            workout_plans = {
                "male": {
                    "Monday": {
                        "focus": "Chest",
                        "exercises": [
                            {"name": "Push-ups", "details": "2-3 sets of 8-10 reps"},
                            {"name": "Flat bench press", "details": "2-3 sets of 8-10 reps"},
                            {"name": "Flat dumbbell press", "details": "2-3 sets of 8-10 reps"},
                            {"name": "Incline dumbbell flies", "details": "2-3 sets of 8-10 reps"}
                        ],
                        "notes": "Focus on proper form. Start with warm-up and stretching."
                    },
                    "Tuesday": {
                        "focus": "Back & Triceps",
                        "exercises": [
                            {"name": "Pull-ups", "details": "2-3 sets of 5-8 reps"},
                            {"name": "Lat pulldowns", "details": "2-3 sets of 8-10 reps"},
                            {"name": "Cable rowing", "details": "2-3 sets of 8-10 reps"},
                            {"name": "Straight rod lying tricep extension", "details": "2-3 sets of 8-10 reps"}
                        ],
                        "notes": "Focus on controlled movements and proper form."
                    },
                    "Wednesday": {
                        "focus": "Legs",
                        "exercises": [
                            {"name": "Free weight squats", "details": "2-3 sets of 8-10 reps"},
                            {"name": "Leg press", "details": "2-3 sets of 10-12 reps"},
                            {"name": "Leg raises", "details": "2-3 sets of 10-12 reps"},
                            {"name": "Crunches", "details": "2-3 sets of 10-15 reps"}
                        ],
                        "notes": "Start with bodyweight movements before adding weights."
                    },
                    "Thursday": {
                        "focus": "Active Recovery",
                        "exercises": [
                            {"name": "Light stretching", "details": "15-20 minutes"},
                            {"name": "Walking", "details": "20-30 minutes"}
                        ],
                        "notes": "Focus on recovery and flexibility."
                    },
                    "Friday": {
                        "focus": "Full Body",
                        "exercises": [
                            {"name": "Push-ups", "details": "2 sets of 8-10 reps"},
                            {"name": "Bodyweight squats", "details": "2 sets of 10-12 reps"},
                            {"name": "Planks", "details": "2 sets of 20-30 seconds"},
                            {"name": "Frog jumps", "details": "2 sets of 5-8 reps"}
                        ],
                        "notes": "Light full body workout to end the week."
                    },
                    "Saturday": {
                        "focus": "Cardio",
                        "exercises": [
                            {"name": "Brisk walking", "details": "20-30 minutes"},
                            {"name": "Light stretching", "details": "10 minutes"}
                        ],
                        "notes": "Low intensity cardio and recovery."
                    }
                },
                "female": {
                    "Monday": {
                        "focus": "Chest",
                        "exercises": [
                            {"name": "Push-ups (modified)", "details": "2-3 sets of 8-10 reps"},
                            {"name": "Flat dumbbell press", "details": "2-3 sets of 8-10 reps"},
                            {"name": "Incline dumbbell flies", "details": "2-3 sets of 8-10 reps"},
                            {"name": "Pec deck", "details": "2-3 sets of 8-10 reps"}
                        ],
                        "notes": "Start with warm-up and focus on form over weight."
                    },
                    "Tuesday": {
                        "focus": "Back & Triceps",
                        "exercises": [
                            {"name": "Assisted pull-ups", "details": "2-3 sets of 5-8 reps"},
                            {"name": "Lat pulldowns", "details": "2-3 sets of 8-10 reps"},
                            {"name": "Cable rowing", "details": "2-3 sets of 8-10 reps"},
                            {"name": "Single hand dumbbell tricep extension", "details": "2-3 sets of 8-10 reps"}
                        ],
                        "notes": "Use lighter weights and focus on muscle activation."
                    },
                    "Wednesday": {
                        "focus": "Legs",
                        "exercises": [
                            {"name": "Bodyweight squats", "details": "2-3 sets of 10-12 reps"},
                            {"name": "Leg press", "details": "2-3 sets of 10-12 reps"},
                            {"name": "Leg raises", "details": "2-3 sets of 10-12 reps"},
                            {"name": "Crunches", "details": "2-3 sets of 10-15 reps"}
                        ],
                        "notes": "Focus on proper squat form and core engagement."
                    },
                    "Thursday": {
                        "focus": "Active Recovery",
                        "exercises": [
                            {"name": "Yoga", "details": "15-20 minutes"},
                            {"name": "Light walking", "details": "20 minutes"}
                        ],
                        "notes": "Focus on flexibility and recovery."
                    },
                    "Friday": {
                        "focus": "Full Body",
                        "exercises": [
                            {"name": "Modified push-ups", "details": "2 sets of 8-10 reps"},
                            {"name": "Bodyweight squats", "details": "2 sets of 10-12 reps"},
                            {"name": "Planks", "details": "2 sets of 20-30 seconds"},
                            {"name": "Glute bridges", "details": "2 sets of 10-12 reps"}
                        ],
                        "notes": "Light full body workout focusing on form."
                    },
                    "Saturday": {
                        "focus": "Cardio",
                        "exercises": [
                            {"name": "Brisk walking", "details": "20-30 minutes"},
                            {"name": "Stretching", "details": "10-15 minutes"}
                        ],
                        "notes": "Low intensity cardio and flexibility work."
                    }
                }
            }
        # Intermediate intensity workouts
        elif intensity == "intermediate":
            workout_plans = {
                "male": {
                    "Monday": {
                        "focus": "Chest",
                        "exercises": [
                            {"name": "Flat bench press", "details": "3-4 sets of 8-12 reps"},
                            {"name": "Cable flies", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Incline dumbbell flies", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Upper cable flies", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Butterfly chest dips", "details": "3-4 sets of 8-10 reps"},
                            {"name": "Incline bench press", "details": "3-4 sets of 8-10 reps"},
                            {"name": "Bent over flies", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Butterfly dumbbell", "details": "3-4 sets of 10-12 reps"}
                        ],
                        "notes": "Focus on progressive overload and proper form."
                    },
                    "Tuesday": {
                        "focus": "Biceps",
                        "exercises": [
                            {"name": "Zig zag bar curls", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Hammer curls", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Cable curls", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Cable handle curls", "details": "3-4 sets of 10-12 reps"}
                        ],
                        "notes": "Focus on controlled movements and muscle contraction."
                    },
                    "Wednesday": {
                        "focus": "Back",
                        "exercises": [
                            {"name": "Pull-ups", "details": "3-4 sets of 8-12 reps"},
                            {"name": "Barbell rowing", "details": "3-4 sets of 8-10 reps"},
                            {"name": "Lat pulldowns", "details": "3-4 sets of 10-12 reps"},
                            {"name": "T-bar rows", "details": "3-4 sets of 8-10 reps"},
                            {"name": "Close grip pulldowns", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Cable rowing", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Single dumbbell rowing", "details": "3-4 sets of 10-12 reps each arm"}
                        ],
                        "notes": "Focus on back width and thickness development."
                    },
                    "Thursday": {
                        "focus": "Triceps",
                        "exercises": [
                            {"name": "Zig zag rod incline bench press", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Cable reverse extension", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Rope overhead extension", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Back dips", "details": "3-4 sets of 8-12 reps"}
                        ],
                        "notes": "Focus on tricep isolation and strength building."
                    },
                    "Friday": {
                        "focus": "Legs",
                        "exercises": [
                            {"name": "Weight squats", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Weighted lunges", "details": "3-4 sets of 10-12 reps each leg"},
                            {"name": "Hamstring leg press", "details": "3-4 sets of 12-15 reps"},
                            {"name": "Calf machine leg raises", "details": "3-4 sets of 12-15 reps"},
                            {"name": "Reverse leg extension", "details": "3-4 sets of 12-15 reps"}
                        ],
                        "notes": "Focus on compound movements and progressive overload."
                    },
                    "Saturday": {
                        "focus": "Full Body",
                        "exercises": [
                            {"name": "Circuit training", "details": "3 rounds of mixed exercises"},
                            {"name": "Cardio", "details": "20-30 minutes moderate intensity"}
                        ],
                        "notes": "Combine strength and cardio for overall fitness."
                    }
                },
                "female": {
                    "Monday": {
                        "focus": "Chest",
                        "exercises": [
                            {"name": "Flat bench press", "details": "3-4 sets of 8-12 reps"},
                            {"name": "Cable flies", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Incline dumbbell flies", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Upper cable flies", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Butterfly chest dips", "details": "3-4 sets of 8-10 reps"},
                            {"name": "Incline bench press", "details": "3-4 sets of 8-10 reps"},
                            {"name": "Bent over flies", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Butterfly dumbbell", "details": "3-4 sets of 10-12 reps"}
                        ],
                        "notes": "Use moderate weights and focus on muscle activation."
                    },
                    "Tuesday": {
                        "focus": "Biceps",
                        "exercises": [
                            {"name": "Zig zag bar curls", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Hammer curls", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Cable curls", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Cable handle curls", "details": "3-4 sets of 10-12 reps"}
                        ],
                        "notes": "Focus on controlled movements and proper form."
                    },
                    "Wednesday": {
                        "focus": "Back",
                        "exercises": [
                            {"name": "Assisted pull-ups", "details": "3-4 sets of 8-12 reps"},
                            {"name": "Barbell rowing", "details": "3-4 sets of 8-10 reps"},
                            {"name": "Lat pulldowns", "details": "3-4 sets of 10-12 reps"},
                            {"name": "T-bar rows", "details": "3-4 sets of 8-10 reps"},
                            {"name": "Close grip pulldowns", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Cable rowing", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Single dumbbell rowing", "details": "3-4 sets of 10-12 reps each arm"}
                        ],
                        "notes": "Focus on back development with proper form."
                    },
                    "Thursday": {
                        "focus": "Triceps",
                        "exercises": [
                            {"name": "Zig zag rod incline bench press", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Cable reverse extension", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Rope overhead extension", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Back dips", "details": "3-4 sets of 8-12 reps"}
                        ],
                        "notes": "Focus on tricep toning and strength."
                    },
                    "Friday": {
                        "focus": "Legs",
                        "exercises": [
                            {"name": "Weight squats", "details": "3-4 sets of 10-12 reps"},
                            {"name": "Weighted lunges", "details": "3-4 sets of 10-12 reps each leg"},
                            {"name": "Hamstring leg press", "details": "3-4 sets of 12-15 reps"},
                            {"name": "Calf machine leg raises", "details": "3-4 sets of 12-15 reps"},
                            {"name": "Reverse leg extension", "details": "3-4 sets of 12-15 reps"}
                        ],
                        "notes": "Focus on lower body strength and toning."
                    },
                    "Saturday": {
                        "focus": "Full Body",
                        "exercises": [
                            {"name": "Circuit training", "details": "3 rounds of mixed exercises"},
                            {"name": "Cardio", "details": "20-30 minutes moderate intensity"}
                        ],
                        "notes": "Combine strength and cardio for overall fitness."
                    }
                }
            }
        # Hardcore intensity workouts
        else:  # hardcore
            hardcore_note = "HARDCORE LEVEL: Increase weight and sets or repetitions for maximum intensity and muscle growth."
            workout_plans = {
                "male": {
                    "Monday": {
                        "focus": "Chest",
                        "exercises": [
                            {"name": "Flat bench press", "details": "4-5 sets of 6-10 reps (heavy weight)"},
                            {"name": "Cable flies", "details": "4-5 sets of 10-15 reps"},
                            {"name": "Incline dumbbell flies", "details": "4-5 sets of 10-15 reps"},
                            {"name": "Upper cable flies", "details": "4-5 sets of 10-15 reps"},
                            {"name": "Butterfly chest dips", "details": "4-5 sets of 8-12 reps"},
                            {"name": "Incline bench press", "details": "4-5 sets of 6-10 reps"},
                            {"name": "Bent over flies", "details": "4-5 sets of 12-15 reps"},
                            {"name": "Butterfly dumbbell", "details": "4-5 sets of 12-15 reps"}
                        ],
                        "notes": hardcore_note + " Focus on maximum muscle stimulation."
                    },
                    "Tuesday": {
                        "focus": "Biceps",
                        "exercises": [
                            {"name": "Zig zag bar curls", "details": "4-5 sets of 8-12 reps (heavy weight)"},
                            {"name": "Hammer curls", "details": "4-5 sets of 10-15 reps"},
                            {"name": "Cable curls", "details": "4-5 sets of 10-15 reps"},
                            {"name": "Cable handle curls", "details": "4-5 sets of 10-15 reps"}
                        ],
                        "notes": hardcore_note + " Push to muscle failure."
                    },
                    "Wednesday": {
                        "focus": "Back",
                        "exercises": [
                            {"name": "Pull-ups", "details": "4-5 sets of 8-15 reps (add weight if needed)"},
                            {"name": "Barbell rowing", "details": "4-5 sets of 6-10 reps (heavy weight)"},
                            {"name": "Lat pulldowns", "details": "4-5 sets of 10-15 reps"},
                            {"name": "T-bar rows", "details": "4-5 sets of 8-12 reps"},
                            {"name": "Close grip pulldowns", "details": "4-5 sets of 10-15 reps"},
                            {"name": "Cable rowing", "details": "4-5 sets of 10-15 reps"},
                            {"name": "Single dumbbell rowing", "details": "4-5 sets of 10-15 reps each arm"}
                        ],
                        "notes": hardcore_note + " Focus on back width and thickness."
                    },
                    "Thursday": {
                        "focus": "Triceps",
                        "exercises": [
                            {"name": "Zig zag rod incline bench press", "details": "4-5 sets of 8-12 reps"},
                            {"name": "Cable reverse extension", "details": "4-5 sets of 10-15 reps"},
                            {"name": "Rope overhead extension", "details": "4-5 sets of 10-15 reps"},
                            {"name": "Back dips", "details": "4-5 sets of 8-15 reps (add weight if needed)"}
                        ],
                        "notes": hardcore_note + " Maximum tricep development."
                    },
                    "Friday": {
                        "focus": "Legs",
                        "exercises": [
                            {"name": "Weight squats", "details": "4-5 sets of 6-12 reps (heavy weight)"},
                            {"name": "Weighted lunges", "details": "4-5 sets of 10-15 reps each leg"},
                            {"name": "Hamstring leg press", "details": "4-5 sets of 12-20 reps"},
                            {"name": "Calf machine leg raises", "details": "4-5 sets of 15-20 reps"},
                            {"name": "Reverse leg extension", "details": "4-5 sets of 12-20 reps"}
                        ],
                        "notes": hardcore_note + " Focus on leg power and mass."
                    },
                    "Saturday": {
                        "focus": "Full Body Power",
                        "exercises": [
                            {"name": "High intensity circuit", "details": "4-5 rounds of compound exercises"},
                            {"name": "HIIT cardio", "details": "20-30 minutes high intensity"}
                        ],
                        "notes": hardcore_note + " Maximum intensity training."
                    }
                },
                "female": {
                    "Monday": {
                        "focus": "Chest",
                        "exercises": [
                            {"name": "Flat bench press", "details": "4-5 sets of 8-12 reps"},
                            {"name": "Cable flies", "details": "4-5 sets of 12-15 reps"},
                            {"name": "Incline dumbbell flies", "details": "4-5 sets of 12-15 reps"},
                            {"name": "Upper cable flies", "details": "4-5 sets of 12-15 reps"},
                            {"name": "Butterfly chest dips", "details": "4-5 sets of 8-12 reps"},
                            {"name": "Incline bench press", "details": "4-5 sets of 8-12 reps"},
                            {"name": "Bent over flies", "details": "4-5 sets of 12-15 reps"},
                            {"name": "Butterfly dumbbell", "details": "4-5 sets of 12-15 reps"}
                        ],
                        "notes": hardcore_note + " Focus on muscle definition and strength."
                    },
                    "Tuesday": {
                        "focus": "Biceps",
                        "exercises": [
                            {"name": "Zig zag bar curls", "details": "4-5 sets of 10-15 reps"},
                            {"name": "Hammer curls", "details": "4-5 sets of 12-15 reps"},
                            {"name": "Cable curls", "details": "4-5 sets of 12-15 reps"},
                            {"name": "Cable handle curls", "details": "4-5 sets of 12-15 reps"}
                        ],
                        "notes": hardcore_note + " Focus on arm definition."
                    },
                    "Wednesday": {
                        "focus": "Back",
                        "exercises": [
                            {"name": "Pull-ups/Assisted pull-ups", "details": "4-5 sets of 8-15 reps"},
                            {"name": "Barbell rowing", "details": "4-5 sets of 8-12 reps"},
                            {"name": "Lat pulldowns", "details": "4-5 sets of 12-15 reps"},
                            {"name": "T-bar rows", "details": "4-5 sets of 10-12 reps"},
                            {"name": "Close grip pulldowns", "details": "4-5 sets of 12-15 reps"},
                            {"name": "Cable rowing", "details": "4-5 sets of 12-15 reps"},
                            {"name": "Single dumbbell rowing", "details": "4-5 sets of 12-15 reps each arm"}
                        ],
                        "notes": hardcore_note + " Focus on back strength and posture."
                    },
                    "Thursday": {
                        "focus": "Triceps",
                        "exercises": [
                            {"name": "Zig zag rod incline bench press", "details": "4-5 sets of 10-15 reps"},
                            {"name": "Cable reverse extension", "details": "4-5 sets of 12-15 reps"},
                            {"name": "Rope overhead extension", "details": "4-5 sets of 12-15 reps"},
                            {"name": "Back dips", "details": "4-5 sets of 8-15 reps"}
                        ],
                        "notes": hardcore_note + " Focus on tricep definition."
                    },
                    "Friday": {
                        "focus": "Legs",
                        "exercises": [
                            {"name": "Weight squats", "details": "4-5 sets of 10-15 reps"},
                            {"name": "Weighted lunges", "details": "4-5 sets of 12-15 reps each leg"},
                            {"name": "Hamstring leg press", "details": "4-5 sets of 15-20 reps"},
                            {"name": "Calf machine leg raises", "details": "4-5 sets of 15-20 reps"},
                            {"name": "Reverse leg extension", "details": "4-5 sets of 15-20 reps"}
                        ],
                        "notes": hardcore_note + " Focus on lower body strength and toning."
                    },
                    "Saturday": {
                        "focus": "Full Body Power",
                        "exercises": [
                            {"name": "High intensity circuit", "details": "4-5 rounds of compound exercises"},
                            {"name": "HIIT cardio", "details": "20-30 minutes high intensity"}
                        ],
                        "notes": hardcore_note + " Maximum intensity for results."
                    }
                }
            }
        
        workout = workout_plans[gender][day]
    
    # Ensure all exercises have video_url
    if "exercises" in workout and isinstance(workout["exercises"], list):
        for exercise in workout["exercises"]:
            if isinstance(exercise, dict) and "name" in exercise:
                video_url = get_exercise_video_url(exercise["name"])
                exercise["video_url"] = video_url
    
    # Add muscle group image
    if "focus" in workout:
        workout["image_url"] = get_muscle_group_image(workout["focus"])
    
    return workout
