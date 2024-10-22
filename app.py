"""
My system has two kinds of user: 
regular ones, and administrators.


Choose Register on the main page in order to register as a regular user or an admin user.
But to register an administrator, the Admin code is [SuperCode]

The db already has a guest: {guest id: admin, password: admin}
and one administrator: {admin id: admin, password: admin}
"""

from flask import Flask, render_template, session, redirect, url_for, g, request
from database import get_db, close_db
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm, RecordDesignForm,DraftForm,Age_RecommendForm, ProfileForm, BmiEnquiryForm, ResetForm, NutritionForm,FoodsForm,FoodNotListForm,AddNewFoodForm,ChangeForm
from functools import wraps
from jinja2 import Environment, FileSystemLoader #zip new learn
import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.teardown_appcontext(close_db)

def do_zip(*args): #zip new learn
    return zip(*args)

app.jinja_env.filters['zip'] = do_zip #zip new learn

@app.before_request
def logged_in_user():
    g.user_type = session.get("user_type",None)
    g.user_id = session.get("user_id", None)
    g.admin_id = session.get("admin_id", None)

def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user_type is None:
            return redirect(url_for("login", next=request.url))
        return view(*args, **kwargs)
    return wrapped_view

@app.route("/")
def index():
    account_id = ""
    if g.user_id:
        account_id = session["user_id"]
    if g.admin_id:
        account_id = session["admin_id"]
    return render_template("index.html",title = "Nutrition Enquiry - Home", account_id = account_id)

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    db = get_db()
    if form.validate_on_submit():
        user_type = form.user_type.data
        user_id = form.user_id.data
        admin_id = form.user_id.data
        password = form.password.data
        password2 = form.password2.data
        valid_code = "SuperCode"
        admin_code = form.admin_code.data
        secret = form.secret.data
        if user_type == "Guest":
            possible_clashing_user = db. execute("""SELECT * FROM users WHERE user_id =?;""",(user_id,)).fetchone()
            if possible_clashing_user is not None:
                form.user_id.errors.append("User id already taken!")
            else:
                db.execute("""INSERT INTO users (user_id, password, secret)
                        VALUES (?,?,?);""",
                        (user_id, generate_password_hash(password), secret))
                db.execute("""INSERT INTO user_profiles (user_id)
                        VALUES (?);""",(user_id,))
                db.commit()
                return redirect ( url_for("login") )
        else:
            possible_clashing_admin = db. execute("""SELECT * FROM admins WHERE admin_id =?;""",(admin_id,)).fetchone()
            if possible_clashing_admin is not None:
                form.user_id.errors.append("Admin id already taken!")
            else:
                if len(admin_code) == 0:
                    form.admin_code.errors.append("Please enter the code!")
                else:
                    if valid_code != admin_code:
                        form.admin_code.errors.append("Code is not correct!")
                    else:
                        db.execute("""INSERT INTO admins (admin_id, password, secret)
                                VALUES (?,?,?);""",(admin_id, generate_password_hash(password),secret))
                        db.commit()
                        return redirect ( url_for("login") )
    return render_template("user_register.html", form=form, title = "Register")
                    
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    db = get_db()
    if form.validate_on_submit():
        user_type = form.user_type.data
        user_id = form.user_id.data
        admin_id = form.user_id.data
        password = form.password.data
        if user_type == "Guest":
            possible_clashing_user = db. execute("""SELECT * FROM users
                                WHERE user_id =?;""",(user_id,)).fetchone()
            if possible_clashing_user is None:
                form.user_id.errors.append("No such user!")
            elif not check_password_hash(possible_clashing_user["password"], password):
                form.password.errors.append("Incorrect password!")
            else:
                session.clear()
                session["user_type"] = "admin"
                session["user_id"] = user_id
                next_page = request.args.get("next")
                if not next_page:
                    next_page = url_for("index")
                return redirect(next_page)
        else:
            possible_clashing_admin = db. execute("""SELECT * FROM admins
                                WHERE admin_id =?;""",(admin_id,)).fetchone()
            if possible_clashing_admin is None:
                form.user_id.errors.append("No such user!")
            elif not check_password_hash(possible_clashing_admin["password"], password):
                form.password.errors.append("Incorrect password!")
            else:
                session.clear()
                session["user_type"] = "admin"
                session["admin_id"] = admin_id
                return redirect(url_for("dashboard"))
    return render_template("user_login.html", form=form, title="Login")

