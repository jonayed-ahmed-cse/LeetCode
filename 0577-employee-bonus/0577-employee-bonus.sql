SELECT e.name, b.bonus 
FROM Employee e 
LEFT JOIN Bonus b 
ON e.empid = b.empid 
WHERE bonus <1000
OR bonus is null;