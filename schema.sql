DROP TABLE IF EXISTS users;
CREATE TABLE users 
(
    user_id TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    secret TEXT NOT NULL
);
INSERT INTO users (user_id, password, secret)
VALUES
    ('admin','pbkdf2:sha256:260000$wWQXhnBbMYQmWEZN$b13dec11bcf502318527a18052f096ec7e9d18bdb66e0e6a408e2eef195af983','secret');
/*********************************/

DROP TABLE IF EXISTS admins;
CREATE TABLE admins 
(
    admin_id TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    secret TEXT NOT NULL
);
INSERT INTO admins (admin_id, password, secret)
VALUES
    ('admin','pbkdf2:sha256:260000$wWQXhnBbMYQmWEZN$b13dec11bcf502318527a18052f096ec7e9d18bdb66e0e6a408e2eef195af983','secret');
/*********************************/


DROP TABLE IF EXISTS user_profiles;
CREATE TABLE user_profiles 
(
    user_id TEXT PRIMARY KEY,
    name TEXT,
    gender TEXT,
    age INTEGER,
    height DECIMAL,
    weight DECIMAL,
    bmi DECIMAL,
    bmi_category TEXT
);
INSERT INTO user_profiles (user_id, name, gender, age, height, weight, bmi, bmi_category)
VALUES
('u001', 'Alice', 'Female', 25, 1.68, 60.5, 21.39, 'Normal'),
('u002', 'Diana', 'Female', 28, 1.6, 48.9, 19.14, 'Underweight'),
('u003', 'Ethan', 'Male', 37, 1.85, 82.3, 24.01, 'Normal');
/*********************************/

DROP TABLE IF EXISTS foods;

CREATE TABLE foods
(
    food_name TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT
);

DROP TABLE IF EXISTS nutrition;
CREATE TABLE nutrition
(
    food_name TEXT PRIMARY KEY,
    food_type TEXT,
    url TEXT,
    energy DECIMAL,
    protein DECIMAL,
    carbohydrate DECIMAL,
    dietaryFiber DECIMAL,
    fat DECIMAL,
    vitamin_a DECIMAL,
    vitamin_b DECIMAL,
    vitamin_c DECIMAL,
    vitamin_d DECIMAL,
    trace_minerals DECIMAL
);
INSERT INTO nutrition (food_name,food_type,url,energy, protein, carbohydrate, dietaryFiber, fat, vitamin_a, vitamin_b, vitamin_c, vitamin_d, trace_minerals) 
VALUES 
("Apple", "Fruit","Apple.png",52, 0.26, 13.81, 2.4, 0.17, 3, 0.017, 7.9, 0, 0.04),
("Tomato", "Vegetable","Tomato.jpg",18, 0.88, 3.89, 1.2, 0.2, 1027, 0.037, 13, 0, 0.15),
("Salmon", "Seafood","Salmon.jpg",206, 22, 0, 0, 13, 28, 0.95, 0, 526, 0.45),
("Peanuts", "Seed","Peanuts.jpeg",567, 25.8, 16.13, 8.5, 49.24, 0, 0.08, 0, 0, 1.02),
("Chicken", "Meat","Chicken.jpg",239, 27.3, 0, 0, 14.9, 0, 0.2, 0, 0, 1.2),
("Soybean", "Legume","Soybean.jpg",446, 36.49, 30.16, 9.3, 19.94, 0, 0.89, 0, 0, 4.5),
("Wheat", "Grain","Wheat.jpg",329, 13.7, 71.2, 10.7, 1.9, 0, 0.482, 0, 0, 3.67);
/**Ref: https://fdc.nal.usda.gov/index.html***********************/
/*********************************/

DROP TABLE IF EXISTS gigl_table;
CREATE TABLE gigl_table
(
    food_name TEXT PRIMARY KEY,
    gi DECIMAL,
    gl DECIMAL
);
INSERT INTO gigl_table (food_name, gi, gl)
VALUES 
    ('Apple', 38, 6),
    ('Tomato', 38, 2),
    ('Salmon', 0, 0),
    ('Peanuts', 13, 0),
    ('Chicken', 0, 0),
    ('Soybean', 18, 1),
    ('Wheat', 45, 26.8);
/*********************************/

