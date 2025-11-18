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
        "snacks": snacks,
        "daily_calories": daily_calories
    }

def generate_non_veg_diet(day, gender, calories, bmi_category):
    """Generate non-vegetarian diet for a specific day"""
    
    # Calculate daily calorie summary
    daily_calories = f"Daily Target: {calories} calories"
    
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
        "snacks": snacks,
        "daily_calories": daily_calories
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
