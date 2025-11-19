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

def generate_diet_plan(gender, food_preference, bmi_category, week_number=1, user_intensity=None):
    """
    Generate a weekly diet plan based on gender, food preference, BMI category, and week
    
    Args:
        gender (str): 'male' or 'female'
        food_preference (str): 'veg' or 'non-veg'
        bmi_category (str): BMI category
        week_number (int): Week number (1-4)
        user_intensity (str): User selected intensity ('easy', 'intermediate', 'hardcore')
        
    Returns:
        dict: Weekly diet plan with new structure
    """
    # Map user intensity to diet levels if provided
    if user_intensity:
        intensity_mapping = {
            "easy": "beginner",
            "intermediate": "intermediate", 
            "hardcore": "advanced"
        }
        intensity = intensity_mapping.get(user_intensity, "beginner")
    else:
        # Fallback: Determine intensity level based on BMI
        if bmi_category in ["Underweight", "Normal weight"]:
            intensity = "beginner"  # 1800-2000 kcal
        elif bmi_category == "Overweight":
            intensity = "intermediate"  # 2200-2400 kcal
        else:  # Obese
            intensity = "advanced"  # 2600-3000 kcal
    
    return generate_weekly_diet(intensity, food_preference, week_number)

def generate_weekly_diet(intensity, food_preference, week_number):
    """
    Generate diet plan based on intensity level and week number
    """
    diet_plans = {
        "beginner": get_beginner_diet(week_number, food_preference),
        "intermediate": get_intermediate_diet(week_number, food_preference),
        "advanced": get_advanced_diet(week_number, food_preference)
    }
    
    return diet_plans.get(intensity, diet_plans["beginner"])

