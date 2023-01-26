library(RSQLite)

mydb <- dbConnect(RSQLite::SQLite(), "C:/Moje/Wykłady - notatki/3 semestr/Rachunek Prawdopodobieństwa i Statystyka/Website-reading/Database/shops.db")
shops_number <- dbGetQuery(mydb,'SELECT liczba_sklepow FROM liczba_sklepow WHERE liczba_sklepow > 1')
dbDisconnect(mydb)

png(file='Histogram_shops_greater_one_log.png', width=900, height = 800)

par(mar = c(6,6,6,2))

hist(log(shops_number$liczba_sklepow), main="Histogram liczby sklepów", 
     xlab="Zlogarytmowana liczba sklepów",
     ylab = "Ilość gmin", col='#800080', cex.main=2, cex.lab = 2, cex.axis = 1.3)
grid(nx=NA, ny=NULL)
hist(log(shops_number$liczba_sklepow), main="Histogram liczby sklepów", 
     xlab="Zlogarytmowana liczba sklepów", add=T,
     ylab = "Ilość gmin", col='#800080', cex.main=2, cex.lab = 2, cex.axis = 1.3)

dev.off()