@app.route("/reset", methods=["GET", "POST"])
def reset():
    form = ResetForm()
    db = get_db()
    if form.validate_on_submit():
        user_type = form.user_type.data
        user_id = form.user_id.data
        admin_id = form.user_id.data
        password = form.password.data
        secret = form.secret.data
        if user_type == "Guest":
            user_id_exists = db.execute("""SELECT * FROM users
                                    WHERE user_id =?;""",(user_id,)).fetchone()
            if user_id_exists is None:
                form.user_id.errors.append("No such regular user!")
            else:
                secret_check = db.execute("""SELECT secret FROM users
                                    WHERE user_id =?;""",(user_id,)).fetchone()
                if secret not in secret_check:
                    form.secret.errors.append("Your secret key is incorrect.")
                else:
                    db.execute("""UPDATE users SET password=? WHERE user_id=?;""",(generate_password_hash(password),user_id))
                    db.commit()
                    return redirect ( url_for("login") )
        elif user_type == "Admin":
            admin_id_exists = db.execute("""SELECT * FROM users
                                    WHERE user_id =?;""",(admin_id,)).fetchone()
            if admin_id_exists is None:
                form.user_id.errors.append("No such admin user!")
            else:
                secret_check = db.execute("""SELECT secret FROM admins
                                    WHERE admin_id =?;""",(admin_id,)).fetchone()
                if secret not in secret_check:
                    form.secret.errors.append("Your secret key is incorrect.")
                else:
                    db.execute("""UPDATE admins SET password=? WHERE admin_id=?;""",(generate_password_hash(password),admin_id))
                    db.commit()
                    return redirect ( url_for("login") )
    return render_template("user_reset.html", form=form, title="Reset")

@app.route("/logout")
def logout():
    session.clear()
    return redirect( url_for("index") )


@app.route("/dashboard",methods=["GET","POST"])
def dashboard():
    db = get_db()
    form = AddNewFoodForm()
    account_id = ""
    if g.admin_id:
        account_id = session["admin_id"]
    else:
        return redirect(url_for("login"))
    foods_not = db.execute("""SELECT * FROM foods_not;""").fetchall()
    foods = db.execute("""SELECT * FROM nutrition AS n 
                                        JOIN gigl_table AS g
                                        ON n.food_name = g.food_name
                                        """).fetchall()
    if form.submit.data:
        food_name = form.food_name.data
        food_type = form.food_type.data
        url = "None.png"
        valid = db.execute("""SELECT * FROM nutrition
                                WHERE food_name =?;""",(food_name,)).fetchone()
        if form.submit.data and valid==None:
            db.execute("""INSERT INTO nutrition (food_name,food_type,url) 
                       VALUES(?,?,?);""",(food_name,food_type,url))
            db.execute("""INSERT INTO gigl_table (food_name) 
                       VALUES(?);""",(food_name,))
            db.commit()
            return redirect(url_for("foods"))
        else:
            form.food_name.errors = list(form.food_name.errors)
            form.food_name.errors.append("This food is already in the db.")
        foods = db.execute("""SELECT * FROM nutrition AS n 
                                        JOIN gigl_table AS g
                                        ON n.food_name = g.food_name
                                        """).fetchall()
    return render_template("dashboard.html",title = "Dashboard", account_id = account_id,foods_not=foods_not,form=form,foods=foods)

@app.route("/food_update/<order_id>",methods=["GET","POST"])
def food_update(order_id):
    db = get_db()
    form = AddNewFoodForm()
    account_id=""
    if g.user_type:
        if g.user_id:
            account_id = session["user_id"]
        else:
            account_id = session["admin_id"]
    status_dict = db.execute("""SELECT * FROM foods_not WHERE order_id=?;""",(order_id,)).fetchone()
    foods = db.execute("""SELECT * FROM nutrition AS n 
                                        JOIN gigl_table AS g
                                        ON n.food_name = g.food_name
                                        """).fetchall()
    if form.update.data:
        status = form.status.data
        db.execute("""UPDATE foods_not SET status=? WHERE order_id=?;""",(status,order_id,))
        db.commit()
        form.status.data = status_dict["status"]
        return redirect(url_for("food_update",order_id=order_id))
    form.status.data = status_dict["status"]
    if form.submit.data:
        food_name = form.food_name.data
        food_type = form.food_type.data
        url = "None.png"
        valid = db.execute("""SELECT * FROM nutrition
                                WHERE food_name =?;""",(food_name,)).fetchone()
        if form.submit.data and valid==None:
            db.execute("""INSERT INTO nutrition (food_name,food_type,url) 
                       VALUES(?,?,?);""",(food_name,food_type,url))
            db.execute("""INSERT INTO gigl_table (food_name) 
                       VALUES(?);""",(food_name,))
            db.commit()
            return redirect(url_for("foods"))
        else:
            form.food_name.errors = list(form.food_name.errors)
            form.food_name.errors.append("This food is already in the db.")
        foods = db.execute("""SELECT * FROM nutrition AS n 
                                        JOIN gigl_table AS g
                                        ON n.food_name = g.food_name
                                        """).fetchall()
    return render_template("food_update.html",account_id=account_id,title="Status",status_dict=status_dict,form=form,foods=foods)


