library(RSQLite)
mydb <- dbConnect(RSQLite::SQLite(), "C:/Moje/Wykłady - notatki/3 semestr/Rachunek Prawdopodobieństwa i Statystyka/Website-reading/Database/shops.db")
shops_type_data <- dbGetQuery(mydb,'SELECT typ, SUM(liczba_sklepow) AS liczba_sklepow FROM liczba_sklepow GROUP BY typ')
dbDisconnect(mydb)



png(file='Shops_by_type.png', width=900, height = 800)

plot.new()

par(mar = c(6,6,6,2))


barp <- barplot(shops_type_data$liczba_sklepow, names.arg = shops_type_data$typ, 
                main="Liczba sklepów w gminach danego typu",
                col='#800080', cex.main=2, cex.lab = 2, cex.axis = 1.3, cex.names = 1.3, ylim=c(0, 2300))
text(barp, shops_type_data$liczba_sklepow + 100, labels = shops_type_data$liczba_sklepow, cex = 1.3)

dev.off()
