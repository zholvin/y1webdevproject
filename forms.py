from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField, SelectField, IntegerField, RadioField, SelectField, BooleanField, FloatField
from wtforms.validators import InputRequired, EqualTo, NumberRange

class RegistrationForm(FlaskForm):
    user_type = SelectField("Account:",choices=["Guest","Admin"],default="Guest")
    user_id = StringField("User id:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    password2 = PasswordField("Repeat password:", validators=[InputRequired(),EqualTo("password")])
    admin_code = StringField("Admin code:")
    submit = SubmitField("Submit")
    secret = StringField("Answer:", validators=[InputRequired()])
    
class LoginForm(FlaskForm):
    user_type = SelectField("Account:",choices=["Guest","Admin"],default="Guest")
    user_id = StringField("User id:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    submit = SubmitField("Submit")
    
class ResetForm(FlaskForm):
    user_type = SelectField("Account:",choices=["Guest","Admin"],default="Guest")
    user_id = StringField("User id:", validators=[InputRequired()])
    password = PasswordField("New password:", validators=[InputRequired()])
    secret = StringField("Answer:", validators=[InputRequired()])
    submit = SubmitField("Reset")
    
class ProfileForm(FlaskForm):
    user_id = StringField("User id:")
    name = StringField("Name:",validators=[InputRequired()])
    gender = SelectField("Gender:", 
        choices=("Male","Female"))
    age = StringField("Age:")
    weight = DecimalField("Weight in kg:",
        validators = [InputRequired(),NumberRange(1,233)])
    height = DecimalField("Height in m:",
        validators = [InputRequired(),NumberRange(0.1,2.33)])
    bmi = DecimalField("BMI:")
    bmi_category = StringField("BMI Category:")
    submit = SubmitField("Update")
    energy_MJ = DecimalField()
    energy_kcal = DecimalField()
    protein = DecimalField()
    fat = DecimalField()
    carbohydrate = DecimalField()
    free_sugars = DecimalField()
    salt = DecimalField()
    fibre = DecimalField()
    
class NutritionForm(FlaskForm):
    food_name = StringField("Food name:")
    food_type = SelectField("Food type:",
                            choices=["Not selected","Fruit","Meat","Vegetable",
                                     "Seafood","Legume"],
                            default="Not selected")
    submit = SubmitField("Enquiry")
    
class FoodsForm(FlaskForm):
    food_name = StringField("Food name:")
    food_type = SelectField("Food type:",
                            choices=["Not selected","Fruit","Meat","Vegetable",
                                     "Seafood","Legume"],
                            default="Not selected")
    view_type = SelectField(choices=["Overview","Detail"])
    submit = SubmitField("Enquiry")
    exchange = SubmitField("Exchange")
    search = SubmitField("Search")
    
class BmiEnquiryForm(FlaskForm):
    weight = DecimalField("Weight in kg:",
        validators = [InputRequired(),NumberRange(1,233)])
    height = DecimalField("Height in m:",
        validators = [InputRequired(),NumberRange(0.1,2.33)])
    bmi = StringField("BMI:")
    result = StringField("Your category:")  
    submit = SubmitField("Enquiry")
    save = SubmitField("Save to User Profile")
        
class Age_RecommendForm(FlaskForm):
    gender = SelectField("Gender:",
                        choices=["Male","Female","Both"],
                        default="Both")
    age = StringField("Age:")
    submit = SubmitField("Submit")
    save = SubmitField("Save recommendation")

class DraftForm(FlaskForm):
    submit = SubmitField("submit")
    
class RecordDesignForm(FlaskForm):
    food_id = IntegerField("Food id:",
                           validators=[NumberRange(1,10000)])
    meal_time = SelectField("Meal time:",
                            choices=["Morning","Afternoon","Evening","Not Select"])
    enquiry = SubmitField("enquiry")
    delete = SubmitField("delete")
    update = SubmitField("update")
    
class FoodNotListForm(FlaskForm):
    food_name = StringField(validators = [InputRequired()])
    food_type = SelectField("Food Type",
                            choices=["Not selected","Fruit","Meat","Vegetable",
                                     "Seafood","Legume"])
    guest_description = StringField("Description",validators = [InputRequired()])
    submit = SubmitField()
    
class AddNewFoodForm(FlaskForm):
    food_name = StringField(validators = [InputRequired()])
    food_type = SelectField("Food Type",
                            choices=["Fruit","Meat","Vegetable",
                                     "Seafood","Legume"])
    status = SelectField(choices=["Unfinished","Finish","Give Up"])
    update = SubmitField()
    submit= SubmitField()
    
class ChangeForm(FlaskForm):
    food_name = StringField(validators = [InputRequired()])
    food_type = SelectField("Food Type",
                            choices=["Fruit","Meat","Vegetable",
                                     "Seafood","Legume"])
    url = StringField()
    energy = FloatField()
    protein = FloatField()
    carbohydrate = FloatField()
    dietaryFiber = FloatField()
    fat = FloatField()
    vitamin_a = FloatField()
    vitamin_b = FloatField()
    vitamin_c = FloatField()
    vitamin_d = FloatField()
    trace_minerals = FloatField()
    gi = FloatField()
    gl = FloatField()
    update = SubmitField()