@app.route("/user_profile",methods=["GET","POST"])
def user_profile():
    form = ProfileForm()
    db = get_db()
    account_id = ""
    if g.user_type:
        if g.user_id:
            account_id = session["user_id"]
        elif g.admin_id:
            account_id = session["admin_id"]
        if form.validate_on_submit():
            name = str(form.name.data)
            gender = str(form.gender.data)
            age = str(form.age.data)
            height = float(form.height.data)
            weight = float(form.weight.data)
            bmi_data = weight/(height*height)
            form.bmi.data = bmi_data
            if name.isalpha()==False:
                name = None
                form.name.errors.append("Please enter the name by alphas!")
            if age != "":
                try:
                    age = int(age)
                    age = str(age)
                except:
                    age = None
                    form.age.errors.append("Please enter the age in integer!")
            else:
                age = None
            if bmi_data <= 16:
                form.bmi_category.data = "Underweight (Severe thinness)"
            elif bmi_data >16 and bmi_data <= 17:
                form.bmi_category.data = "Underweight (Moderate thinness)"
            elif bmi_data >17 and bmi_data <= 18.5:
                form.bmi_category.data = "Underweight (Mild thinness)"
            elif bmi_data >18.5 and bmi_data <= 25:
                form.bmi_category.data = "Normal range"
            elif bmi_data >25 and bmi_data <= 30:
                form.bmi_category.data = "Overweight (Pre-obese)"
            elif bmi_data > 30 and bmi_data <= 35:
                form.bmi_category.data = "Obese (Class I)"
            elif bmi_data > 35 and bmi_data <= 40:
                form.bmi_category.data = "Obese (Class II)"
            elif bmi_data > 40:
                form.bmi_category.data = "Obese (Class III)"
            bmi_category = form.bmi_category.data
            if height is not None and weight is not None:
                db.execute("""UPDATE user_profiles SET name=?,gender=?, age=?, height=?,weight=?,bmi=?,bmi_category=?
                    WHERE user_id=?;""",(name,gender,age,height,weight,round(bmi_data,2),bmi_category,account_id,))
                db.commit()
        user_profile = db.execute("""SELECT * FROM user_profiles WHERE user_id = ?;""",(account_id,)).fetchall()
        form.user_id.data = user_profile[0]["user_id"]
        form.name.data = user_profile[0]["name"]
        form.gender.data = user_profile[0]["gender"]
        form.age.data = user_profile[0]["age"]
        form.height.data = user_profile[0]["height"]
        form.weight.data = user_profile[0]["weight"]
        form.bmi.data = user_profile[0]["bmi"]
        form.bmi_category.data = user_profile[0]["bmi_category"]
        if user_profile[0]["gender"] == "Male":
            dict_general = db.execute("""SELECT * FROM age_recommend_general_male WHERE age=?;""",(user_profile[0]["age"],)).fetchall()
            dict_vitamin = db.execute("""SELECT * FROM age_recommend_vitamin_male WHERE age=?;""",(user_profile[0]["age"],)).fetchall()
        else:
            dict_general = db.execute("""SELECT * FROM age_recommend_general_female WHERE age=?;""",(user_profile[0]["age"],)).fetchall()
            dict_vitamin = db.execute("""SELECT * FROM age_recommend_vitamin_female WHERE age=?;""",(user_profile[0]["age"],)).fetchall()
    else:
        return redirect( url_for('login') )
    return render_template("user_profile.html",dict_general=dict_general,dict_vitamin=dict_vitamin,form=form,user_profile=user_profile, title="User Profile", account_id = account_id)

