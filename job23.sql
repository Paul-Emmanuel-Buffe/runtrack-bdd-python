SELECT *
FROM laplateforme.etudiant
WHERE age = (SELECT MAX(age) FROM laplateforme.etudiant);