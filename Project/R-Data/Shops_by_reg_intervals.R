library(RSQLite)

mydb <- dbConnect(RSQLite::SQLite(), "C:/Moje/Wykłady - notatki/3 semestr/Rachunek Prawdopodobieństwa i Statystyka/Website-reading/Database/shops.db")
shops_intervals_data <- dbGetQuery(mydb,'SELECT liczba_mieszkancow + (10000 - (liczba_mieszkancow % 10000)) AS do_tylu_mieszkancow,
                                   SUM(liczba_sklepow) AS liczba_sklepow FROM liczba_sklepow GROUP BY do_tylu_mieszkancow')
dbDisconnect(mydb)

intervals_maker <- function(df){
  vec = c('(0,10]')
  n = length(df$do_tylu_mieszkancow)
  for(i in 2:n){
    be = df$do_tylu_mieszkancow[i-1]/1000
    en = df$do_tylu_mieszkancow[i]/1000
    to_add = paste('(', as.character(be), ',', as.character(en), ']')
    vec = c(vec, to_add)
  }
  return(vec)
}

intervals = intervals_maker(shops_intervals_data)


png(file='Shops_by_reg_intervals.png', width=1100, height = 700)

plot.new()
par(mar = c(6,6,6,2))
barplot(shops_intervals_data$liczba_sklepow, names.arg = shops_intervals_data$do_tylu_mieszkancow/10000, 
        main="Liczba sklepów w zależności od liczby mieszkańców\nz podziałem na przedziały",
        xlab = "Liczba mieszkańców[10tys.]", ylab = "Liczba sklepów",
        col='#800080', cex.main=2.5, cex.lab = 2.5, cex.axis = 1.8, cex.names = 1)
grid(nx=NA, ny=NULL)
barplot(shops_intervals_data$liczba_sklepow, names.arg = shops_intervals_data$do_tylu_mieszkancow/10000, 
        main="Liczba sklepów w zależności od liczby mieszkańców\nz podziałem na przedziały",
        xlab = "Liczba mieszkańców[10tys.]", ylab = "Liczba sklepów", add=T,
        col='#800080', cex.main=2.5, cex.lab = 2.5, cex.axis = 1.8, cex.names = 1)
dev.off()
