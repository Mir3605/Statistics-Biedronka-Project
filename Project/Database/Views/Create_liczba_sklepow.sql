CREATE VIEW IF NOT EXISTS liczba_sklepow AS
SELECT nazwa, G.id, wojewodztwo, powiat, typ, liczba_mieszkancow,
COUNT(id_sklepu) AS 'liczba_sklepow'
FROM gminy AS G
LEFT OUTER JOIN sklepy AS S ON G.id = S.id_gminy
GROUP BY nazwa, G.id, wojewodztwo, powiat, typ, liczba_mieszkancow
