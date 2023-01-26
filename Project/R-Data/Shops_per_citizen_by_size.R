library(RSQLite)
library(comprehenr)
mydb <- dbConnect(RSQLite::SQLite(), "C:/Moje/Wykłady - notatki/3 semestr/Rachunek Prawdopodobieństwa i Statystyka/Website-reading/Database/shops.db")
shops_num_data <- dbGetQuery(mydb,'SELECT liczba_mieszkancow, liczba_sklepow FROM liczba_sklepow')
c_0_20 <- dbGetQuery(mydb,'SELECT SUM(liczba_mieszkancow) AS LM, SUM(liczba_sklepow) AS n FROM liczba_sklepow WHERE liczba_mieszkancow <= 20000')
c_20_100 <- dbGetQuery(mydb,'SELECT SUM(liczba_mieszkancow) AS LM, SUM(liczba_sklepow) AS n FROM liczba_sklepow WHERE liczba_mieszkancow > 20000 AND liczba_mieszkancow <= 100000')
c_100_400 <- dbGetQuery(mydb,'SELECT SUM(liczba_mieszkancow) AS LM, SUM(liczba_sklepow) AS n FROM liczba_sklepow WHERE liczba_mieszkancow > 100000 AND liczba_mieszkancow <= 400000')
c_400_inf <- dbGetQuery(mydb,'SELECT SUM(liczba_mieszkancow) AS LM, SUM(liczba_sklepow) AS n FROM liczba_sklepow WHERE liczba_mieszkancow > 400000')
dbDisconnect(mydb)

get_shops_per_citizen <- function(c_val){
  return(100000*c_val$n[1]/c_val$LM[1])
}

data_vec = c(get_shops_per_citizen(c_0_20), get_shops_per_citizen(c_20_100), get_shops_per_citizen(c_100_400),
             get_shops_per_citizen(c_400_inf))

png(file='Shops_per_citizen_by_size.png', width=900, height = 800)

par(mar = c(6,6,6,2))

barp <- barplot(data_vec, names.arg = c('(0,20]','(20,100]','(100,400]','(400,Inf]'), 
                main="Liczba sklepów na 100tys. mieszkańców\nw zależności od liczby mieszkańców\nz podziałem na przedziały",
                xlab = "Liczba mieszkańców[tys.]", ylab = "Liczba sklepów na 100tys. mieszkańców",
                col='#800080', cex.main=2, cex.lab = 2, cex.axis = 1.3, cex.names = 1.3, ylim=c(0, 12))
text(barp, data_vec + 0.5, labels = round(data_vec, 2), cex = 1.3)

dev.off()
