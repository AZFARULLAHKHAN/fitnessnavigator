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

def get_exercise_video_url(name):
    video_map = {
        # Push variations
        "Push-ups": "https://youtu.be/mECzqUIDWfU?si=lj2k_FLbfe2iuBVD",  
        "Diamond Push-ups": "https://www.youtube.com/embed/dYhQ05pUB0A?si=aRM1Idmspq3tauME",  
        "Pike Push-ups": "https://www.youtube.com/embed/XckEEwa1BPI?si=d-Tny65kI-Pc5PeY",  # Calisthenicmovement
        "Dips": "https://www.youtube.com/embed/rZl4D4p_nO4?si=EKkImmMjUla85XYD",  # Calisthenicmovement
        "Wall Push-ups": "https://www.youtube.com/embed/EOf3cGIQpA4?si=0ymERtKh0TBii--y",  # HASfit
        "Modified Push-ups": "https://www.youtube.com/embed/GnjOtan1wZ0?si=VxecbT1cxZeInUMh",  # HASfit
        "Push-ups (regular or modified)": "https://www.youtube.com/embed/WDIpL0pjun0?si=gYvrtr1JQHoTXNsk",  # MadFit
        "Clap Push-ups": "https://www.youtube.com/embed/EYwWCgM198U?si=SyXGdfTyN_REN8Fn",  # Calisthenicmovement
        "Explosive Push-ups": "https://www.youtube.com/embed/_ICD84Bde4M?si=ZJp5KYNZGFbfQ4HP",  # MadFit

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
        "Leg Raises": "https://www.youtube.com/embed/JB2oyawG9KI?si=5OlWnikPKrrXZxpV",  # Bowflex

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
        # Easy intensity workouts
        if intensity == "easy":
            workout_plans = {
                "male": {
                    "Monday": {
                        "focus": "Full Body",
                        "exercises": [
                            {"name": "Walking", "details": "20 minutes at moderate pace"},
                            {"name": "Bodyweight Squats", "details": "2 sets of 10 reps"},
                            {"name": "Wall Push-ups", "details": "2 sets of 8 reps"},
                            {"name": "Standing Side Leg Raises", "details": "2 sets of 10 each side"}
                        ],
                        "notes": "Focus on proper form and breathing. Rest as needed between exercises."
                    },
                    "Tuesday": {
                        "focus": "Walking & Stretching",
                        "exercises": [
                            {"name": "Brisk Walking", "details": "25 minutes"},
                            {"name": "Standing Side Bends", "details": "2 sets of 10 each side"},
                            {"name": "Shoulder Rolls", "details": "2 sets of 10 forward and backward"}
                        ],
                        "notes": "Take deep breaths during stretches and hold each position for 15-20 seconds."
                    },
                    "Wednesday": {
                        "focus": "Upper Body",
                        "exercises": [
                            {"name": "Push-ups", "details": "3 sets of 12 reps"},
                            {"name": "Diamond Push-ups", "details": "2 sets of 10 reps"},
                            {"name": "Pike Push-ups", "details": "2 sets of 8 reps"},
                            {"name": "Dips", "details": "3 sets of 10 reps"}
                        ],
                        "notes": "Rest 60-90 seconds between sets. Focus on controlled movements."
                    },
                    "Thursday": {
                        "focus": "Active Recovery",
                        "exercises": [
                            {"name": "Yoga", "details": "Beginner's yoga routine, 15-20 minutes"},
                            {"name": "Stretching", "details": "Full body stretching, 10 minutes"}
                        ],
                        "notes": "Focus on flexibility and recovery."
                    },
                    "Friday": {
                        "focus": "Full Body",
                        "exercises": [
                            {"name": "Push-ups", "details": "2 sets of 8-10 reps"},
                            {"name": "Bodyweight Squats", "details": "2 sets of 12 reps"},
                            {"name": "Planks", "details": "2 sets of 20-30 seconds"},
                            {"name": "Walking Lunges", "details": "2 sets of 10 steps per leg"}
                        ],
                        "notes": "Perform exercises as a circuit with minimal rest between exercises."
                    },
                    "Saturday": {
                        "focus": "Cardio & Core",
                        "exercises": [
                            {"name": "Brisk Walking or Light Jogging", "details": "20 minutes"},
                            {"name": "Bicycle Crunches", "details": "2 sets of 10 reps per side"},
                            {"name": "Planks", "details": "2 sets of 20-30 seconds"}
                        ],
                        "notes": "Focus on maintaining good form throughout."
                    }
                },
                "female": {
                    "Monday": {
                        "focus": "Full Body",
                        "exercises": [
                            {"name": "Walking", "details": "20 minutes at moderate pace"},
                            {"name": "Modified Push-ups", "details": "2 sets of 8 reps"},
                            {"name": "Bodyweight Squats", "details": "2 sets of 10 reps"},
                            {"name": "Standing Side Leg Raises", "details": "2 sets of 10 each side"}
                        ],
                        "notes": "Remember to maintain proper form throughout the exercises."
                    },
                    "Tuesday": {
                        "focus": "Walking & Stretching",
                        "exercises": [
                            {"name": "Brisk Walking", "details": "25 minutes"},
                            {"name": "Standing Side Bends", "details": "2 sets of 10 each side"},
                            {"name": "Shoulder Rolls", "details": "2 sets of 10 forward and backward"}
                        ],
                        "notes": "Take deep breaths during stretches and hold each position for 15-20 seconds."
                    },
                    "Wednesday": {
                        "focus": "Upper Body",
                        "exercises": [
                            {"name": "Push-ups (regular or modified)", "details": "3 sets of 12 reps"},
                            {"name": "Dumbbell Rows", "details": "3 sets of 12 reps per arm"},
                            {"name": "Tricep Dips", "details": "3 sets of 8-10 reps"},
                            {"name": "Planks", "details": "3 sets of 20-30 seconds"}
                        ],
                        "notes": "Use light weights or household items if dumbbells are not available."
                    },
                    "Thursday": {
                        "focus": "Active Recovery",
                        "exercises": [
                            {"name": "Yoga", "details": "Beginner's yoga routine, 15-20 minutes"},
                            {"name": "Stretching", "details": "Full body stretching, 10 minutes"}
                        ],
                        "notes": "Focus on flexibility and recovery."
                    },
                    "Friday": {
                        "focus": "Full Body",
                        "exercises": [
                            {"name": "Circuit Training", "details": "3 rounds of: 12 squats, 10 push-ups, 12 lunges per leg, 10 dumbbell rows per arm, 30-second plank"},
                            {"name": "Burpees", "details": "3 sets of 10 reps"}
                        ],
                        "notes": "Perform the circuit with minimal rest between exercises, rest 1-2 minutes between rounds."
                    },
                    "Saturday": {
                        "focus": "Cardio & Mobility",
                        "exercises": [
                            {"name": "Brisk Walking", "details": "20 minutes"},
                            {"name": "Arm Circles", "details": "2 sets of 10 in each direction"},
                            {"name": "Hip Circles", "details": "2 sets of 10 in each direction"},
                            {"name": "Cat-Cow Stretch", "details": "10 repetitions"}
                        ],
                        "notes": "Focus on loosening tight areas and improving mobility."
                    }
                }
            }
        # Intermediate intensity workouts
        elif intensity == "intermediate":
            workout_plans = {
                "male": {
                    "Monday": {
                        "focus": "Chest & Triceps",
                        "exercises": [
                            {"name": "Push-ups", "details": "3 sets of 12 reps"},
                            {"name": "Diamond Push-ups", "details": "2 sets of 10 reps"},
                            {"name": "Pike Push-ups", "details": "2 sets of 8 reps"},
                            {"name": "Dips", "details": "3 sets of 10 reps"}
                        ],
                        "notes": "Rest 60-90 seconds between sets. Focus on controlled movements."
                    },
                    "Tuesday": {
                        "focus": "Cardio & Core",
                        "exercises": [
                            {"name": "Jogging or Cycling", "details": "25 minutes"},
                            {"name": "Planks", "details": "3 sets of 40-60 seconds"},
                            {"name": "Russian Twists", "details": "3 sets of 15 reps per side"},
                            {"name": "Mountain Climbers", "details": "3 sets of 20 reps per leg"}
                        ],
                        "notes": "Maintain moderate intensity throughout your cardio session."
                    },
                    "Wednesday": {
                        "focus": "Back & Biceps",
                        "exercises": [
                            {"name": "Dumbbell Rows", "details": "3 sets of 12 reps per arm"},
                            {"name": "Superman Holds", "details": "3 sets of 30 seconds"},
                            {"name": "Bicep Curls", "details": "3 sets of 12 reps"},
                            {"name": "Hammer Curls", "details": "3 sets of 12 reps"}
                        ],
                        "notes": "Use challenging weights but maintain proper form."
                    },
                    "Thursday": {
                        "focus": "HIIT & Mobility",
                        "exercises": [
                            {"name": "HIIT Circuit", "details": "30 seconds work, 30 seconds rest for 15 minutes (Jumping jacks, Mountain climbers, High knees, Burpees)"},
                            {"name": "Foam Rolling", "details": "10 minutes focusing on tight areas"},
                            {"name": "Dynamic Stretching", "details": "5-10 minutes"}
                        ],
                        "notes": "Push yourself during the work intervals, fully recover during rest periods."
                    },
                    "Friday": {
                        "focus": "Legs & Shoulders",
                        "exercises": [
                            {"name": "Bodyweight Squats", "details": "3 sets of 15 reps"},
                            {"name": "Walking Lunges", "details": "3 sets of 12 reps per leg"},
                            {"name": "Shoulder Press", "details": "3 sets of 12 reps"},
                            {"name": "Lateral Raises", "details": "3 sets of 12 reps"}
                        ],
                        "notes": "Focus on form and controlled movements."
                    },
                    "Saturday": {
                        "focus": "Full Body & Cardio",
                        "exercises": [
                            {"name": "Circuit Training", "details": "3 rounds of: 15 push-ups, 15 bodyweight squats, 15 dumbbell rows, 15 lunges, 30-second plank"},
                            {"name": "Brisk Walking or Jogging", "details": "15 minutes"}
                        ],
                        "notes": "Perform the circuit with minimal rest between exercises, rest 1-2 minutes between rounds."
                    }
                },
                "female": {
                    "Monday": {
                        "focus": "Lower Body",
                        "exercises": [
                            {"name": "Bodyweight Squats", "details": "3 sets of 15 reps"},
                            {"name": "Lunges", "details": "3 sets of 12 reps per leg"},
                            {"name": "Glute Bridges", "details": "3 sets of 15 reps"},
                            {"name": "Calf Raises", "details": "3 sets of 15 reps"}
                        ],
                        "notes": "Focus on form and controlled movements."
                    },
                    "Tuesday": {
                        "focus": "Cardio & Core",
                        "exercises": [
                            {"name": "Jogging, Cycling, or Dance", "details": "25 minutes"},
                            {"name": "Planks", "details": "3 sets of 40-60 seconds"},
                            {"name": "Bicycle Crunches", "details": "3 sets of 15 reps per side"},
                            {"name": "Leg Raises", "details": "3 sets of 12 reps"}
                        ],
                        "notes": "Maintain moderate intensity throughout your cardio session."
                    },
                    "Wednesday": {
                        "focus": "Upper Body",
                        "exercises": [
                            {"name": "Push-ups (regular or modified)", "details": "3 sets of 12 reps"},
                            {"name": "Dumbbell Rows", "details": "3 sets of 12 reps per arm"},
                            {"name": "Tricep Dips", "details": "3 sets of 12 reps"},
                            {"name": "Shoulder Press", "details": "3 sets of 12 reps"}
                        ],
                        "notes": "Use challenging weights but maintain proper form."
                    },
                    "Thursday": {
                        "focus": "HIIT & Flexibility",
                        "exercises": [
                            {"name": "HIIT Circuit", "details": "30 seconds work, 30 seconds rest for 15 minutes (Jumping jacks, Squat jumps, Mountain climbers, High knees)"},
                            {"name": "Yoga Flow", "details": "15 minutes focusing on flexibility"}
                        ],
                        "notes": "Push yourself during the work intervals, fully recover during rest periods."
                    },
                    "Friday": {
                        "focus": "Full Body",
                        "exercises": [
                            {"name": "Circuit Training", "details": "3 rounds of: 12 squats, 10 push-ups, 12 lunges per leg, 10 dumbbell rows per arm, 30-second plank"}
                        ],
                        "notes": "Perform the circuit with minimal rest between exercises, rest 1-2 minutes between rounds."
                    },
                    "Saturday": {
                        "focus": "Cardio & Toning",
                        "exercises": [
                            {"name": "Brisk Walking, Jogging, or Dancing", "details": "20 minutes"},
                            {"name": "Bodyweight Squats", "details": "3 sets of 15 reps"},
                            {"name": "Glute Kickbacks", "details": "3 sets of 12 reps per leg"},
                            {"name": "Arm Circles", "details": "3 sets of 15 in each direction"}
                        ],
                        "notes": "Focus on engaging muscles throughout all movements."
                    }
                }
            }
        # Hardcore intensity workouts
        else:  # hardcore
            workout_plans = {
                "male": {
                    "Monday": {
                        "focus": "Chest & Triceps",
                        "exercises": [
                            {"name": "Explosive Push-ups", "details": "4 sets of 15 reps"},
                            {"name": "Clap Push-ups", "details": "3 sets of 10 reps"},
                            {"name": "Diamond Push-ups", "details": "4 sets of 12 reps"},
                            {"name": "Tricep Dips", "details": "4 sets of 15 reps"}
                        ],
                        "notes": "Perform exercises with explosive power while maintaining proper form."
                    },
                    "Tuesday": {
                        "focus": "HIIT Cardio",
                        "exercises": [
                            {"name": "HIIT Circuit", "details": "45 seconds work, 15 seconds rest for 20 minutes"},
                            {"name": "Burpees", "details": "4 sets of 15 reps"},
                            {"name": "Mountain Climbers", "details": "4 sets of 30 reps per leg"},
                            {"name": "Squat Jumps", "details": "4 sets of 20 reps"}
                        ],
                        "notes": "Push yourself to maximum intensity during work intervals."
                    },
                    "Wednesday": {
                        "focus": "Back & Biceps",
                        "exercises": [
                            {"name": "Dumbbell Rows", "details": "4 sets of 15 reps per arm"},
                            {"name": "Superman Holds", "details": "4 sets of 45 seconds"},
                            {"name": "Bicep Curls", "details": "4 sets of 15 reps"},
                            {"name": "Hammer Curls", "details": "4 sets of 15 reps"}
                        ],
                        "notes": "Use heavy weights with perfect form."
                    },
                    "Thursday": {
                        "focus": "Legs & Core",
                        "exercises": [
                            {"name": "Bodyweight Squats", "details": "4 sets of 25 reps"},
                            {"name": "Walking Lunges", "details": "4 sets of 20 reps per leg"},
                            {"name": "Planks", "details": "4 sets of 60-90 seconds"},
                            {"name": "Russian Twists", "details": "4 sets of 25 reps per side"}
                        ],
                        "notes": "Focus on explosive movements and core stability."
                    },
                    "Friday": {
                        "focus": "Full Body Circuit",
                        "exercises": [
                            {"name": "Circuit Training", "details": "5 rounds of: 20 push-ups, 20 squats, 20 burpees, 20 mountain climbers"},
                            {"name": "Planks", "details": "3 sets of 60 seconds"}
                        ],
                        "notes": "Minimal rest between exercises, 2 minutes between rounds."
                    },
                    "Saturday": {
                        "focus": "Strength & Power",
                        "exercises": [
                            {"name": "Explosive Push-ups", "details": "4 sets of 12 reps"},
                            {"name": "Squat Jumps", "details": "4 sets of 15 reps"},
                            {"name": "Dumbbell Rows", "details": "4 sets of 12 reps per arm"},
                            {"name": "Burpees", "details": "4 sets of 10 reps"}
                        ],
                        "notes": "Focus on power and explosive movements."
                    }
                },
                "female": {
                    "Monday": {
                        "focus": "Lower Body Power",
                        "exercises": [
                            {"name": "Squat Jumps", "details": "4 sets of 15 reps"},
                            {"name": "Lunges", "details": "4 sets of 15 reps per leg"},
                            {"name": "Glute Bridges", "details": "4 sets of 20 reps"},
                            {"name": "Calf Raises", "details": "4 sets of 20 reps"}
                        ],
                        "notes": "Focus on explosive power in lower body movements."
                    },
                    "Tuesday": {
                        "focus": "HIIT Cardio",
                        "exercises": [
                            {"name": "HIIT Circuit", "details": "45 seconds work, 15 seconds rest for 20 minutes"},
                            {"name": "Burpees", "details": "4 sets of 12 reps"},
                            {"name": "Mountain Climbers", "details": "4 sets of 25 reps per leg"},
                            {"name": "High knees", "details": "4 sets of 30 seconds"}
                        ],
                        "notes": "Push yourself to maximum intensity during work intervals."
                    },
                    "Wednesday": {
                        "focus": "Upper Body Strength",
                        "exercises": [
                            {"name": "Push-ups", "details": "4 sets of 15 reps"},
                            {"name": "Dumbbell Rows", "details": "4 sets of 15 reps per arm"},
                            {"name": "Tricep Dips", "details": "4 sets of 15 reps"},
                            {"name": "Shoulder Press", "details": "4 sets of 15 reps"}
                        ],
                        "notes": "Use challenging weights while maintaining perfect form."
                    },
                    "Thursday": {
                        "focus": "Core & Stability",
                        "exercises": [
                            {"name": "Planks", "details": "4 sets of 60-90 seconds"},
                            {"name": "Bicycle Crunches", "details": "4 sets of 25 reps per side"},
                            {"name": "Russian Twists", "details": "4 sets of 25 reps per side"},
                            {"name": "Leg Raises", "details": "4 sets of 15 reps"}
                        ],
                        "notes": "Focus on core stability and controlled movements."
                    },
                    "Friday": {
                        "focus": "Full Body Circuit",
                        "exercises": [
                            {"name": "Circuit Training", "details": "4 rounds of: 15 push-ups, 20 squats, 15 burpees, 20 lunges per leg, 45-second plank"}
                        ],
                        "notes": "Minimal rest between exercises, 90 seconds between rounds."
                    },
                    "Saturday": {
                        "focus": "Power & Conditioning",
                        "exercises": [
                            {"name": "Squat Jumps", "details": "4 sets of 15 reps"},
                            {"name": "Push-ups", "details": "4 sets of 12 reps"},
                            {"name": "Burpees", "details": "4 sets of 10 reps"},
                            {"name": "Mountain Climbers", "details": "4 sets of 30 reps per leg"}
                        ],
                        "notes": "Focus on explosive power and cardiovascular conditioning."
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
    
    return workout
