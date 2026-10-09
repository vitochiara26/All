CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(100),
    age INT,
    init_date DATE,
    email VARCHAR(100)
)