DROP TABLE IF EXISTS bmi;
CREATE TABLE bmi
(
    category TEXT,
    min_bmi DECIMAL,
    max_bmi DECIMAL,
    min_bmi_prime DECIMAL,
    max_bmi_prime DECIMAL
);
INSERT INTO bmi (category, min_bmi, max_bmi, min_bmi_prime, max_bmi_prime)
VALUES
    ("Underweight (Severe thinness)",NULL,16.0,NULL,0.64),
    ("Underweight (Moderate thinness)",16.0,16.9,0.64,0.67),
    ("Underweight (Mild thinness)",17.0,18.4,0.68,0.73),
    ("Normal range",18.5,24.9,0.74,0.99),
    ("Overweight (Pre-obese)",25.0,29.9,1.00,1.19),
    ("Obese (Class I)",30.0,34.9,1.20,1.39),
    ("Obese (Class II)",35.0,39.9,1.40,1.59),
    ("Obese (Class III)",40.0,NULL,1.60,NULL);
/**Ref: https://en.wikipedia.org/wiki/Body_mass_index**/
/*********************************/

DROP TABLE IF EXISTS age_recommend_general_male;
CREATE TABLE age_recommend_general_male
(
    age INTEGER PRIMARY KEY,
    energy_MJ DECIMAL,
    energy_kcal DECIMAL,
    protein DECIMAL,
    fat DECIMAL,
    carbohydrate DECIMAL,
    free_sugars DECIMAL,
    salt DECIMAL,
    fibre DECIMAL
);
INSERT INTO age_recommend_general_male (
    age,
    energy_MJ,
    energy_kcal,
    protein,
    fat,
    carbohydrate,
    free_sugars,
    salt,
    fibre
)
VALUES
    (1, 3.2, 765, 14.5 , NULL, NULL, Null, 2.0, NUll),
    (2, 4.55, 1088, 14.5, NULL, 15, 2.0, 15, Null),
    (3, 4.55, 1088, 14.5, NULL, 15, 2.0, 15, Null),
    (4, 6.2, 1482, 19.7, 58, 198, 20, 3.0, 15),
    (5, 6.2, 1482, 19.7, 58, 198, 20, 3.0, 20),
    (6, 6.2, 1482, 19.7, 58, 198, 20, 3.0, 20),
    (7, 7.6, 1817, 28.3, 71, 242, 24, 5.0, 20),
    (8, 7.6, 1817, 28.3, 71, 242, 24, 5.0, 20),
    (9, 7.6, 1817, 28.3, 71, 242, 24, 5.0, 20),
    (10, 7.6, 1817, 28.3, 71, 242, 24, 5.0, 20),
    (11, 10.5, 2500, 42.1, 97, 333, 33, 6.0, 25),
    (12, 10.5, 2500, 42.1, 97, 333, 33, 6.0, 25),
    (13, 10.5, 2500, 42.1, 97, 333, 33, 6.0, 25),
    (14, 10.5, 2500, 42.1, 97, 333, 33, 6.0, 25),
    (15, 10.5, 2500, 55.2, 97, 333, 33, 6.0, 30),
    (16, 10.5, 2500, 55.2, 97, 333, 33, 6.0, 30),
    (17, 10.5, 2500, 55.2, 97, 333, 33, 6.0, 30),
    (18, 10.5, 2500, 55.2, 97, 333, 33, 6.0, 30),
    (19, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (20, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (21, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (22, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (23, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (24, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (25, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (26, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (27, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (28, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (29, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (30, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (31, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (32, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (33, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (34, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (35, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (36, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (37, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (38, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (39, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (40, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (41, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (42, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (43, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (44, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (45, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (46, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (47, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (48, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (49, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (50, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (51, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (52, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (53, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (54, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (55, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (56, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (57, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (58, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (59, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (60, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (61, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (62, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (63, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (64, 10.5, 2500, 55.5, 97, 333, 33, 6.0, 30),
    (65, 9.8, 2342, 53.3, 91, 312, 31, 6.0, 30),
    (66, 9.8, 2342, 53.3, 91, 312, 31, 6.0, 30),
    (67, 9.8, 2342, 53.3, 91, 312, 31, 6.0, 30),
    (68, 9.8, 2342, 53.3, 91, 312, 31, 6.0, 30),
    (69, 9.8, 2342, 53.3, 91, 312, 31, 6.0, 30),
    (70, 9.8, 2342, 53.3, 91, 312, 31, 6.0, 30),
    (71, 9.8, 2342, 53.3, 91, 312, 31, 6.0, 30),
    (72, 9.8, 2342, 53.3, 91, 312, 31, 6.0, 30),
    (73, 9.8, 2342, 53.3, 91, 312, 31, 6.0, 30),
    (74, 9.8, 2342, 53.3, 91, 312, 31, 6.0, 30),
    (75, 9.6, 2294, 53.5, 89, 306, 31, 6.0, 30);
/**Ref: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/618167/government_dietary_recommendations.pdf**/
/*********************************/

DROP TABLE IF EXISTS age_recommend_general_female;
CREATE TABLE age_recommend_general_female
(
    age INTEGER PRIMARY KEY,
    energy_MJ DECIMAL,
    energy_kcal DECIMAL,
    protein DECIMAL,
    fat DECIMAL,
    carbohydrate DECIMAL,
    free_sugars DECIMAL,
    salt DECIMAL,
    fibre DECIMAL
);
INSERT INTO age_recommend_general_female (
    age,
    energy_MJ,
    energy_kcal,
    protein,
    fat,
    carbohydrate,
    free_sugars,
    salt,
    fibre
)
VALUES
    (1, 3.0, 717, 14.5, NULL, NULL, NULL, 2.0, NULL),
    (2, 4.2, 1004, 14.5, NULL, 134, 13, 2.0, 15),
    (3, 4.2, 1004, 14.5, NULL, 134, 13, 2.0, 15),
    (4, 5.8, 1378, 19.7, 54, 184, 18, 3.0, 15),
    (5, 5.8, 1378, 19.7, 54, 184, 18, 3.0, 20),
    (6, 5.8, 1378, 19.7, 54, 184, 18, 3.0, 20),
    (7, 7.1, 1703, 28.3, 66, 227, 23, 5.0, 20),
    (8, 7.1, 1703, 28.3, 66, 227, 23, 5.0, 20),
    (9, 7.1, 1703, 28.3, 66, 227, 23, 5.0, 20),
    (10, 7.1, 1703, 28.3, 66, 227, 23, 5.0, 20),
    (11, 8.4, 2000, 41.2, 78, 267, 27, 6.0, 25),
    (12, 8.4, 2000, 41.2, 78, 267, 27, 6.0, 25),
    (13, 8.4, 2000, 41.2, 78, 267, 27, 6.0, 25),
    (14, 8.4, 2000, 41.2, 78, 267, 27, 6.0, 25),
    (15, 8.4, 2000, 45, 78, 267, 27, 6.0, 25),
    (16, 8.4, 2000, 45, 78, 267, 27, 6.0, 25),
    (17, 8.4, 2000, 45, 78, 267, 27, 6.0, 25),
    (18, 8.4, 2000, 45, 78, 267, 27, 6.0, 25),
    (19, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (20, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (21, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (22, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (23, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (24, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (25, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (26, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (27, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (28, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (29, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (30, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (31, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (32, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (33, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (34, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (35, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (36, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (37, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (38, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (39, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (40, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (41, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (42, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (43, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (44, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (45, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (46, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (47, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (48, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (49, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (50, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (51, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (52, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (53, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (54, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (55, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (56, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (57, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (58, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (59, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (60, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (61, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (62, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (63, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (64, 8.4, 2000, 45.0, 78, 267, 27, 6.0, 30),
    (65, 7.7, 1912, 46.5, 74, 255, 26, 6.0, 30),
    (66, 7.7, 1912, 46.5, 74, 255, 26, 6.0, 30),
    (67, 7.7, 1912, 46.5, 74, 255, 26, 6.0, 30),
    (68, 7.7, 1912, 46.5, 74, 255, 26, 6.0, 30),
    (69, 7.7, 1912, 46.5, 74, 255, 26, 6.0, 30),
    (70, 7.7, 1912, 46.5, 74, 255, 26, 6.0, 30),
    (71, 7.7, 1912, 46.5, 74, 255, 26, 6.0, 30),
    (72, 7.7, 1912, 46.5, 74, 255, 26, 6.0, 30),
    (73, 7.7, 1912, 46.5, 74, 255, 26, 6.0, 30),
    (74, 7.7, 1912, 46.5, 74, 255, 26, 6.0, 30),
    (75, 7.7, 1840, 46.5, 72, 245, 25, 6.0, 30);
/**Ref: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/618167/government_dietary_recommendations.pdf**/
/*********************************/

DROP TABLE IF EXISTS age_recommend_vitamin_male;
CREATE TABLE age_recommend_vitamin_male
(
    age INTEGER PRIMARY KEY, 
    vitamin_a DECIMAL,
    thiamin DECIMAL,
    riboflavin DECIMAL,
    niacin_equivalent DECIMAL,
    vitamin_b6 DECIMAL,
    vitamin_b12 DECIMAL,
    folate DECIMAL,
    vitamin_c DECIMAL,
    vitamin_d DECIMAL
);
INSERT INTO age_recommend_vitamin_male (
    age,
    vitamin_a,
    thiamin,
    riboflavin,
    niacin_equivalent,
    vitamin_b6,
    vitamin_b12,
    folate,
    vitamin_c,
    vitamin_d
)
VALUES
    (1, 400, 0.3, 0.6, 5.0, 0.7, 0.5, 70, 30, 10),
    (2, 400, 0.4, 0.6, 7.2, 0.7, 0.5, 70, 30, 10),
    (3, 400, 0.4, 0.6, 7.2, 0.7, 0.5, 70, 30, 10),
    (4, 400, 0.6, 0.8, 9.8, 0.9, 0.8, 100, 30, 10),
    (5, 400, 0.6, 0.8, 9.8, 0.9, 0.8, 100, 30, 10),
    (6, 400, 0.6, 0.8, 9.8, 0.9, 0.8, 100, 30, 10),
    (7, 500, 0.7, 1.0, 12.0, 1.0, 1.0, 100, 30, 10),
    (8, 500, 0.7, 1.0, 12.0, 1.0, 1.0, 100, 30, 10),
    (9, 500, 0.7, 1.0, 12.0, 1.0, 1.0, 100, 30, 10),
    (10, 500, 0.7, 1.0, 12.0, 1.0, 1.0, 100, 30, 10),
    (11, 600, 1.0, 1.2, 16.5, 1.2, 1.2, 200, 35, 10),
    (12, 600, 1.0, 1.2, 16.5, 1.2, 1.2, 200, 35, 10),
    (13, 600, 1.0, 1.2, 16.5, 1.2, 1.2, 200, 35, 10),
    (14, 600, 1.0, 1.2, 16.5, 1.2, 1.2, 200, 35, 10),
    (15, 700, 1.0, 1.3, 16.5, 1.5, 1.5, 200, 40, 10),
    (16, 700, 1.0, 1.3, 16.5, 1.5, 1.5, 200, 40, 10),
    (17, 700, 1.0, 1.3, 16.5, 1.5, 1.5, 200, 40, 10),
    (18, 700, 1.0, 1.3, 16.5, 1.5, 1.5, 200, 40, 10),
    (19, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (20, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (21, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (22, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (23, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (24, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (25, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (26, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (27, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (28, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (29, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (30, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (31, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (32, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (33, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (34, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (35, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (36, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (37, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (38, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (39, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (40, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (41, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (42, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (43, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (44, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (45, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (46, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (47, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (48, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (49, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (50, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (51, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (52, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (53, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (54, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (55, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (56, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (57, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (58, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (59, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (60, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (61, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (62, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (63, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (64, 700, 1.0, 1.3, 16.5, 1.4, 1.5, 200, 40, 10),
    (65, 700, 0.9, 1.3, 15.5, 1.4, 1.5, 200, 40, 10),
    (66, 700, 0.9, 1.3, 15.5, 1.4, 1.5, 200, 40, 10),
    (67, 700, 0.9, 1.3, 15.5, 1.4, 1.5, 200, 40, 10),
    (68, 700, 0.9, 1.3, 15.5, 1.4, 1.5, 200, 40, 10),
    (69, 700, 0.9, 1.3, 15.5, 1.4, 1.5, 200, 40, 10),
    (70, 700, 0.9, 1.3, 15.5, 1.4, 1.5, 200, 40, 10),
    (71, 700, 0.9, 1.3, 15.5, 1.4, 1.5, 200, 40, 10),
    (72, 700, 0.9, 1.3, 15.5, 1.4, 1.5, 200, 40, 10),
    (73, 700, 0.9, 1.3, 15.5, 1.4, 1.5, 200, 40, 10),
    (74, 700, 0.9, 1.3, 15.5, 1.4, 1.5, 200, 40, 10),
    (75, 700, 0.9, 1.3, 15.1, 1.4, 1.5, 200, 40, 10);
/**Ref: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/618167/government_dietary_recommendations.pdf**/
/*********************************/

DROP TABLE IF EXISTS age_recommend_vitamin_female;
CREATE TABLE age_recommend_vitamin_female
(
    age INTEGER PRIMARY KEY,
    vitamin_a DECIMAL,
    thiamin DECIMAL,
    riboflavin DECIMAL,
    niacin_equivalent DECIMAL,
    vitamin_b6 DECIMAL,
    vitamin_b12 DECIMAL,
    folate DECIMAL,
    vitamin_c DECIMAL,
    vitamin_d DECIMAL
);
INSERT INTO age_recommend_vitamin_female (
    age,
    vitamin_a,
    thiamin,
    riboflavin,
    niacin_equivalent,
    vitamin_b6,
    vitamin_b12,
    folate,
    vitamin_c,
    vitamin_d
)
VALUES
    (1, 400, 0.3, 0.6, 4.7, 0.7, 0.5, 70, 30, 10),
    (2, 400, 0.4, 0.6, 6.6, 0.7, 0.5, 70, 30, 10),
    (3, 400, 0.4, 0.6, 6.6, 0.7, 0.5, 70, 30, 10),
    (4, 400, 0.6, 0.8, 9.1, 0.9, 0.8, 100, 30, 10),
    (5, 400, 0.6, 0.8, 9.1, 0.9, 0.8, 100, 30, 10),
    (6, 400, 0.6, 0.8, 9.1, 0.9, 0.8, 100, 30, 10),
    (7, 500, 0.7, 1.0, 11.2, 1.0, 1.0, 150, 30, 10),
    (8, 500, 0.7, 1.0, 11.2, 1.0, 1.0, 150, 30, 10),
    (9, 500, 0.7, 1.0, 11.2, 1.0, 1.0, 150, 30, 10),
    (10, 500, 0.7, 1.0, 11.2, 1.0, 1.0, 150, 30, 10),
    (11, 600, 1.0, 1.2, 16.5, 1.2, 1.2, 200, 35, 10),
    (12, 600, 1.0, 1.2, 16.5, 1.2, 1.2, 200, 35, 10),
    (13, 600, 1.0, 1.2, 16.5, 1.2, 1.2, 200, 35, 10),
    (14, 600, 1.0, 1.2, 16.5, 1.2, 1.2, 200, 35, 10),
    (15, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (16, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (17, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (18, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (19, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (20, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (21, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (22, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (23, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (24, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (25, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (26, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (27, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (28, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (29, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (30, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (31, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (32, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (33, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (34, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (35, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (36, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (37, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (38, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (39, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (40, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (41, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (42, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (43, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (44, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (45, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (46, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (47, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (48, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (49, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (50, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (51, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (52, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (53, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (54, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (55, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (56, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (57, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (58, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (59, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (60, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (61, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (62, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (63, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (64, 600, 0.8, 1.1, 13.2, 1.2, 1.5, 200, 40, 10),
    (65, 600, 0.8, 1.1, 12.6, 1.2, 1.5, 200, 40, 10),
    (66, 600, 0.8, 1.1, 12.6, 1.2, 1.5, 200, 40, 10),
    (67, 600, 0.8, 1.1, 12.6, 1.2, 1.5, 200, 40, 10),
    (68, 600, 0.8, 1.1, 12.6, 1.2, 1.5, 200, 40, 10),
    (69, 600, 0.8, 1.1, 12.6, 1.2, 1.5, 200, 40, 10),
    (70, 600, 0.8, 1.1, 12.6, 1.2, 1.5, 200, 40, 10),
    (71, 600, 0.8, 1.1, 12.6, 1.2, 1.5, 200, 40, 10),
    (72, 600, 0.8, 1.1, 12.6, 1.2, 1.5, 200, 40, 10),
    (73, 600, 0.8, 1.1, 12.6, 1.2, 1.5, 200, 40, 10),
    (74, 600, 0.8, 1.1, 12.6, 1.2, 1.5, 200, 40, 10),
    (75, 600, 0.7, 1.1, 12.1, 1.2, 1.5, 200, 40, 10);
/**Ref: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/618167/government_dietary_recommendations.pdf**/
/*********************************/


DROP TABLE IF EXISTS record_design;
CREATE TABLE record_design
(
    food_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    food_name TEXT,
    meal_time TEXT,
    insert_date DATE,
    energy DECIMAL
);
/*********************************/

DROP TABLE IF EXISTS record;
CREATE TABLE record
(
    user_id TEXT,
    food_name TEXT,
    food_time TEXT,
    food_type TEXT,
    insert_date DATE
);

INSERT INTO record (user_id,food_name,food_time,food_type,insert_date)
VALUES
    ('admin','test_food','morning','type','2023-03-12');
/*********************************/

DROP TABLE IF EXISTS foods_not;
CREATE TABLE foods_not
(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    food_name TEXT,
    food_type TEXT,
    insert_date DATE,
    guest_description TEXT,
    status TEXT
);

INSERT INTO foods_not (order_id,user_id,food_name,food_type,insert_date,guest_description,status)
VALUES
    (1,'Guest','Lemon','Fruit','2023-03-12','Acid food','on progress');
/*********************************/