SELECT c.name, SUM(p.amount)
FROM categories c
JOIN products p ON c.id = p.id_categories
GROUP BY c.name;