@app.route("/users_profile",methods=["GET","POST"])
def users_profile():
    form = ProfileForm()
    db = get_db()
    account_id = ""
    if g.user_type:
        if g.user_id:
            account_id = session["user_id"]
        elif g.admin_id:
            account_id = session["admin_id"]
    else:
        return redirect( url_for('login') )
    users_profile = db.execute("""SELECT * FROM user_profiles;""").fetchall()
    return render_template("users_profile.html",title="User Profile", account_id = account_id,users_profile=users_profile)

@app.route("/enquiry",methods=["GET","POST"])
def enquiry():
    account_id=""
    if g.user_type:
        if g.user_id:
            account_id = session["user_id"]
        else:
            account_id = session["admin_id"]
    return render_template("enquiry_base.html", title="Enquiry",account_id=account_id)

@app.route("/foods",methods=["GET","POST"])
def foods():
    db = get_db()
    form = FoodsForm()
    account_id=""
    if g.user_type:
        if g.user_id:
            account_id = session["user_id"]
        else:
            account_id = session["admin_id"]
    foods = db.execute("""SELECT * FROM nutrition AS n 
                                            JOIN gigl_table AS g
                                            ON n.food_name = g.food_name;""").fetchall()
    if form.submit.data or form.search.data:
        food_name = form.food_name.data
        food_type = form.food_type.data
        foods = db.execute("""SELECT * FROM nutrition AS n 
                                        JOIN gigl_table AS g
                                        ON n.food_name = g.food_name
                                        WHERE n.food_name=?;""",(food_name,)).fetchall()
        if foods == [] and food_type=="Not selected":
            foods = db.execute("""SELECT * FROM nutrition AS n 
                                            JOIN gigl_table AS g
                                            ON n.food_name = g.food_name;""").fetchall()
        elif foods == [] and food_type != "Not selected":
            foods = db.execute("""SELECT * FROM nutrition AS n 
                                            JOIN gigl_table AS g
                                            ON n.food_name = g.food_name
                                            WHERE n.food_type=?;""",(food_type,)).fetchall()
    view_type = form.view_type.data
    if view_type == None:
        view_type = "Overview"
    if form.exchange.data:
        view_type = form.view_type.data
    return render_template("foods.html",view_type=view_type,foods=foods,title="Foods",account_id=account_id,form=form)

@app.route("/food/not_list/add",methods=["GET","POST"])
def food_not_list():
    db = get_db()
    form = FoodNotListForm()
    account_id=""
    if g.user_type:
        if g.user_id:
            account_id = session["user_id"]
        else:
            account_id = session["admin_id"]
    else:
        return redirect(url_for("login"))
    if form.validate_on_submit():
        food_name = form.food_name.data
        food_type = form.food_type.data
        user_id = account_id
        insert_date = datetime.date.today()
        guest_description = form.guest_description.data
        db.execute("""INSERT INTO foods_not (user_id,food_name,food_type,insert_date,guest_description) VALUES (?,?,?,?,?);""",(user_id,food_name,food_type,insert_date,guest_description))
        db.commit()
        redirect(url_for("food_not_list"))
    foods_not = db.execute("""SELECT * FROM foods_not WHERE user_id=?;""",(account_id,)).fetchall()
    return render_template("food_not_list.html",title="Foods",account_id=account_id,form=form,foods_not=foods_not)

@app.route("/food/not_list/delete/<order_id>",methods=["GET","POST"])
def food_not_list_delete(order_id):
    db = get_db()
    account_id=""
    if g.user_type:
        if g.user_id:
            account_id = session["user_id"]
        else:
            account_id = session["admin_id"]
    db.execute("""DELETE FROM foods_not WHERE user_id=? AND order_id=?;""", (account_id, order_id,))
    db.commit()
    return redirect(url_for("food_not_list"))
    


@app.route("/food_detail/<food_name>",methods=["GET","POST"])
def food_nutrition(food_name):
    db = get_db()
    form = NutritionForm()
    account_id=""
    if g.user_type:
        if g.user_id:
            account_id = session["user_id"]
        else:
            account_id = session["admin_id"]
    food_nutrition = db.execute("""SELECT * FROM nutrition AS n 
                                     JOIN gigl_table AS g
                                     ON n.food_name = g.food_name
                                     WHERE n.food_name=?;""",(food_name,)).fetchone()
    return render_template("food_detail.html",food_nutrition=food_nutrition,account_id=account_id,form=form,title="Enquiry Foods' Detail")

