library(RSQLite)
mydb <- dbConnect(RSQLite::SQLite(), "C:/Moje/Wykłady - notatki/3 semestr/Rachunek Prawdopodobieństwa i Statystyka/Website-reading/Database/shops.db")
shops_avg_data <- dbGetQuery(mydb,'SELECT typ, SUM(liczba_sklepow) AS liczba_sklepow, SUM(liczba_mieszkancow) AS liczba_mieszkancow FROM liczba_sklepow GROUP BY typ')
dbDisconnect(mydb)


data_to_plot <- data.frame(name = shops_avg_data$typ,
                           value = 100000*shops_avg_data$liczba_sklepow/shops_avg_data$liczba_mieszkancow)

png(file='Avg_shops_per_citizen_by_type.png', width=900, height = 800)

par(mar = c(6,6,6,2))


barp <- barplot(data_to_plot$value, names.arg = data_to_plot$name, 
        main="Liczba sklepów na 100tys. mieszkańców\nw gminach danego typu",
        col='#800080', cex.main=2, cex.lab = 2, cex.axis = 1.3, cex.names = 1.3, ylim=c(0, 12))
text(barp, data_to_plot$value + 0.5, labels = round(data_to_plot$value, 2), cex = 1.3)

dev.off()
