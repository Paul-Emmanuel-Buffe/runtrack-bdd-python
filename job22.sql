SELECT *
FROM laplateforme.etudiant
WHERE age = (SELECT MIN(age) FROM laplateforme.etudiant);
