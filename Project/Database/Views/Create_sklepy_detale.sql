CREATE VIEW IF NOT EXISTS sklepy_detale AS
SELECT DISTINCT * FROM gminy AS G
INNER JOIN sklepy AS S ON G.id = S.id_gminy
INNER JOIN godziny_otwarcia AS Godz ON Godz.id_sklepu = S.id_sklepu
ORDER BY S.id_sklepu