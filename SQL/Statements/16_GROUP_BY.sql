SELECT MAX(age) FROM users GROUP BY age;

SELECT COUNT(age) FROM users GROUP BY age;

SELECT COUNT(age), age FROM users WHERE age > 15 GROUP BY age ORDER BY age DESC;