@app.route("/food_change/<food_name>",methods=["GET","POST"])
def food_change(food_name):
    db = get_db()
    form = ChangeForm()
    account_id=""
    if g.admin_id:
        account_id = session["admin_id"]
    else:
        return redirect(url_for("login"))
    if form.validate_on_submit():
        food_name = form.food_name.data
        food_type = form.food_type.data
        energy = form.energy.data
        protein = form.protein.data
        carbohydrate = form.carbohydrate.data
        dietaryFiber = form.dietaryFiber.data
        fat = form.fat.data
        vitamin_a = form.vitamin_a.data
        vitamin_b = form.vitamin_b.data
        vitamin_c = form.vitamin_c.data
        vitamin_d = form.vitamin_d.data
        trace_minerals = form.trace_minerals.data
        # user_id = account_id
        # insert_date = datetime.date.today()
        # guest_description = form.guest_description.data
        # food_name,food_type,url,energy,protein,carbohydrate,dietaryFiber,fat,vitamin_a,vitamin_b,vitamin_c,vitamin_d,trace_minera,gi,gl
        
        db.execute("""UPDATE nutrition 
                   SET food_name =?,food_type =?,energy =?,protein =?,carbohydrate =?,dietaryFiber =?,
                   fat =?,vitamin_a =?,vitamin_b =?,vitamin_c =?,vitamin_d =?,trace_minerals =?
                    WHERE food_name=?;""",
                        (food_name,food_type,energy,protein,carbohydrate,dietaryFiber,fat,vitamin_a,vitamin_b,vitamin_c,vitamin_d,trace_minerals,food_name))
        db.commit()
        redirect(url_for("food_change",food_name = food_name))
        
    food_nutrition = db.execute("""SELECT * FROM nutrition AS n 
                                    JOIN gigl_table AS g
                                    ON n.food_name = g.food_name
                                    WHERE n.food_name=?;""",(food_name,)).fetchone()
    form.food_name.data = food_nutrition["food_name"]
    form.food_type.data = food_nutrition["food_type"] 
    form.url.data = food_nutrition["url"] 
    form.energy.data = food_nutrition["energy"] 
    form.protein.data = food_nutrition["protein"] 
    form.carbohydrate.data = food_nutrition["carbohydrate"] 
    form.dietaryFiber.data = food_nutrition["dietaryFiber"] 
    form.fat.data = food_nutrition["fat"] 
    form.vitamin_a.data = food_nutrition["vitamin_a"] 
    form.vitamin_b.data = food_nutrition["vitamin_b"] 
    form.vitamin_c.data = food_nutrition["vitamin_c"] 
    form.vitamin_d.data = food_nutrition["vitamin_d"] 
    form.trace_minerals.data = food_nutrition["trace_minerals"] 
    form.gi.data = food_nutrition["gi"] 
    form.gl.data = food_nutrition["gl"] 

    return render_template("food_change.html",food_nutrition=food_nutrition,account_id=account_id,form=form,title="Change")

@app.route("/enquiry/bmi",methods=["GET","POST"])
def bmi():
    form = BmiEnquiryForm()
    db = get_db()
    bmi = db.execute("""SELECT * FROM bmi;""").fetchall()
    account_id = ""
    if form.validate_on_submit():
        weight = float(form.weight.data)
        height = float(form.height.data)
        bmi_data = weight/(height*height)
        form.bmi.data = round(bmi_data,2)
        if bmi_data <= 16:
            form.result.data = "Underweight (Severe thinness)"
        elif bmi_data >16 and bmi_data <= 17:
            form.result.data = "Underweight (Moderate thinness)"
        elif bmi_data >17 and bmi_data <= 18.5:
            form.result.data = "Underweight (Mild thinness)"
        elif bmi_data >18.5 and bmi_data <= 25:
            form.result.data = "Normal range"
        elif bmi_data >25 and bmi_data <= 30:
            form.result.data = "Overweight (Pre-obese)"
        elif bmi_data > 30 and bmi_data <= 35:
            form.result.data = "Obese (Class I)"
        elif bmi_data > 35 and bmi_data <= 40:
            form.result.data = "Obese (Class II)"
        elif bmi_data > 40:
            form.result.data = "Obese (Class III)"
        if form.save.data:
            if g.user_id:
                user_id = session["user_id"]
                bmi_category = form.result.data
                if height is not None and weight is not None:
                    db.execute("""UPDATE user_profiles SET height=?,
                               weight=?,bmi=?, bmi_category=?
                               WHERE user_id=?;""",
                               (height,weight,round(bmi_data,2),bmi_category,user_id))
                    db.commit()
    if g.user_type:
        if g.user_id:
            account_id = session["user_id"]
            user_id = session["user_id"]
        elif g.admin_id:
            account_id = session["admin_id"]
    return render_template("enquiry_bmi.html",bmi=bmi, form=form, title="Enquiry BMI", account_id=account_id)
    
