SELECT name as 'Nombre', init_date as 'Fecha de inicio' FROM users WHERE age BETWEEN 20 AND 30;

SELECT CONCAT('Nombre: ', name, '. Apellido: ', surname) FROM users;