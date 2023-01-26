library(RSQLite)

mydb <- dbConnect(RSQLite::SQLite(), "C:/Moje/Wykłady - notatki/3 semestr/Rachunek Prawdopodobieństwa i Statystyka/Website-reading/Database/shops.db")
citizens_number <- dbGetQuery(mydb,'SELECT liczba_mieszkancow FROM gminy')
dbDisconnect(mydb)

png(file='Histogram_coms_all.png', width=900, height = 800)

par(mar = c(6,6,6,2))

hist(citizens_number$liczba_mieszkancow, main="Histogram liczby mieszkańców\nwszystkich gmin", 
     xlab="Liczba mieszkańców",
     ylab = "Częstotliwość występowania", col='#800080', cex.main=2, cex.lab = 2, cex.axis = 1.3)
grid(nx=NA, ny=NULL)
hist(citizens_number$liczba_mieszkancow, main="Histogram liczby mieszkańców\nwszystkich gmin", 
     xlab="Liczba mieszkańców", add=T,
     ylab = "Częstotliwość występowania", col='#800080', cex.main=2, cex.lab = 2, cex.axis = 1.3)

dev.off()