@app.route("/enquiry/recommend_age_general",methods=["GET","POST"])
def recommend_age_general():
    form = Age_RecommendForm()
    db = get_db()
    account_id = ""
    if g.user_type:
        if g.user_id:
            account_id = session["user_id"]
        elif g.admin_id:
            account_id = session["admin_id"]
    age_recommend_male = db.execute("""SELECT * FROM age_recommend_general_male AS g JOIN age_recommend_vitamin_male AS v
                                            ON g.age = v.age;""").fetchall()
    age_recommend_female = db.execute("""SELECT * FROM age_recommend_general_female AS g JOIN age_recommend_vitamin_female AS v
                                            ON g.age = v.age;""").fetchall()
    if form.validate_on_submit():
        gender = form.gender.data
        age = form.age.data
        flag = True
        try:
            age = int(age)
        except:
            flag = False
        if flag == True and age>0 and age<=75:
            if gender == "Male":
                age_recommend_female = ""
                age_recommend_male = db.execute("""SELECT * FROM age_recommend_general_male AS g JOIN age_recommend_vitamin_male AS v
                                                ON g.age = v.age WHERE g.age=? AND v.age=?;""",(age,age)).fetchall()
            elif gender == "Female":
                age_recommend_male = ""
                age_recommend_female = db.execute("""SELECT * FROM age_recommend_general_female AS g JOIN age_recommend_vitamin_female AS v
                                                ON g.age = v.age WHERE g.age=? AND v.age=?;""",(age,age)).fetchall()
            elif gender == "Both":
                age_recommend_male = db.execute("""SELECT * FROM age_recommend_general_male AS g JOIN age_recommend_vitamin_male AS v
                                                ON g.age = v.age WHERE g.age=? AND v.age=?;""",(age,age)).fetchall()
                age_recommend_female = db.execute("""SELECT * FROM age_recommend_general_female AS g JOIN age_recommend_vitamin_female AS v
                                                ON g.age = v.age WHERE g.age=? AND v.age=?;""",(age,age)).fetchall()
            if form.save.data:
                db.execute("""UPDATE user_profiles SET age=?, gender=? WHERE user_id=?;""",(age,gender,account_id))
                db.commit()
        else:
            if age == "":
                if gender == "Male":
                    age_recommend_female = ""
                    age_recommend_male = db.execute("""SELECT * FROM age_recommend_general_male AS g JOIN age_recommend_vitamin_male AS v
                                                ON g.age = v.age;""").fetchall()
                elif gender == "Female":
                    age_recommend_male = ""
                    age_recommend_female = db.execute("""SELECT * FROM age_recommend_general_female AS g JOIN age_recommend_vitamin_female AS v
                                                    ON g.age = v.age;""").fetchall()
                elif gender == "Both":
                    age_recommend_male = db.execute("""SELECT * FROM age_recommend_general_male AS g JOIN age_recommend_vitamin_male AS v
                                                    ON g.age = v.age;""").fetchall()
                    age_recommend_female = db.execute("""SELECT * FROM age_recommend_general_female AS g JOIN age_recommend_vitamin_female AS v
                                                    ON g.age = v.age;""").fetchall()
            else:
                form.age.errors.append("Please enter an integer between 0 and 75!")
                if gender == "Male":
                    age_recommend_female = ""
                    age_recommend_male = db.execute("""SELECT * FROM age_recommend_general_male AS g JOIN age_recommend_vitamin_male AS v
                                                    ON g.age = v.age;""").fetchall()
                elif gender == "Female":
                    age_recommend_male = ""
                    age_recommend_female = db.execute("""SELECT * FROM age_recommend_general_female AS g JOIN age_recommend_vitamin_female AS v
                                                    ON g.age = v.age;""").fetchall()
                elif gender == "Both":
                    age_recommend_male = db.execute("""SELECT * FROM age_recommend_general_male AS g JOIN age_recommend_vitamin_male AS v
                                                    ON g.age = v.age;""").fetchall()
                    age_recommend_female = db.execute("""SELECT * FROM age_recommend_general_female AS g JOIN age_recommend_vitamin_female AS v
                                                    ON g.age = v.age;""").fetchall()
    return render_template("recommend_age_general.html",form=form, age_recommend_male = age_recommend_male, age_recommend_female=age_recommend_female, title="Age Recommend Nutrition", account_id=account_id)

