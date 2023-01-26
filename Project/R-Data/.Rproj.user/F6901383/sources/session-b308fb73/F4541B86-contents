library(RSQLite)

mydb <- dbConnect(RSQLite::SQLite(), "C:/Moje/Wykłady - notatki/3 semestr/Rachunek Prawdopodobieństwa i Statystyka/Website-reading/Database/shops.db")
shops_num_data <- dbGetQuery(mydb,'SELECT liczba_mieszkancow, liczba_sklepow FROM liczba_sklepow')
dbDisconnect(mydb)

png(file='No_shops_to_citizens_log.png', width=900, height = 800)

par(mar = c(6,6,6,2))

plot.new()

rect(par("usr")[1], par("usr")[3],
     par("usr")[2], par("usr")[4],
     col = "#FFFFB6") # Color

par(new = TRUE)
plot(shops_num_data$liczba_mieszkancow/1000, shops_num_data$liczba_sklepow, 
     main='Liczba sklepów, a liczba mieszkańców\n (skala logarytmiczna)', xlab='Liczba mieszkańców[tys.]', 
     ylab='Liczba sklepów', type='p', log = 'xy', col='#800080', cex.main=2, 
     cex.lab = 2, cex.axis = 1.3, bty='L')
grid(nx=NULL, ny=NULL)

dev.off()