def get_beginner_diet(week_number, food_preference):
    """Beginner level diet (1800-2000 kcal)"""
    if week_number == 1:
        return {
            "level": "🔥 LEVEL 1 — BEGINNER (1800–2000 kcal)",
            "week": "WEEK 1",
            "protein_target": "75–90g",
            "Monday": {
                "early_morning": {"meal": "Warm water + chia (1 tsp)", "time": "6:00 AM"},
                "breakfast": {"meal": "2 roti + Mixed sabzi + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": "Rice (1 cup) + Dal (1 bowl) + Leafy veg curry", "time": "1:00 PM"},
                "snack": {"meal": "Banana (1)", "time": "4:00 PM"},
                "dinner": {"meal": "2 roti + " + ("Paneer 150g (bhurji)" if food_preference == "veg" else "Chicken 150g (grilled/boiled)"), "time": "8:00 PM"},
                "calories": "~1850 kcal", "protein": "~85g"
            },
            "Tuesday": {
                "early_morning": {"meal": "Jeera water", "time": "6:00 AM"},
                "breakfast": {"meal": "Poha (1 bowl) + 1 boiled egg", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Dal + sabzi", "time": "1:00 PM"},
                "snack": {"meal": "Buttermilk (1 glass)", "time": "4:00 PM"},
                "dinner": {"meal": "Khichdi (1 bowl) + Curd (1 bowl)", "time": "8:00 PM"},
                "calories": "~1800 kcal", "protein": "~75-80g"
            },
            "Wednesday": {
                "early_morning": {"meal": "Lemon + warm water", "time": "6:00 AM"},
                "breakfast": {"meal": "Sprouts (1 bowl) + lemon + Apple (1)", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + rajma", "time": "1:00 PM"},
                "snack": {"meal": "Roasted chana (1 handful)", "time": "4:00 PM"},
                "dinner": {"meal": "2 roti + Paneer 150g (bhurji)", "time": "8:00 PM"},
                "calories": "~1850 kcal", "protein": "~80-85g"
            },
            "Thursday": {
                "early_morning": {"meal": "5 soaked almonds", "time": "6:00 AM"},
                "breakfast": {"meal": "Upma (1 bowl) + 1 boiled egg", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Dal + veggie curry", "time": "1:00 PM"},
                "snack": {"meal": "Orange (1)", "time": "4:00 PM"},
                "dinner": {"meal": ("2 roti + Paneer 150g + sautéed veggies" if food_preference == "veg" else "Chicken 150g + sautéed veggies"), "time": "8:00 PM"},
                "calories": "~1900 kcal", "protein": "~85g"
            },
            "Friday": {
                "early_morning": {"meal": "Warm water", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + milk + banana", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + chole", "time": "1:00 PM"},
                "snack": {"meal": "Sprouts (½ bowl)", "time": "4:00 PM"},
                "dinner": {"meal": "2 roti + Paneer bhurji (150g)", "time": "8:00 PM"},
                "calories": "~1900-2000 kcal", "protein": "~80-90g"
            },
            "Saturday": {
                "early_morning": {"meal": "Jeera water", "time": "6:00 AM"},
                "breakfast": {"meal": "2 idli + sambar + 1 boiled egg", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Mixed veg curry", "time": "1:00 PM"},
                "snack": {"meal": "Coconut water", "time": "4:00 PM"},
                "dinner": {"meal": ("2 roti + Paneer curry 150g + vegetables" if food_preference == "veg" else "Chicken curry 150g + vegetables"), "time": "8:00 PM"},
                "calories": "~1850 kcal", "protein": "~85g"
            },
            "Sunday": {
                "early_morning": {"meal": "Chia water", "time": "6:00 AM"},
                "breakfast": {"meal": "Veg sandwich (2 slices)", "time": "8:00 AM"},
                "lunch": {"meal": "Dal + rice + sabzi", "time": "1:00 PM"},
                "snack": {"meal": "Apple", "time": "4:00 PM"},
                "dinner": {"meal": "2 roti + Egg curry (2 whole + 1 white)", "time": "8:00 PM"},
                "calories": "~1850-1900 kcal", "protein": "~80-85g"
            }
        }
    elif week_number == 2:
        return {
            "level": "🔥 LEVEL 1 — BEGINNER (1800–2000 kcal)",
            "week": "WEEK 2",
            "protein_target": "80–85g",
            "Monday": {
                "early_morning": {"meal": "Jeera water", "time": "6:00 AM"},
                "breakfast": {"meal": "Poha (1 bowl) + 1 boiled egg", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Sabzi + dal", "time": "1:00 PM"},
                "snack": {"meal": "Roasted chana (1 handful)", "time": "4:00 PM"},
                "dinner": {"meal": "Rice (1 cup) + " + ("Paneer curry 150g" if food_preference == "veg" else "Chicken 150g"), "time": "8:00 PM"},
                "calories": "~1850 kcal", "protein": "~80-85g"
            },
            "Tuesday": {
                "early_morning": {"meal": "Warm lemon water", "time": "6:00 AM"},
                "breakfast": {"meal": "Sprouts bowl + 1 fruit (banana/apple)", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + rajma", "time": "1:00 PM"},
                "snack": {"meal": "Buttermilk (1 glass)", "time": "4:00 PM"},
                "dinner": {"meal": "2 roti + Paneer curry 150g", "time": "8:00 PM"},
                "calories": "~1900 kcal", "protein": "~80g"
            },
            "Wednesday": {
                "early_morning": {"meal": "5 almonds", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + milk + ½ banana", "time": "8:00 AM"},
                "lunch": {"meal": "Khichdi + curd", "time": "1:00 PM"},
                "snack": {"meal": "Coconut water", "time": "4:00 PM"},
                "dinner": {"meal": "2 roti + Egg curry (2 whole + 1 white)", "time": "8:00 PM"},
                "calories": "~1850 kcal", "protein": "~82g"
            },
            "Thursday": {
                "early_morning": {"meal": "Warm water", "time": "6:00 AM"},
                "breakfast": {"meal": "Upma (1 bowl)", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Dal + seasonal vegetables", "time": "1:00 PM"},
                "snack": {"meal": "Apple", "time": "4:00 PM"},
                "dinner": {"meal": "Rice + " + ("Paneer 150g" if food_preference == "veg" else "fish 120g"), "time": "8:00 PM"},
                "calories": "~1900 kcal", "protein": "~80g"
            },
            "Friday": {
                "early_morning": {"meal": "Jeera water", "time": "6:00 AM"},
                "breakfast": {"meal": "2 idli + sambar", "time": "8:00 AM"},
                "lunch": {"meal": "Veg pulao + raita", "time": "1:00 PM"},
                "snack": {"meal": "Sprouts salad", "time": "4:00 PM"},
                "dinner": {"meal": "2 roti + Paneer 150g", "time": "8:00 PM"},
                "calories": "~1900 kcal", "protein": "~80-85g"
            },
            "Saturday": {
                "early_morning": {"meal": "Lemon water", "time": "6:00 AM"},
                "breakfast": {"meal": "2 boiled eggs + 2 slices brown bread", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Chole", "time": "1:00 PM"},
                "snack": {"meal": "Orange", "time": "4:00 PM"},
                "dinner": {"meal": "Rice + " + ("Paneer curry 150g" if food_preference == "veg" else "chicken 150g"), "time": "8:00 PM"},
                "calories": "~1900 kcal", "protein": "~85g"
            },
            "Sunday": {
                "early_morning": {"meal": "Chia water", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + peanut butter (1 tsp)", "time": "8:00 AM"},
                "lunch": {"meal": "Dal + rice + sabzi", "time": "1:00 PM"},
                "snack": {"meal": "Buttermilk", "time": "4:00 PM"},
                "dinner": {"meal": "Paneer 150g + veg", "time": "8:00 PM"},
                "calories": "~1850-1900 kcal", "protein": "~82-85g"
            }
        }
    # Add weeks 3 and 4 for beginner level
    elif week_number == 3:
        return {
            "level": "🔥 LEVEL 1 — BEGINNER (1800–2000 kcal)",
            "week": "WEEK 3",
            "protein_target": "80–85g",
            "Monday": {
                "early_morning": {"meal": "Chia water", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + milk + banana", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + dal + sabzi", "time": "1:00 PM"},
                "snack": {"meal": "Roasted chana", "time": "4:00 PM"},
                "dinner": {"meal": "2 roti + Paneer curry 150g", "time": "8:00 PM"},
                "calories": "~1900 kcal", "protein": "~80-85g"
            },
            "Tuesday": {
                "early_morning": {"meal": "Jeera water", "time": "6:00 AM"},
                "breakfast": {"meal": "Poha + lemon + peanuts", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Dal + veg", "time": "1:00 PM"},
                "snack": {"meal": "Buttermilk", "time": "4:00 PM"},
                "dinner": {"meal": ("2 roti + Paneer curry 150g" if food_preference == "veg" else "Chicken curry 150g + 2 roti"), "time": "8:00 PM"},
                "calories": "~1900 kcal", "protein": "~85g"
            },
            "Wednesday": {
                "early_morning": {"meal": "Lemon warm water", "time": "6:00 AM"},
                "breakfast": {"meal": "Sprouts bowl + 1 apple", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + rajma", "time": "1:00 PM"},
                "snack": {"meal": "Coconut water", "time": "4:00 PM"},
                "dinner": {"meal": "2 roti + Paneer bhurji 150g", "time": "8:00 PM"},
                "calories": "~1850 kcal", "protein": "~80-85g"
            },
            "Thursday": {
                "early_morning": {"meal": "5 almonds", "time": "6:00 AM"},
                "breakfast": {"meal": "Upma + 1 boiled egg", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Dal + sabzi", "time": "1:00 PM"},
                "snack": {"meal": "Orange", "time": "4:00 PM"},
                "dinner": {"meal": "Egg curry (2 whole + 1 egg white) + 1 roti", "time": "8:00 PM"},
                "calories": "~1850-1900 kcal", "protein": "~80g"
            },
            "Friday": {
                "early_morning": {"meal": "Warm water", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + peanut butter (1 tsp)", "time": "8:00 AM"},
                "lunch": {"meal": "Khichdi + curd", "time": "1:00 PM"},
                "snack": {"meal": "Sprouts", "time": "4:00 PM"},
                "dinner": {"meal": "2 roti + " + ("Paneer 150g" if food_preference == "veg" else "Chicken 150g"), "time": "8:00 PM"},
                "calories": "~1900 kcal", "protein": "~85g"
            },
            "Saturday": {
                "early_morning": {"meal": "Lemon water", "time": "6:00 AM"},
                "breakfast": {"meal": "2 idli + sambar", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + chole", "time": "1:00 PM"},
                "snack": {"meal": "Apple", "time": "4:00 PM"},
                "dinner": {"meal": "2 roti + Paneer 150g", "time": "8:00 PM"},
                "calories": "~1850-1900 kcal", "protein": "~80-85g"
            },
            "Sunday": {
                "early_morning": {"meal": "Jeera water", "time": "6:00 AM"},
                "breakfast": {"meal": "Veg sandwich", "time": "8:00 AM"},
                "lunch": {"meal": "Dal + rice + leafy veg", "time": "1:00 PM"},
                "snack": {"meal": "Buttermilk", "time": "4:00 PM"},
                "dinner": {"meal": ("Paneer curry 150g + 1 roti" if food_preference == "veg" else "Fish curry 120-150g + 1 roti"), "time": "8:00 PM"},
                "calories": "~1850 kcal", "protein": "~80g"
            }
        }
    else:  # week 4
        return {
            "level": "🔥 LEVEL 1 — BEGINNER (1800–2000 kcal)",
            "week": "WEEK 4",
            "protein_target": "80–85g",
            "Monday": {
                "early_morning": {"meal": "Lemon warm water", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + milk + banana", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Dal + veg", "time": "1:00 PM"},
                "snack": {"meal": "Buttermilk", "time": "4:00 PM"},
                "dinner": {"meal": ("Chicken 150g + 2 roti" if food_preference == "non-veg" else "Paneer curry 150g + 2 roti"), "time": "8:00 PM"},
                "calories": "~1900 kcal",
                "protein": "~85g"
            },
            "Tuesday": {
                "early_morning": {"meal": "Jeera water", "time": "6:00 AM"},
                "breakfast": {"meal": "Upma (1 bowl) + 1 boiled egg", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + dal + sabzi", "time": "1:00 PM"},
                "snack": {"meal": "Apple", "time": "4:00 PM"},
                "dinner": {"meal": "Paneer curry 150g + 2 roti", "time": "8:00 PM"},
                "calories": "~1850-1900 kcal",
                "protein": "~82-85g"
            },
            "Wednesday": {
                "early_morning": {"meal": "Warm water + chia", "time": "6:00 AM"},
                "breakfast": {"meal": "Sprouts + 1 fruit", "time": "8:00 AM"},
                "lunch": {"meal": "Rajma + rice", "time": "1:00 PM"},
                "snack": {"meal": "Coconut water", "time": "4:00 PM"},
                "dinner": {"meal": ("2 roti + Fish curry (120-150g)" if food_preference == "non-veg" else "2 roti + Paneer curry 150g"), "time": "8:00 PM"},
                "calories": "~1850 kcal",
                "protein": "~80-85g"
            },
            "Thursday": {
                "early_morning": {"meal": "5 soaked almonds", "time": "6:00 AM"},
                "breakfast": {"meal": "Poha + lemon", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Dal + veg curry", "time": "1:00 PM"},
                "snack": {"meal": "Roasted chana", "time": "4:00 PM"},
                "dinner": {"meal": "2 roti + Egg curry (2 whole + 1 white)", "time": "8:00 PM"},
                "calories": "~1850 kcal",
                "protein": "~80-85g"
            },
            "Friday": {
                "early_morning": {"meal": "Lemon water", "time": "6:00 AM"},
                "breakfast": {"meal": "Idli (2) + sambar", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + chole", "time": "1:00 PM"},
                "snack": {"meal": "Sprouts", "time": "4:00 PM"},
                "dinner": {"meal": "Paneer 150g + veg", "time": "8:00 PM"},
                "calories": "~1900 kcal",
                "protein": "~80-85g"
            },
            "Saturday": {
                "early_morning": {"meal": "Jeera water", "time": "6:00 AM"},
                "breakfast": {"meal": "Bread omelette (2 slices + 1 egg)", "time": "8:00 AM"},
                "lunch": {"meal": "Dal + rice + sabzi", "time": "1:00 PM"},
                "snack": {"meal": "Orange", "time": "4:00 PM"},
                "dinner": {"meal": ("Chicken curry 150g + 1 roti" if food_preference == "non-veg" else "Paneer curry 150g + 1 roti"), "time": "8:00 PM"},
                "calories": "~1900 kcal",
                "protein": "~85g"
            },
            "Sunday": {
                "early_morning": {"meal": "Warm water", "time": "6:00 AM"},
                "breakfast": {"meal": "Veg sandwich", "time": "8:00 AM"},
                "lunch": {"meal": "Roti (2) + dal + veg", "time": "1:00 PM"},
                "snack": {"meal": "Buttermilk", "time": "4:00 PM"},
                "dinner": {"meal": "Paneer bhurji 150g", "time": "8:00 PM"},
                "calories": "~1850-1900 kcal",
                "protein": "~80g"
            }
        }

def get_intermediate_diet(week_number, food_preference):
    """Intermediate level diet (2200-2400 kcal)"""
    if week_number == 1:
        return {
            "level": "🔥 LEVEL 2 — INTERMEDIATE (2200–2400 kcal)",
            "week": "WEEK 1",
            "protein_target": "130–140g",
            "Monday": {
                "early_morning": {"meal": "Chia water", "time": "6:00 AM"},
                "breakfast": {"meal": "2 roti + sabzi + 2 boiled eggs + Soaked chana (½ bowl)", "time": "8:00 AM"},
                "lunch": {"meal": "Rice (1 cup) + Leafy veg curry + 2 egg whites", "time": "1:00 PM"},
                "pre_workout": {"meal": "Oats + milk + banana + 1 tbsp peanut butter", "time": "4:30 PM"},
                "post_workout": {"meal": "3 egg whites + 1 whole egg", "time": "6:30 PM"},
                "dinner": {"meal": "2 roti + " + ("Paneer 250g" if food_preference == "veg" else "Chicken 250g"), "time": "8:00 PM"},
                "calories": "~2300 kcal",
                "protein": "~135g"
            },
            "Tuesday": {
                "early_morning": {"meal": "Warm water + lemon", "time": "6:00 AM"},
                "breakfast": {"meal": "Sprouts bowl + 1 fruit (apple/banana) + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Dal + sabzi + Curd (½ bowl)", "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana + black coffee", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop) OR 3 egg whites", "time": "6:30 PM"},
                "dinner": {"meal": "Rice + " + ("Paneer 200g" if food_preference == "veg" else "Fish 200g"), "time": "8:00 PM"},
                "calories": "~2300 kcal",
                "protein": "~130–135g"
            },
            "Wednesday": {
                "early_morning": {"meal": "Jeera water", "time": "6:00 AM"},
                "breakfast": {"meal": "Veg omelette (3 eggs) + 1 roti", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + Dal + " + ("Paneer curry 100g" if food_preference == "veg" else "Chicken curry 100g"), "time": "1:00 PM"},
                "pre_workout": {"meal": "Peanut butter bread (1 slice + PB)", "time": "4:30 PM"},
                "post_workout": {"meal": "3 egg whites + any fruit juice", "time": "6:30 PM"},
                "dinner": {"meal": "2 roti + Paneer 200g", "time": "8:00 PM"},
                "calories": "~2250–2350 kcal",
                "protein": "~130g"
            },
            "Thursday": {
                "early_morning": {"meal": "5 soaked almonds", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + milk + banana", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Dal + mixed veg", "time": "1:00 PM"},
                "pre_workout": {"meal": "2 dates + 1 banana", "time": "4:30 PM"},
                "post_workout": {"meal": "1 whole egg + 3 whites", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer tikka 200g" if food_preference == "veg" else "Chicken tikka / grilled chicken 200g"), "time": "8:00 PM"},
                "calories": "~2300 kcal",
                "protein": "~135g"
            },
            "Friday": {
                "early_morning": {"meal": "Lemon water", "time": "6:00 AM"},
                "breakfast": {"meal": "Poha + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + rajma", "time": "1:00 PM"},
                "pre_workout": {"meal": "Oats shake (oats + milk + banana)", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop)", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer 200g + 2 roti", "time": "8:00 PM"},
                "calories": "~2350 kcal",
                "protein": "~130g"
            },
            "Saturday": {
                "early_morning": {"meal": "Coconut water", "time": "6:00 AM"},
                "breakfast": {"meal": "Bread omelette (2 slices + 2 eggs)", "time": "8:00 AM"},
                "lunch": {"meal": ("Paneer curry + rice" if food_preference == "veg" else "Chicken curry + rice"), "time": "1:00 PM"},
                "pre_workout": {"meal": "Coffee + banana", "time": "4:30 PM"},
                "post_workout": {"meal": "3 egg whites", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 200g + 1 roti" if food_preference == "veg" else "Fish 200g + 1 roti"), "time": "8:00 PM"},
                "calories": "~2300 kcal",
                "protein": "~130–135g"
            },
            "Sunday": {
                "early_morning": {"meal": "Warm water + chia", "time": "6:00 AM"},
                "breakfast": {"meal": "Sprouts + 2 eggs", "time": "8:00 AM"},
                "lunch": {"meal": "Veg biryani (1 bowl) + Curd (½ bowl)", "time": "1:00 PM"},
                "pre_workout": {"meal": "Dates (2–3)", "time": "4:30 PM"},
                "post_workout": {"meal": "Juice + 3 egg whites", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer 200g + 1 roti", "time": "8:00 PM"},
                "calories": "~2200–2300 kcal",
                "protein": "~125–130g"
            }
        }
    elif week_number == 2:
        return {
            "level": "🔥 LEVEL 2 — INTERMEDIATE (2200–2400 kcal)",
            "week": "WEEK 2",
            "protein_target": "125–135g",
            "Monday": {
                "early_morning": {"meal": "Warm lemon water", "time": "6:00 AM"},
                "breakfast": {"meal": "Upma (1 bowl) + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Dal + sabzi", "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana + coffee", "time": "4:30 PM"},
                "post_workout": {"meal": "3 egg whites + 1 whole egg", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 250g + salad" if food_preference == "veg" else "Chicken 250g + salad"), "time": "8:00 PM"},
                "calories": "~2300 kcal",
                "protein": "~130g"
            },
            "Tuesday": {
                "early_morning": {"meal": "Jeera water", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + milk + ½ banana", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + dal + mixed veg", "time": "1:00 PM"},
                "pre_workout": {"meal": "1 slice bread + peanut butter", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop)", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer curry 200g + 2 roti", "time": "8:00 PM"},
                "calories": "~2300–2400 kcal",
                "protein": "~130–135g"
            },
            "Wednesday": {
                "early_morning": {"meal": "Chia water", "time": "6:00 AM"},
                "breakfast": {"meal": "Poha (1 bowl) + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Dal + sabzi", "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana", "time": "4:30 PM"},
                "post_workout": {"meal": "3 egg whites + juice", "time": "6:30 PM"},
                "dinner": {"meal": "Egg curry (3 whole eggs) + 1 roti", "time": "8:00 PM"},
                "calories": "~2250–2350 kcal",
                "protein": "~125–130g"
            },
            "Thursday": {
                "early_morning": {"meal": "5 almonds", "time": "6:00 AM"},
                "breakfast": {"meal": "Veg omelette (3 eggs) + 1 roti", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + rajma", "time": "1:00 PM"},
                "pre_workout": {"meal": "Dates (2–3)", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop)", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer grilled 200g + veg" if food_preference == "veg" else "Chicken grilled 200g + veg"), "time": "8:00 PM"},
                "calories": "~2350 kcal",
                "protein": "~135g"
            },
            "Friday": {
                "early_morning": {"meal": "Warm water", "time": "6:00 AM"},
                "breakfast": {"meal": "Sprouts bowl + 1 fruit + 1 boiled egg", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + chole", "time": "1:00 PM"},
                "pre_workout": {"meal": "Peanut butter bread", "time": "4:30 PM"},
                "post_workout": {"meal": "3 egg whites", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer 200g + 2 roti", "time": "8:00 PM"},
                "calories": "~2300–2400 kcal",
                "protein": "~130g"
            },
            "Saturday": {
                "early_morning": {"meal": "Coconut water", "time": "6:00 AM"},
                "breakfast": {"meal": "Idli 2 + sambar + 1 boiled egg", "time": "8:00 AM"},
                "lunch": {"meal": "Dal + rice + sabzi", "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana + coffee", "time": "4:30 PM"},
                "post_workout": {"meal": "1 whole egg + 3 whites", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer curry 200g + 1 roti" if food_preference == "veg" else "Fish curry 200g + 1 roti"), "time": "8:00 PM"},
                "calories": "~2300 kcal",
                "protein": "~130g"
            },
            "Sunday": {
                "early_morning": {"meal": "Lemon water", "time": "6:00 AM"},
                "breakfast": {"meal": "Bread omelette (2 eggs + 2 slices)", "time": "8:00 AM"},
                "lunch": {"meal": ("Paneer curry + rice" if food_preference == "veg" else "Chicken curry + rice"), "time": "1:00 PM"},
                "pre_workout": {"meal": "Dates (2–3)", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop)", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer tikka 200g", "time": "8:00 PM"},
                "calories": "~2300 kcal",
                "protein": "~130–135g"
            }
        }
    elif week_number == 3:
        return {
            "level": "🔥 LEVEL 2 — INTERMEDIATE (2200–2400 kcal)",
            "week": "WEEK 3",
            "protein_target": "125–135g",
            "Monday": {
                "early_morning": {"meal": "Jeera water", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + milk + banana", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + " + ("paneer curry 150g" if food_preference == "veg" else "chicken curry 150g"), "time": "1:00 PM"},
                "pre_workout": {"meal": "Peanut butter bread", "time": "4:30 PM"},
                "post_workout": {"meal": "3 egg whites + juice", "time": "6:30 PM"},
                "dinner": {"meal": "2 roti + Paneer curry 200g", "time": "8:00 PM"},
                "calories": "~2300 kcal",
                "protein": "~130g"
            },
            "Tuesday": {
                "early_morning": {"meal": "Lemon warm water", "time": "6:00 AM"},
                "breakfast": {"meal": "Poha + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + dal + sabzi", "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana + coffee", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop)", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer curry 200g + 1 roti" if food_preference == "veg" else "Fish curry 200g + 1 roti"), "time": "8:00 PM"},
                "calories": "~2300 kcal",
                "protein": "~130–135g"
            },
            "Wednesday": {
                "early_morning": {"meal": "Chia + warm water", "time": "6:00 AM"},
                "breakfast": {"meal": "Idli (2) + sambar + 1 boiled egg", "time": "8:00 AM"},
                "lunch": {"meal": "Rajma + rice", "time": "1:00 PM"},
                "pre_workout": {"meal": "Dates (2–3)", "time": "4:30 PM"},
                "post_workout": {"meal": "1 whole egg + 3 egg whites", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 200g + salad" if food_preference == "veg" else "Chicken 200g + salad"), "time": "8:00 PM"},
                "calories": "~2350 kcal",
                "protein": "~130g"
            },
            "Thursday": {
                "early_morning": {"meal": "5 almonds", "time": "6:00 AM"},
                "breakfast": {"meal": "Veg omelette (3 eggs) + 1 roti", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + dal + veg", "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop)", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer 200g + veg", "time": "8:00 PM"},
                "calories": "~2300–2400 kcal",
                "protein": "~130–135g"
            },
            "Friday": {
                "early_morning": {"meal": "Warm water", "time": "6:00 AM"},
                "breakfast": {"meal": "Sprouts + 1 fruit + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + chole", "time": "1:00 PM"},
                "pre_workout": {"meal": "Peanut butter oats shake", "time": "4:30 PM"},
                "post_workout": {"meal": "3 egg whites", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 200g + 1 roti" if food_preference == "veg" else "Fish 200g + 1 roti"), "time": "8:00 PM"},
                "calories": "~2250–2350 kcal",
                "protein": "~130g"
            },
            "Saturday": {
                "early_morning": {"meal": "Coconut water", "time": "6:00 AM"},
                "breakfast": {"meal": "Bread omelette (2 eggs + 2 slices)", "time": "8:00 AM"},
                "lunch": {"meal": "Dal + rice + sabzi", "time": "1:00 PM"},
                "pre_workout": {"meal": "Dates (2) + banana", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop)", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer curry 200g" if food_preference == "veg" else "Chicken curry 200g"), "time": "8:00 PM"},
                "calories": "~2350–2400 kcal",
                "protein": "~135g"
            },
            "Sunday": {
                "early_morning": {"meal": "Lemon water", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + peanut butter (1 tbsp)", "time": "8:00 AM"},
                "lunch": {"meal": "Veg biryani + curd", "time": "1:00 PM"},
                "pre_workout": {"meal": "Coffee + banana", "time": "4:30 PM"},
                "post_workout": {"meal": "1 egg + 3 whites", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer 200g + 1 roti", "time": "8:00 PM"},
                "calories": "~2250–2300 kcal",
                "protein": "~125–130g"
            }
        }
    else:  # week 4
        return {
            "level": "🔥 LEVEL 2 — INTERMEDIATE (2200–2400 kcal)",
            "week": "WEEK 4",
            "protein_target": "125–135g",
            "Monday": {
                "early_morning": {"meal": "Lemon warm water", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + milk + banana", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Dal + sabzi", "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana + coffee", "time": "4:30 PM"},
                "post_workout": {"meal": "3 egg whites + 1 whole egg", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 250g + veg" if food_preference == "veg" else "Chicken 250g + veg"), "time": "8:00 PM"},
                "calories": "~2300 kcal",
                "protein": "~135g"
            },
            "Tuesday": {
                "early_morning": {"meal": "Jeera water", "time": "6:00 AM"},
                "breakfast": {"meal": "Upma + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + dal + veg", "time": "1:00 PM"},
                "pre_workout": {"meal": "Peanut butter bread", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop)", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer curry 200g + 2 roti", "time": "8:00 PM"},
                "calories": "~2300–2400 kcal",
                "protein": "~130–135g"
            },
            "Wednesday": {
                "early_morning": {"meal": "Chia water", "time": "6:00 AM"},
                "breakfast": {"meal": "Sprouts bowl + 1 banana + 1 boiled egg", "time": "8:00 AM"},
                "lunch": {"meal": "Rajma + rice", "time": "1:00 PM"},
                "pre_workout": {"meal": "Dates (2–3)", "time": "4:30 PM"},
                "post_workout": {"meal": "1 whole egg + 3 egg whites", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 200g + 1 roti" if food_preference == "veg" else "Fish 200g + 1 roti"), "time": "8:00 PM"},
                "calories": "~2300 kcal",
                "protein": "~130g"
            },
            "Thursday": {
                "early_morning": {"meal": "5 almonds", "time": "6:00 AM"},
                "breakfast": {"meal": "Veg omelette (3 eggs) + 1 roti", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + dal + veg", "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop)", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 200g + salad" if food_preference == "veg" else "Chicken 200g + salad"), "time": "8:00 PM"},
                "calories": "~2300 kcal",
                "protein": "~130–135g"
            },
            "Friday": {
                "early_morning": {"meal": "Warm water", "time": "6:00 AM"},
                "breakfast": {"meal": "Poha + 2 eggs", "time": "8:00 AM"},
                "lunch": {"meal": "Dal + rice + leafy sabzi", "time": "1:00 PM"},
                "pre_workout": {"meal": "Oats shake", "time": "4:30 PM"},
                "post_workout": {"meal": "3 egg whites", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer 200g + 2 roti", "time": "8:00 PM"},
                "calories": "~2350 kcal",
                "protein": "~135g"
            },
            "Saturday": {
                "early_morning": {"meal": "Coconut water", "time": "6:00 AM"},
                "breakfast": {"meal": "Bread omelette (2 eggs + 2 slices)", "time": "8:00 AM"},
                "lunch": {"meal": ("Paneer curry + rice" if food_preference == "veg" else "Chicken curry + rice"), "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana + coffee", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop)", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 200g" if food_preference == "veg" else "Fish 200g"), "time": "8:00 PM"},
                "calories": "~2300–2400 kcal",
                "protein": "~130–135g"
            },
            "Sunday": {
                "early_morning": {"meal": "Lemon water", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + peanut butter (1 tbsp)", "time": "8:00 AM"},
                "lunch": {"meal": "Veg biryani (1 bowl) + curd", "time": "1:00 PM"},
                "pre_workout": {"meal": "Dates (2–3)", "time": "4:30 PM"},
                "post_workout": {"meal": "1 egg + 3 whites", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer 200g + 1 roti", "time": "8:00 PM"},
                "calories": "~2250–2300 kcal",
                "protein": "~125–130g"
            }
        }

def get_advanced_diet(week_number, food_preference):
    """Advanced level diet (2600-3000 kcal)"""
    if week_number == 1:
        return {
            "level": "🔥 LEVEL 3 — ADVANCED (2600–3000 kcal)",
            "week": "WEEK 1",
            "protein_target": "155–170g",
            "Monday": {
                "early_morning": {"meal": "Chia + electrolytes", "time": "6:00 AM"},
                "breakfast": {"meal": "3-egg omelette + 2 roti + 1 slice bread + peanut butter", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + Dal + " + ("Paneer 200g" if food_preference == "veg" else "Chicken 200g") + " + Salad", "time": "1:00 PM"},
                "pre_workout": {"meal": "Oats + milk + banana + dates + 1 tbsp PB", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop) + 2 boiled eggs", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 300g + 2 roti" if food_preference == "veg" else "Chicken 300g + 2 roti"), "time": "8:00 PM"},
                "calories": "~2900 kcal",
                "protein": "~165g"
            },
            "Tuesday": {
                "early_morning": {"meal": "Coconut water", "time": "6:00 AM"},
                "breakfast": {"meal": "3 idlis + sambar + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": "3 roti + Paneer 200g + Dal", "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana + whey + 5 almonds", "time": "4:30 PM"},
                "post_workout": {"meal": "3 egg whites + juice", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 250g + rice (1 cup)" if food_preference == "veg" else "Mutton 250g + rice (1 cup)"), "time": "8:00 PM"},
                "calories": "~3000 kcal",
                "protein": "~160–170g"
            },
            "Wednesday": {
                "early_morning": {"meal": "Warm electrolytes", "time": "6:00 AM"},
                "breakfast": {"meal": "Chole + 2 roti + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": "Brown rice + Rajma + Curd (½ bowl)", "time": "1:00 PM"},
                "pre_workout": {"meal": "Peanut butter oats shake", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey + 2 boiled eggs", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 300g + veg" if food_preference == "veg" else "Grilled chicken 300g + veg"), "time": "8:00 PM"},
                "calories": "~2850–2950 kcal",
                "protein": "~165g"
            },
            "Thursday": {
                "early_morning": {"meal": "Lemon honey water", "time": "6:00 AM"},
                "breakfast": {"meal": "Heavy oats bowl (oats + milk + banana + PB) + 1 egg", "time": "8:00 AM"},
                "lunch": {"meal": ("Paneer curry 200g" if food_preference == "veg" else "Chicken curry 200g") + " + 2 roti", "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana + dates", "time": "4:30 PM"},
                "post_workout": {"meal": "1 scoop whey", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 300g + 1 roti" if food_preference == "veg" else "Fish 300g + 1 roti"), "time": "8:00 PM"},
                "calories": "~2800–2900 kcal",
                "protein": "~160g"
            },
            "Friday": {
                "early_morning": {"meal": "Chia water", "time": "6:00 AM"},
                "breakfast": {"meal": "Sprouts bowl + 2 boiled eggs + 1 roti", "time": "8:00 AM"},
                "lunch": {"meal": "Veg pulao + Dal + Curd", "time": "1:00 PM"},
                "pre_workout": {"meal": "Coffee + banana", "time": "4:30 PM"},
                "post_workout": {"meal": "Eggs (3 whites + 1 whole)", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 300g" if food_preference == "veg" else "Chicken 300g"), "time": "8:00 PM"},
                "calories": "~2700–2850 kcal",
                "protein": "~160g"
            },
            "Saturday": {
                "early_morning": {"meal": "Electrolyte drink", "time": "6:00 AM"},
                "breakfast": {"meal": "Bread omelette (3 eggs + 3 slices bread)", "time": "8:00 AM"},
                "lunch": {"meal": "Dal + rice + sabzi", "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana + whey", "time": "4:30 PM"},
                "post_workout": {"meal": "2 whole eggs", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer 300g (grilled/bhurji)", "time": "8:00 PM"},
                "calories": "~2600–2750 kcal",
                "protein": "~150–160g"
            },
            "Sunday": {
                "early_morning": {"meal": "Lemon water", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + banana + PB + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": ("Paneer biryani (1.5 cups)" if food_preference == "veg" else "Chicken biryani (1.5 cups)") + " + Curd", "time": "1:00 PM"},
                "pre_workout": {"meal": "3 dates + banana", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop)", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 250g + veg" if food_preference == "veg" else "Fish 250g + veg"), "time": "8:00 PM"},
                "calories": "~2900 kcal",
                "protein": "~155–160g"
            }
        }
    elif week_number == 2:
        return {
            "level": "🔥 LEVEL 3 — ADVANCED (2600–3000 kcal)",
            "week": "WEEK 2",
            "protein_target": "150–170g",
            "Monday": {
                "early_morning": {"meal": "Coconut water + 5 almonds", "time": "6:00 AM"},
                "breakfast": {"meal": "3 eggs omelette + 2 roti + 1 slice bread + peanut butter", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + Dal + " + ("Paneer 200g" if food_preference == "veg" else "Chicken 200g"), "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana + whey + dates", "time": "4:30 PM"},
                "post_workout": {"meal": "2 boiled eggs", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer 300g + 1 roti", "time": "8:00 PM"},
                "calories": "~2800–2950 kcal",
                "protein": "~160–170g"
            },
            "Tuesday": {
                "early_morning": {"meal": "Warm water + chia", "time": "6:00 AM"},
                "breakfast": {"meal": "Idli 3 + sambar + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Paneer 200g + Dal", "time": "1:00 PM"},
                "pre_workout": {"meal": "Oats + banana", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop)", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer curry 250g + rice" if food_preference == "veg" else "Mutton curry 250g + rice"), "time": "8:00 PM"},
                "calories": "~3000 kcal",
                "protein": "~165g"
            },
            "Wednesday": {
                "early_morning": {"meal": "Lemon honey water", "time": "6:00 AM"},
                "breakfast": {"meal": "Chole + 2 roti + 2 eggs", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + Rajma + Salad", "time": "1:00 PM"},
                "pre_workout": {"meal": "Peanut butter shake", "time": "4:30 PM"},
                "post_workout": {"meal": "3 egg whites + juice", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer grill 300g" if food_preference == "veg" else "Chicken grill 300g"), "time": "8:00 PM"},
                "calories": "~2800 kcal",
                "protein": "~160g"
            },
            "Thursday": {
                "early_morning": {"meal": "Electrolyte drink", "time": "6:00 AM"},
                "breakfast": {"meal": "Heavy oats bowl (oats + milk + banana + PB) + 1 boiled egg", "time": "8:00 AM"},
                "lunch": {"meal": "Dal + rice + " + ("paneer 100g" if food_preference == "veg" else "chicken 100g"), "time": "1:00 PM"},
                "pre_workout": {"meal": "Dates + banana", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 300g + 1 roti" if food_preference == "veg" else "Fish 300g + 1 roti"), "time": "8:00 PM"},
                "calories": "~2700–2850 kcal",
                "protein": "~160g"
            },
            "Friday": {
                "early_morning": {"meal": "Warm water + chia", "time": "6:00 AM"},
                "breakfast": {"meal": "Sprouts bowl + 2 boiled eggs + 1 roti", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + chole + Curd", "time": "1:00 PM"},
                "pre_workout": {"meal": "Coffee + banana", "time": "4:30 PM"},
                "post_workout": {"meal": "3 egg whites + 1 egg", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer 300g", "time": "8:00 PM"},
                "calories": "~2700 kcal",
                "protein": "~150–160g"
            },
            "Saturday": {
                "early_morning": {"meal": "Coconut water", "time": "6:00 AM"},
                "breakfast": {"meal": "Bread omelette (3 eggs + 3 bread slices)", "time": "8:00 AM"},
                "lunch": {"meal": "Dal + rice + veg", "time": "1:00 PM"},
                "pre_workout": {"meal": "Peanut butter oats shake", "time": "4:30 PM"},
                "post_workout": {"meal": "2 boiled eggs", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 300g" if food_preference == "veg" else "Chicken 300g"), "time": "8:00 PM"},
                "calories": "~2800–3000 kcal",
                "protein": "~160–170g"
            },
            "Sunday": {
                "early_morning": {"meal": "Lemon water", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + peanut butter + banana + 2 eggs", "time": "8:00 AM"},
                "lunch": {"meal": ("Paneer biryani (large bowl)" if food_preference == "veg" else "Chicken biryani (large bowl)") + " + Curd", "time": "1:00 PM"},
                "pre_workout": {"meal": "Dates 3–4", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 250g + veg" if food_preference == "veg" else "Fish 250g + veg"), "time": "8:00 PM"},
                "calories": "~2900 kcal",
                "protein": "~160g"
            }
        }
    elif week_number == 3:
        return {
            "level": "🔥 LEVEL 3 — ADVANCED (2600–3000 kcal)",
            "week": "WEEK 3",
            "protein_target": "155–170g",
            "Monday": {
                "early_morning": {"meal": "Electrolyte drink", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + milk + banana + peanut butter + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": ("Paneer curry 200g" if food_preference == "veg" else "Chicken curry 200g") + " + Rice (1 cup) + Veg salad", "time": "1:00 PM"},
                "pre_workout": {"meal": "Peanut butter bread", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop) + 1 banana", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer 300g + 1 roti", "time": "8:00 PM"},
                "calories": "~2800 kcal",
                "protein": "~160–165g"
            },
            "Tuesday": {
                "early_morning": {"meal": "Lemon honey water", "time": "6:00 AM"},
                "breakfast": {"meal": "Poha + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Dal + sabzi + Curd", "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana + dates (2–3)", "time": "4:30 PM"},
                "post_workout": {"meal": "2 boiled eggs", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 300g + 1 roti" if food_preference == "veg" else "Fish 300g + 1 roti"), "time": "8:00 PM"},
                "calories": "~2700–2850 kcal",
                "protein": "~160–170g"
            },
            "Wednesday": {
                "early_morning": {"meal": "Coconut water", "time": "6:00 AM"},
                "breakfast": {"meal": "3 egg omelette + 1 roti", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + Rajma + Veg salad", "time": "1:00 PM"},
                "pre_workout": {"meal": "Oats shake (oats + milk + banana)", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop)", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer grill 300g" if food_preference == "veg" else "Chicken grill 300g"), "time": "8:00 PM"},
                "calories": "~2900 kcal",
                "protein": "~165g"
            },
            "Thursday": {
                "early_morning": {"meal": "Chia water", "time": "6:00 AM"},
                "breakfast": {"meal": "Bread omelette (3 eggs + 3 slices)", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + dal + " + ("paneer 150g" if food_preference == "veg" else "chicken 150g"), "time": "1:00 PM"},
                "pre_workout": {"meal": "Coffee + banana", "time": "4:30 PM"},
                "post_workout": {"meal": "3 egg whites + juice", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer 300g", "time": "8:00 PM"},
                "calories": "~2750–2900 kcal",
                "protein": "~155–165g"
            },
            "Friday": {
                "early_morning": {"meal": "Lemon water", "time": "6:00 AM"},
                "breakfast": {"meal": "Sprouts bowl + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": "Dal + rice + sabzi", "time": "1:00 PM"},
                "pre_workout": {"meal": "Dates (3–4) + whey", "time": "4:30 PM"},
                "post_workout": {"meal": "2 whole eggs", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 300g + veg" if food_preference == "veg" else "Chicken 300g + veg"), "time": "8:00 PM"},
                "calories": "~2800–2950 kcal",
                "protein": "~160–170g"
            },
            "Saturday": {
                "early_morning": {"meal": "Electrolyte + 5 almonds", "time": "6:00 AM"},
                "breakfast": {"meal": "Idli 3 + sambar + 2 eggs", "time": "8:00 AM"},
                "lunch": {"meal": ("Paneer biryani (1.5 cups)" if food_preference == "veg" else "Chicken biryani (1.5 cups)") + " + Curd", "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 250g + veg" if food_preference == "veg" else "Fish 250g + veg"), "time": "8:00 PM"},
                "calories": "~2900–3000 kcal",
                "protein": "~160g"
            },
            "Sunday": {
                "early_morning": {"meal": "Lemon + warm water", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + peanut butter + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": "Rajma + rice + salad", "time": "1:00 PM"},
                "pre_workout": {"meal": "Coffee + dates (2–3)", "time": "4:30 PM"},
                "post_workout": {"meal": "3 egg whites + 1 whole egg", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer 300g + 1 roti", "time": "8:00 PM"},
                "calories": "~2700–2850 kcal",
                "protein": "~155–165g"
            }
        }
    else:  # week 4
        return {
            "level": "🔥 LEVEL 3 — ADVANCED (2600–3000 kcal)",
            "week": "WEEK 4",
            "protein_target": "155–170g",
            "Monday": {
                "early_morning": {"meal": "Lemon honey water", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + milk + banana + peanut butter + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": ("Paneer curry 200g" if food_preference == "veg" else "Chicken curry 200g") + " + 2 roti + Salad", "time": "1:00 PM"},
                "pre_workout": {"meal": "Coffee + banana", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop) + 3 egg whites", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer 300g + 1 roti", "time": "8:00 PM"},
                "calories": "~2800–2950 kcal",
                "protein": "~160–170g"
            },
            "Tuesday": {
                "early_morning": {"meal": "Coconut water", "time": "6:00 AM"},
                "breakfast": {"meal": "Poha + 2 eggs", "time": "8:00 AM"},
                "lunch": {"meal": "Rice + Dal + " + ("Paneer 150g" if food_preference == "veg" else "Chicken 150g"), "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana + dates", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop)", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 300g + veg" if food_preference == "veg" else "Fish 300g + veg"), "time": "8:00 PM"},
                "calories": "~2750–2900 kcal",
                "protein": "~160g"
            },
            "Wednesday": {
                "early_morning": {"meal": "Chia water", "time": "6:00 AM"},
                "breakfast": {"meal": "Bread omelette (3 eggs + 3 slices)", "time": "8:00 AM"},
                "lunch": {"meal": "Rajma + rice", "time": "1:00 PM"},
                "pre_workout": {"meal": "Oats shake", "time": "4:30 PM"},
                "post_workout": {"meal": "2 boiled eggs", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer grill 300g" if food_preference == "veg" else "Chicken grill 300g"), "time": "8:00 PM"},
                "calories": "~2900 kcal",
                "protein": "~160–170g"
            },
            "Thursday": {
                "early_morning": {"meal": "Warm electrolyte drink", "time": "6:00 AM"},
                "breakfast": {"meal": "Idli 3 + sambar + 2 eggs", "time": "8:00 AM"},
                "lunch": {"meal": "2 roti + Dal + veg", "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana + PB (1 tbsp)", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey (1 scoop)", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer 300g + salad", "time": "8:00 PM"},
                "calories": "~2700–2850 kcal",
                "protein": "~155–165g"
            },
            "Friday": {
                "early_morning": {"meal": "Lemon warm water", "time": "6:00 AM"},
                "breakfast": {"meal": "Sprouts bowl + 2 boiled eggs", "time": "8:00 AM"},
                "lunch": {"meal": ("Paneer biryani (1.5 cups)" if food_preference == "veg" else "Chicken biryani (1.5 cups)") + " + Curd", "time": "1:00 PM"},
                "pre_workout": {"meal": "Banana + coffee", "time": "4:30 PM"},
                "post_workout": {"meal": "3 egg whites + 1 whole egg", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 250g + 1 roti" if food_preference == "veg" else "Fish 250g + 1 roti"), "time": "8:00 PM"},
                "calories": "~2900 kcal",
                "protein": "~155–165g"
            },
            "Saturday": {
                "early_morning": {"meal": "Coconut water", "time": "6:00 AM"},
                "breakfast": {"meal": "Heavy oats bowl (oats + milk + banana + PB) + 1 boiled egg", "time": "8:00 AM"},
                "lunch": {"meal": "Dal + rice + " + ("paneer 150g" if food_preference == "veg" else "chicken 150g"), "time": "1:00 PM"},
                "pre_workout": {"meal": "Dates (3–4)", "time": "4:30 PM"},
                "post_workout": {"meal": "Whey", "time": "6:30 PM"},
                "dinner": {"meal": "Paneer 300g + veg", "time": "8:00 PM"},
                "calories": "~2700–2850 kcal",
                "protein": "~160g"
            },
            "Sunday": {
                "early_morning": {"meal": "Lemon water", "time": "6:00 AM"},
                "breakfast": {"meal": "Oats + peanut butter + banana + 2 eggs", "time": "8:00 AM"},
                "lunch": {"meal": "Chole + 2 roti", "time": "1:00 PM"},
                "pre_workout": {"meal": "Coffee + dates", "time": "4:30 PM"},
                "post_workout": {"meal": "2 whole eggs", "time": "6:30 PM"},
                "dinner": {"meal": ("Paneer 300g" if food_preference == "veg" else "Chicken 300g"), "time": "8:00 PM"},
                "calories": "~2900–3000 kcal",
                "protein": "~165g"
            }
        }

def generate_veg_diet(day, gender, calories, bmi_category):
    """Generate vegetarian diet for a specific day"""
    
    # Calculate daily calorie summary
    daily_calories = f"Daily Target: {calories} calories"
    
    # Calculate week number for consistency
    import datetime
    current_week = datetime.datetime.now().isocalendar()[1]
    week_number = ((current_week - 1) % 4) + 1
    
    # Morning hydration (consistent across all days)
    morning_hydration = {
        "meal": "Hydration & Detox",
        "details": "1 Litre Water with Chia Seeds",
        "time": "7:00 AM",
        "calories": "20-30 calories"
    }
    
    # Mid-morning snack (consistent across all days)
    mid_morning_snack = {
        "meal": "Fiber & Protein",
        "details": "1 small bowl Sprouts (Moong/Chana), handful Roasted Chana",
        "time": "11:00 AM",
        "calories": "150-200 calories"
    }
    
    # Pre-workout meal (consistent across all days)
    pre_workout = {
        "meal": "Energy Burst (30-45 min before)",
        "details": "Oats Meal: 1/2 cup White Oats (cooked with Milk/Water), 1 Banana, 1 tsp Peanut Butter, 4 Almonds, 1 tsp Honey. Hydration: 1 Litre Water + 2 Dates",
        "time": "4:30 PM",
        "calories": "350-400 calories"
    }
    
    # Immediate post-workout (consistent across all days)
    immediate_post_workout = {
        "meal": "Simple Carbs (Recovery)",
        "details": "1 glass fresh juice (Pineapple / Avocado / Anaar / Orange)",
        "time": "6:30 PM",
        "calories": "100-150 calories"
    }
    
    # Post-workout protein (consistent across all days)
    post_workout_protein = {
        "meal": "Muscle Repair",
        "details": "3 Egg Whites, 1 Whole Egg",
        "time": "7:00 PM",
        "calories": "150-200 calories"
    }
    
    # Standardized breakfast (consistent across all days)
    breakfast_options = {
        "Monday": {
            "meal": "Complex Carbs & Protein",
            "details": "2 Roti/Whole Wheat Bread, 1 bowl Veg Curry (Seasonal), 2 Boiled Eggs",
            "time": "8:30 AM",
            "calories": "400-450 calories"
        },
        "Tuesday": {
            "meal": "Complex Carbs & Protein",
            "details": "2 Roti/Whole Wheat Bread, 1 bowl Veg Curry (Seasonal), 2 Boiled Eggs",
            "time": "8:30 AM",
            "calories": "400-450 calories"
        },
        "Wednesday": {
            "meal": "Complex Carbs & Protein",
            "details": "2 Roti/Whole Wheat Bread, 1 bowl Veg Curry (Seasonal), 2 Boiled Eggs",
            "time": "8:30 AM",
            "calories": "400-450 calories"
        },
        "Thursday": {
            "meal": "Complex Carbs & Protein",
            "details": "2 Roti/Whole Wheat Bread, 1 bowl Veg Curry (Seasonal), 2 Boiled Eggs",
            "time": "8:30 AM",
            "calories": "400-450 calories"
        },
        "Friday": {
            "meal": "Complex Carbs & Protein",
            "details": "2 Roti/Whole Wheat Bread, 1 bowl Veg Curry (Seasonal), 2 Boiled Eggs",
            "time": "8:30 AM",
            "calories": "400-450 calories"
        },
        "Saturday": {
            "meal": "Complex Carbs & Protein",
            "details": "2 Roti/Whole Wheat Bread, 1 bowl Veg Curry (Seasonal), 2 Boiled Eggs",
            "time": "8:30 AM",
            "calories": "400-450 calories"
        },
        "Sunday": {
            "meal": "Complex Carbs & Protein",
            "details": "2 Roti/Whole Wheat Bread, 1 bowl Veg Curry (Seasonal), 2 Boiled Eggs",
            "time": "8:30 AM",
            "calories": "400-450 calories"
        }
    }
    
    # Standardized lunch (consistent across all days)
    lunch_options = {
        "Monday": {
            "meal": "Satiety & Veggies",
            "details": "1 medium bowl Brown/White Rice, 1 bowl Leafy Vegetable Curry (Dal), 2 Egg Whites",
            "time": "1:30 PM",
            "calories": "450-500 calories"
        },
        "Tuesday": {
            "meal": "Satiety & Veggies",
            "details": "1 medium bowl Brown/White Rice, 1 bowl Leafy Vegetable Curry (Dal), 2 Egg Whites",
            "time": "1:30 PM",
            "calories": "450-500 calories"
        },
        "Wednesday": {
            "meal": "Satiety & Veggies",
            "details": "1 medium bowl Brown/White Rice, 1 bowl Leafy Vegetable Curry (Dal), 2 Egg Whites",
            "time": "1:30 PM",
            "calories": "450-500 calories"
        },
        "Thursday": {
            "meal": "Satiety & Veggies",
            "details": "1 medium bowl Brown/White Rice, 1 bowl Leafy Vegetable Curry (Dal), 2 Egg Whites",
            "time": "1:30 PM",
            "calories": "450-500 calories"
        },
        "Friday": {
            "meal": "Satiety & Veggies",
            "details": "1 medium bowl Brown/White Rice, 1 bowl Leafy Vegetable Curry (Dal), 2 Egg Whites",
            "time": "1:30 PM",
            "calories": "450-500 calories"
        },
        "Saturday": {
            "meal": "Satiety & Veggies",
            "details": "1 medium bowl Brown/White Rice, 1 bowl Leafy Vegetable Curry (Dal), 2 Egg Whites",
            "time": "1:30 PM",
            "calories": "450-500 calories"
        },
        "Sunday": {
            "meal": "Satiety & Veggies",
            "details": "1 medium bowl Brown/White Rice, 1 bowl Leafy Vegetable Curry (Dal), 2 Egg Whites",
            "time": "1:30 PM",
            "calories": "450-500 calories"
        }
    }
    
    # Vegetarian dinner options with weekly focus (adapted for vegetarian preferences)
    if week_number == 1:  # Week 1 - Paneer Focus
        dinner_options = {
            "Monday": {
                "meal": "Paneer Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Paneer Bhurji/Sabji",
                "time": "9:00 PM",
                "calories": "500-550 calories"
            },
            "Tuesday": {
                "meal": "Paneer Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Paneer Bhurji/Sabji",
                "time": "9:00 PM",
                "calories": "500-550 calories"
            },
            "Wednesday": {
                "meal": "Paneer Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Paneer Bhurji/Sabji",
                "time": "9:00 PM",
                "calories": "500-550 calories"
            },
            "Thursday": {
                "meal": "Paneer Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Paneer Bhurji/Sabji",
                "time": "9:00 PM",
                "calories": "500-550 calories"
            },
            "Friday": {
                "meal": "Paneer Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Paneer Bhurji/Sabji",
                "time": "9:00 PM",
                "calories": "500-550 calories"
            },
            "Saturday": {
                "meal": "Paneer Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Paneer Bhurji/Sabji",
                "time": "9:00 PM",
                "calories": "500-550 calories"
            },
            "Sunday": {
                "meal": "Paneer Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Paneer Bhurji/Sabji",
                "time": "9:00 PM",
                "calories": "500-550 calories"
            }
        }
    elif week_number == 2:  # Week 2 - Tofu/Soy Focus
        dinner_options = {
            "Monday": {
                "meal": "Tofu/Soy Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Tofu Curry/Stir-fry",
                "time": "9:00 PM",
                "calories": "450-500 calories"
            },
            "Tuesday": {
                "meal": "Tofu/Soy Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Tofu Curry/Stir-fry",
                "time": "9:00 PM",
                "calories": "450-500 calories"
            },
            "Wednesday": {
                "meal": "Tofu/Soy Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Tofu Curry/Stir-fry",
                "time": "9:00 PM",
                "calories": "450-500 calories"
            },
            "Thursday": {
                "meal": "Tofu/Soy Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Tofu Curry/Stir-fry",
                "time": "9:00 PM",
                "calories": "450-500 calories"
            },
            "Friday": {
                "meal": "Tofu/Soy Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Tofu Curry/Stir-fry",
                "time": "9:00 PM",
                "calories": "450-500 calories"
            },
            "Saturday": {
                "meal": "Tofu/Soy Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Tofu Curry/Stir-fry",
                "time": "9:00 PM",
                "calories": "450-500 calories"
            },
            "Sunday": {
                "meal": "Tofu/Soy Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Tofu Curry/Stir-fry",
                "time": "9:00 PM",
                "calories": "450-500 calories"
            }
        }
    elif week_number == 3:  # Week 3 - Mixed Bean Focus
        dinner_options = {
            "Monday": {
                "meal": "Mixed Bean Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Bean Curry (Rajma/Chana/Black Beans)",
                "time": "9:00 PM",
                "calories": "450-500 calories"
            },
            "Tuesday": {
                "meal": "Mixed Bean Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Bean Curry (Rajma/Chana/Black Beans)",
                "time": "9:00 PM",
                "calories": "450-500 calories"
            },
            "Wednesday": {
                "meal": "Mixed Bean Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Bean Curry (Rajma/Chana/Black Beans)",
                "time": "9:00 PM",
                "calories": "450-500 calories"
            },
            "Thursday": {
                "meal": "Mixed Bean Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Bean Curry (Rajma/Chana/Black Beans)",
                "time": "9:00 PM",
                "calories": "450-500 calories"
            },
            "Friday": {
                "meal": "Mixed Bean Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Bean Curry (Rajma/Chana/Black Beans)",
                "time": "9:00 PM",
                "calories": "450-500 calories"
            },
            "Saturday": {
                "meal": "Mixed Bean Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Bean Curry (Rajma/Chana/Black Beans)",
                "time": "9:00 PM",
                "calories": "450-500 calories"
            },
            "Sunday": {
                "meal": "Mixed Bean Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Bean Curry (Rajma/Chana/Black Beans)",
                "time": "9:00 PM",
                "calories": "450-500 calories"
            }
        }
    else:  # Week 4 - Lentil/Dal Focus
        dinner_options = {
            "Monday": {
                "meal": "Lentil/Dal Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Dal with vegetables",
                "time": "9:00 PM",
                "calories": "400-450 calories"
            },
            "Tuesday": {
                "meal": "Lentil/Dal Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Dal with vegetables",
                "time": "9:00 PM",
                "calories": "400-450 calories"
            },
            "Wednesday": {
                "meal": "Lentil/Dal Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Dal with vegetables",
                "time": "9:00 PM",
                "calories": "400-450 calories"
            },
            "Thursday": {
                "meal": "Lentil/Dal Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Dal with vegetables",
                "time": "9:00 PM",
                "calories": "400-450 calories"
            },
            "Friday": {
                "meal": "Lentil/Dal Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Dal with vegetables",
                "time": "9:00 PM",
                "calories": "400-450 calories"
            },
            "Saturday": {
                "meal": "Lentil/Dal Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Dal with vegetables",
                "time": "9:00 PM",
                "calories": "400-450 calories"
            },
            "Sunday": {
                "meal": "Lentil/Dal Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Dal with vegetables",
                "time": "9:00 PM",
                "calories": "400-450 calories"
            }
        }
    
    # Return the complete diet plan for the day
    return {
        "morning_hydration": morning_hydration,
        "breakfast": breakfast_options[day],
        "mid_morning_snack": mid_morning_snack,
        "lunch": lunch_options[day],
        "pre_workout": pre_workout,
        "immediate_post_workout": immediate_post_workout,
        "post_workout_protein": post_workout_protein,
        "dinner": dinner_options[day],
        "daily_calories": daily_calories,
        "week_focus": f"Week {week_number} - {['Paneer', 'Tofu/Soy', 'Mixed Bean', 'Lentil/Dal'][week_number-1]} Focus"
    }

def generate_non_veg_diet(day, gender, calories, bmi_category):
    """Generate non-vegetarian diet for a specific day"""
    
    # Calculate daily calorie summary
    daily_calories = f"Daily Target: {calories} calories"
    
    # Morning hydration (consistent across all days)
    morning_hydration = {
        "meal": "Hydration & Detox",
        "details": "1 Litre Water with Chia Seeds",
        "time": "7:00 AM",
        "calories": "20-30 calories"
    }
    
    # Standardized breakfast (consistent across all days)
    breakfast_options = {
        "Monday": {
            "meal": "Complex Carbs & Protein",
            "details": "2 Roti/Whole Wheat Bread, 1 bowl Veg Curry (Seasonal), 2 Boiled Eggs",
            "time": "8:30 AM",
            "calories": "400-450 calories"
        },
        "Tuesday": {
            "meal": "Complex Carbs & Protein",
            "details": "2 Roti/Whole Wheat Bread, 1 bowl Veg Curry (Seasonal), 2 Boiled Eggs",
            "time": "8:30 AM",
            "calories": "400-450 calories"
        },
        "Wednesday": {
            "meal": "Complex Carbs & Protein",
            "details": "2 Roti/Whole Wheat Bread, 1 bowl Veg Curry (Seasonal), 2 Boiled Eggs",
            "time": "8:30 AM",
            "calories": "400-450 calories"
        },
        "Thursday": {
            "meal": "Complex Carbs & Protein",
            "details": "2 Roti/Whole Wheat Bread, 1 bowl Veg Curry (Seasonal), 2 Boiled Eggs",
            "time": "8:30 AM",
            "calories": "400-450 calories"
        },
        "Friday": {
            "meal": "Complex Carbs & Protein",
            "details": "2 Roti/Whole Wheat Bread, 1 bowl Veg Curry (Seasonal), 2 Boiled Eggs",
            "time": "8:30 AM",
            "calories": "400-450 calories"
        },
        "Saturday": {
            "meal": "Complex Carbs & Protein",
            "details": "2 Roti/Whole Wheat Bread, 1 bowl Veg Curry (Seasonal), 2 Boiled Eggs",
            "time": "8:30 AM",
            "calories": "400-450 calories"
        },
        "Sunday": {
            "meal": "Complex Carbs & Protein",
            "details": "2 Roti/Whole Wheat Bread, 1 bowl Veg Curry (Seasonal), 2 Boiled Eggs",
            "time": "8:30 AM",
            "calories": "400-450 calories"
        }
    }
    
    # Mid-morning snack (consistent across all days)
    mid_morning_snack = {
        "meal": "Fiber & Protein",
        "details": "1 small bowl Sprouts (Moong/Chana), handful Roasted Chana",
        "time": "11:00 AM",
        "calories": "150-200 calories"
    }
    
    # Standardized lunch (consistent across all days)
    lunch_options = {
        "Monday": {
            "meal": "Satiety & Veggies",
            "details": "1 medium bowl Brown/White Rice, 1 bowl Leafy Vegetable Curry (Dal), 2 Egg Whites",
            "time": "1:30 PM",
            "calories": "450-500 calories"
        },
        "Tuesday": {
            "meal": "Satiety & Veggies",
            "details": "1 medium bowl Brown/White Rice, 1 bowl Leafy Vegetable Curry (Dal), 2 Egg Whites",
            "time": "1:30 PM",
            "calories": "450-500 calories"
        },
        "Wednesday": {
            "meal": "Satiety & Veggies",
            "details": "1 medium bowl Brown/White Rice, 1 bowl Leafy Vegetable Curry (Dal), 2 Egg Whites",
            "time": "1:30 PM",
            "calories": "450-500 calories"
        },
        "Thursday": {
            "meal": "Satiety & Veggies",
            "details": "1 medium bowl Brown/White Rice, 1 bowl Leafy Vegetable Curry (Dal), 2 Egg Whites",
            "time": "1:30 PM",
            "calories": "450-500 calories"
        },
        "Friday": {
            "meal": "Satiety & Veggies",
            "details": "1 medium bowl Brown/White Rice, 1 bowl Leafy Vegetable Curry (Dal), 2 Egg Whites",
            "time": "1:30 PM",
            "calories": "450-500 calories"
        },
        "Saturday": {
            "meal": "Satiety & Veggies",
            "details": "1 medium bowl Brown/White Rice, 1 bowl Leafy Vegetable Curry (Dal), 2 Egg Whites",
            "time": "1:30 PM",
            "calories": "450-500 calories"
        },
        "Sunday": {
            "meal": "Satiety & Veggies",
            "details": "1 medium bowl Brown/White Rice, 1 bowl Leafy Vegetable Curry (Dal), 2 Egg Whites",
            "time": "1:30 PM",
            "calories": "450-500 calories"
        }
    }
    
    # Pre-workout meal (consistent across all days)
    pre_workout = {
        "meal": "Energy Burst (30-45 min before)",
        "details": "Oats Meal: 1/2 cup White Oats (cooked with Milk/Water), 1 Banana, 1 tsp Peanut Butter, 4 Almonds, 1 tsp Honey. Hydration: 1 Litre Water + 2 Dates",
        "time": "4:30 PM",
        "calories": "350-400 calories"
    }
    
    # Immediate post-workout (consistent across all days)
    immediate_post_workout = {
        "meal": "Simple Carbs (Recovery)",
        "details": "1 glass fresh juice (Pineapple / Avocado / Anaar / Orange)",
        "time": "6:30 PM",
        "calories": "100-150 calories"
    }
    
    # Post-workout protein (consistent across all days)
    post_workout_protein = {
        "meal": "Muscle Repair",
        "details": "3 Egg Whites, 1 Whole Egg",
        "time": "7:00 PM",
        "calories": "150-200 calories"
    }
    
    # Calculate week number based on a rotating 4-week cycle
    import datetime
    current_week = datetime.datetime.now().isocalendar()[1]
    week_number = ((current_week - 1) % 4) + 1  # Cycles through weeks 1-4
    
    # Base dinner structure for all days
    dinner_base = {
        "meal": "2 Roti/Whole Wheat Bread + Protein Focus",
        "calories": "500-600 calories"
    }
    
    # Week-specific protein focus
    if week_number == 1:  # Week 1 - Chicken Focus
        dinner_options = {
            "Monday": {
                "meal": "Chicken Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Chicken Curry/Stew",
                "calories": "550-600 calories"
            },
            "Tuesday": {
                "meal": "Chicken Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Chicken Curry/Stew",
                "calories": "550-600 calories"
            },
            "Wednesday": {
                "meal": "Chicken Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Chicken Curry/Stew",
                "calories": "550-600 calories"
            },
            "Thursday": {
                "meal": "Chicken Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Chicken Curry/Stew",
                "calories": "550-600 calories"
            },
            "Friday": {
                "meal": "Chicken Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Chicken Curry/Stew",
                "calories": "550-600 calories"
            },
            "Saturday": {
                "meal": "Chicken Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Chicken Curry/Stew",
                "calories": "550-600 calories"
            },
            "Sunday": {
                "meal": "Chicken Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Chicken Curry/Stew",
                "calories": "550-600 calories"
            }
        }
    elif week_number == 2:  # Week 2 - Paneer Focus
        dinner_options = {
            "Monday": {
                "meal": "Paneer Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Paneer Bhurji/Sabji",
                "calories": "500-550 calories"
            },
            "Tuesday": {
                "meal": "Paneer Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Paneer Bhurji/Sabji",
                "calories": "500-550 calories"
            },
            "Wednesday": {
                "meal": "Paneer Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Paneer Bhurji/Sabji",
                "calories": "500-550 calories"
            },
            "Thursday": {
                "meal": "Paneer Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Paneer Bhurji/Sabji",
                "calories": "500-550 calories"
            },
            "Friday": {
                "meal": "Paneer Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Paneer Bhurji/Sabji",
                "calories": "500-550 calories"
            },
            "Saturday": {
                "meal": "Paneer Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Paneer Bhurji/Sabji",
                "calories": "500-550 calories"
            },
            "Sunday": {
                "meal": "Paneer Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 250g Paneer Bhurji/Sabji",
                "calories": "500-550 calories"
            }
        }
    elif week_number == 3:  # Week 3 - Fish Focus
        dinner_options = {
            "Monday": {
                "meal": "Fish Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 200g Fish Curry/Grilled",
                "calories": "500-550 calories"
            },
            "Tuesday": {
                "meal": "Fish Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 200g Fish Curry/Grilled",
                "calories": "500-550 calories"
            },
            "Wednesday": {
                "meal": "Fish Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 200g Fish Curry/Grilled",
                "calories": "500-550 calories"
            },
            "Thursday": {
                "meal": "Fish Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 200g Fish Curry/Grilled",
                "calories": "500-550 calories"
            },
            "Friday": {
                "meal": "Fish Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 200g Fish Curry/Grilled",
                "calories": "500-550 calories"
            },
            "Saturday": {
                "meal": "Fish Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 200g Fish Curry/Grilled",
                "calories": "500-550 calories"
            },
            "Sunday": {
                "meal": "Fish Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 200g Fish Curry/Grilled",
                "calories": "500-550 calories"
            }
        }
    else:  # Week 4 - Mutton/Red Meat or Lentil Focus
        dinner_options = {
            "Monday": {
                "meal": "Mutton/Red Meat Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 200g Mutton Curry/Stew (Only 1-2 times this week) OR Lentil/Dal Focus",
                "calories": "550-600 calories"
            },
            "Tuesday": {
                "meal": "Lentil/Dal Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Dal with vegetables",
                "calories": "450-500 calories"
            },
            "Wednesday": {
                "meal": "Lentil/Dal Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Dal with vegetables",
                "calories": "450-500 calories"
            },
            "Thursday": {
                "meal": "Mutton/Red Meat Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, 200g Mutton Curry/Stew (Only 1-2 times this week) OR Lentil/Dal Focus",
                "calories": "550-600 calories"
            },
            "Friday": {
                "meal": "Lentil/Dal Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Dal with vegetables",
                "calories": "450-500 calories"
            },
            "Saturday": {
                "meal": "Lentil/Dal Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Dal with vegetables",
                "calories": "450-500 calories"
            },
            "Sunday": {
                "meal": "Lentil/Dal Focus Dinner",
                "details": "2 Roti/Whole Wheat Bread, Mixed Dal with vegetables",
                "calories": "450-500 calories"
            }
        }
    
    # Add complete meal schedule for context
    meal_schedule = {
        "Morning (7:00 AM)": "1 Litre Water with Chia Seeds - Hydration & Detox",
        "Breakfast (8:30 AM)": "2 Roti/Whole Wheat Bread, 1 bowl Veg Curry (Seasonal), 2 Boiled Eggs - Complex Carbs & Protein",
        "Mid-Morning Snack (11:00 AM)": "1 small bowl Sprouts (Moong/Chana), handful Roasted Chana - Fiber & Protein",
        "Lunch (1:30 PM)": "1 medium bowl Brown/White Rice, 1 bowl Leafy Vegetable Curry (Dal), 2 Egg Whites - Satiety & Veggies",
        "Pre-Workout (4:30 PM)": "Oats Meal: 1/2 cup White Oats (cooked with Milk/Water), 1 Banana, 1 tsp Peanut Butter, 4 Almonds, 1 tsp Honey. Hydration: 1 Litre Water + 2 Dates - Energy Burst (30-45 min before)",
        "Immediate Post-Workout (6:30 PM)": "1 glass fresh juice (Pineapple / Avocado / Anaar / Orange) - Simple Carbs (Recovery)",
        "Post-Workout Protein (7:00 PM)": "3 Egg Whites, 1 Whole Egg - Muscle Repair",
        "Dinner (9:00 PM)": "Protein & Fiber focus as per weekly rotation"
    }
    
    # Return the complete diet plan for the day
    return {
        "morning_hydration": morning_hydration,
        "breakfast": breakfast_options[day],
        "mid_morning_snack": mid_morning_snack,
        "lunch": lunch_options[day],
        "pre_workout": pre_workout,
        "immediate_post_workout": immediate_post_workout,
        "post_workout_protein": post_workout_protein,
        "dinner": dinner_options[day],
        "daily_calories": daily_calories,
        "week_focus": f"Week {week_number} - {['Chicken', 'Paneer', 'Fish', 'Mutton/Lentil'][week_number-1]} Focus"
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