@app.route("/enquiry/recommend_age_vitamin",methods=["GET","POST"])
def recommend_age_vitamin():
    form = Age_RecommendForm()
    db = get_db()
    account_id = ""
    if g.user_type:
        if g.user_id:
            account_id = session["user_id"]
        elif g.admin_id:
            account_id = session["admin_id"]
    age_recommend_male = db.execute("""SELECT * FROM age_recommend_general_male AS g JOIN age_recommend_vitamin_male AS v
                                            ON g.age = v.age;""").fetchall()
    age_recommend_female = db.execute("""SELECT * FROM age_recommend_general_female AS g JOIN age_recommend_vitamin_female AS v
                                            ON g.age = v.age;""").fetchall()
    if form.validate_on_submit():
        gender = form.gender.data
        age = form.age.data
        flag = True
        try:
            age = int(age)
        except:
            flag = False
        if flag == True and age>0 and age<=75:
            if gender == "Male":
                age_recommend_female = ""
                age_recommend_male = db.execute("""SELECT * FROM age_recommend_general_male AS g JOIN age_recommend_vitamin_male AS v
                                                ON g.age = v.age WHERE g.age=? AND v.age=?;""",(age,age)).fetchall()
            elif gender == "Female":
                age_recommend_male = ""
                age_recommend_female = db.execute("""SELECT * FROM age_recommend_general_female AS g JOIN age_recommend_vitamin_female AS v
                                                ON g.age = v.age WHERE g.age=? AND v.age=?;""",(age,age)).fetchall()
            elif gender == "Both":
                age_recommend_male = db.execute("""SELECT * FROM age_recommend_general_male AS g JOIN age_recommend_vitamin_male AS v
                                                ON g.age = v.age WHERE g.age=? AND v.age=?;""",(age,age)).fetchall()
                age_recommend_female = db.execute("""SELECT * FROM age_recommend_general_female AS g JOIN age_recommend_vitamin_female AS v
                                                ON g.age = v.age WHERE g.age=? AND v.age=?;""",(age,age)).fetchall()
            if form.save.data:
                db.execute("""UPDATE user_profiles SET age=?, gender=? WHERE user_id=?;""",(age,gender,account_id))
                db.commit()    
        else:
            if age == "":
                if gender == "Male":
                    age_recommend_female = ""
                    age_recommend_male = db.execute("""SELECT * FROM age_recommend_general_male AS g JOIN age_recommend_vitamin_male AS v
                                                ON g.age = v.age;""").fetchall()
                elif gender == "Female":
                    age_recommend_male = ""
                    age_recommend_female = db.execute("""SELECT * FROM age_recommend_general_female AS g JOIN age_recommend_vitamin_female AS v
                                                    ON g.age = v.age;""").fetchall()
                elif gender == "Both":
                    age_recommend_male = db.execute("""SELECT * FROM age_recommend_general_male AS g JOIN age_recommend_vitamin_male AS v
                                                    ON g.age = v.age;""").fetchall()
                    age_recommend_female = db.execute("""SELECT * FROM age_recommend_general_female AS g JOIN age_recommend_vitamin_female AS v
                                                    ON g.age = v.age;""").fetchall()
            else:
                form.age.errors.append("Please enter an integer between 0 and 75!")
                if gender == "Male":
                    age_recommend_female = ""
                    age_recommend_male = db.execute("""SELECT * FROM age_recommend_general_male AS g JOIN age_recommend_vitamin_male AS v
                                                    ON g.age = v.age;""").fetchall()
                elif gender == "Female":
                    age_recommend_male = ""
                    age_recommend_female = db.execute("""SELECT * FROM age_recommend_general_female AS g JOIN age_recommend_vitamin_female AS v
                                                    ON g.age = v.age;""").fetchall()
                elif gender == "Both":
                    age_recommend_male = db.execute("""SELECT * FROM age_recommend_general_male AS g JOIN age_recommend_vitamin_male AS v
                                                    ON g.age = v.age;""").fetchall()
                    age_recommend_female = db.execute("""SELECT * FROM age_recommend_general_female AS g JOIN age_recommend_vitamin_female AS v
                                                    ON g.age = v.age;""").fetchall()
    return render_template("recommend_age_vitamin.html",form=form,
                           age_recommend_male=age_recommend_male,
                           age_recommend_female=age_recommend_female,
                           title="Age Recommend Vitamin",
                           account_id=account_id)

