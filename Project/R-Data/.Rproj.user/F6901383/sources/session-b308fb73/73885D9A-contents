library(RSQLite)

mydb <- dbConnect(RSQLite::SQLite(), "C:/Moje/Wykłady - notatki/3 semestr/Rachunek Prawdopodobieństwa i Statystyka/Website-reading/Database/shops.db")
citizens_number <- dbGetQuery(mydb,'SELECT liczba_mieszkancow FROM liczba_sklepow WHERE liczba_mieszkancow <=50000 AND liczba_sklepow > 0')
dbDisconnect(mydb)

png(file='Histogram_coms_with_shops.png', width=900, height = 800)

par(mar = c(6,6,6,2))

hist(citizens_number$liczba_mieszkancow, main="Histogram liczby mieszkańców gmin\nze sklepami do 50 tys. mieszkańców", 
     xlab="Liczba mieszkańców",
     ylab = "Częstotliwość występowania", col='#800080', cex.main=2, cex.lab = 2, cex.axis = 1.3)
grid(nx=NA, ny=NULL)
hist(citizens_number$liczba_mieszkancow, main="Histogram liczby mieszkańców gmin\nze sklepami do 50 tys. mieszkańców", 
     xlab="Liczba mieszkańców", add=T,
     ylab = "Częstotliwość występowania", col='#800080', cex.main=2, cex.lab = 2, cex.axis = 1.3)

dev.off()