@app.route("/draft",methods=["GET","POST"])
def draft():
    form = DraftForm()
    db = get_db()
    account_id = ""
    if g.user_type:
        if g.user_id:
            account_id = session["user_id"]
        elif g.admin_id:
            account_id = session["admin_id"]
    else:
        return redirect(url_for("login"))
    if "draft" not in session:
        session["draft"] = {}
    food_data = {}
    for food in session["draft"]:
        food_name=food
        dict = db.execute("""SELECT *FROM nutrition
                          WHERE food_name =?""",(food_name,)).fetchone()
        food_name = dict["food_name"]
        food_type = dict["food_type"]
        food_data[food]={"food_name":food_name,"food_type":food_type}
    if form.submit.data:
        return form.submit.data
    return render_template("draft.html", draft=session["draft"],food_data=food_data,form=form, title= "Draft",account_id=account_id)

@app.route("/add_to_draft/<food_name>",methods=["GET","POST"])
def add_to_draft(food_name):
    form = DraftForm()
    db = get_db()
    #Part A
    account_id = ""
    if g.user_type:
        if g.user_id:
            account_id = session["user_id"]
        elif g.admin_id:
            account_id = session["admin_id"]
    else:
        return redirect(url_for("login"))
    #Part B
    food = food_name #initialize
    if "draft" not in session:
        session["draft"] = {}
    if food not in session["draft"]:
        session["draft"][food]={"food_name":food_name,"food_num":1}
    else:
        session["draft"][food]["food_num"] += 1
    return redirect(url_for("draft",form=form, title= "Draft",account_id=account_id))

@app.route("/delete_from_draft/<food_name>",methods=["GET","POST"])
def delete_from_draft(food_name):
    form = DraftForm()
    db = get_db()
    #Part A
    account_id = ""
    if g.user_type:
        if g.user_id:
            account_id = session["user_id"]
        elif g.admin_id:
            account_id = session["admin_id"]
    else:
        return redirect(url_for("login"))
    #Part B
    food = food_name #initialize
    if food in session["draft"]:
        session["draft"].pop(food)
    return redirect(url_for("draft",form=form, title= "Draft",account_id=account_id))

@app.route("/record/design/<food_name>",methods=["GET","POST"])
def record_design(food_name):
    form = RecordDesignForm()
    db = get_db()
    account_id = ""
    if g.user_type:
        if g.user_id:
            account_id = session["user_id"]
        elif g.admin_id:
            account_id = session["admin_id"]
    else:
        return redirect(url_for("login"))
    if food_name != "None":
        today = datetime.date.today() 
        db.execute("""INSERT INTO record_design (user_id,food_name,meal_time,insert_date)
                   VALUES (?,?,?,?);""",(account_id,food_name,None,today,))
        db.commit()
        return redirect(url_for("record_design",food_name="None"))
    record_design = db.execute("""SELECT * FROM record_design WHERE user_id=?;""",(account_id,)).fetchall()
    if form.validate_on_submit:
        food_id = form.food_id.data
        if food_id == None:
            valid = False
            if form.enquiry.data and form.meal_time.data != "Not Select":
                meal_time=form.meal_time.data
                record_design = db.execute("""SELECT * FROM record_design WHERE user_id=? AND meal_time=?;""",(account_id,meal_time,)).fetchall()
                if record_design == []:
                    return redirect(url_for("record_design",food_name="None"))
        else:
            valid = False
            for i in record_design:
                if food_id == i[0]:
                    # error append is better
                    valid = True
        if valid == True:
            if form.enquiry.data:
                record_design = db.execute("""SELECT * FROM record_design WHERE user_id=? AND food_id=?;""",(account_id,food_id,)).fetchall()
                return redirect(url_for("record_design",food_name="None"))
            if form.update.data:
                meal_time = form.meal_time.data
                db.execute("""UPDATE record_design SET meal_time=? WHERE user_id=? and food_id=?;""",(meal_time,account_id,food_id,))
                db.commit()
                return redirect(url_for("record_design",food_name="None"))
            if form.delete.data:
                db.execute("DELETE FROM record_design WHERE user_id=? AND food_id=?;", (account_id, food_id,))
                db.commit()
                return redirect(url_for("record_design",food_name="None"))
    return render_template("record_design.html",form=form,record_design=record_design,title="Record Design",account_id=account_id)
