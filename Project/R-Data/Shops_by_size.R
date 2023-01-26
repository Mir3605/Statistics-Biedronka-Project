library(RSQLite)
library(comprehenr)
mydb <- dbConnect(RSQLite::SQLite(), "C:/Moje/Wykłady - notatki/3 semestr/Rachunek Prawdopodobieństwa i Statystyka/Website-reading/Database/shops.db")
shops_num_data <- dbGetQuery(mydb,'SELECT liczba_mieszkancow, liczba_sklepow FROM liczba_sklepow')
dbDisconnect(mydb)

create_data <- function(x){
  n = length(x$liczba_mieszkancow)
  vec = c()
  for(i in 1:n){
    shops_number = x$liczba_sklepow[i]
    add_vec = c()
    if(shops_number > 0)
      add_vec = to_vec(for(j in 1:shops_number) x$liczba_mieszkancow[i])
    vec = c(vec, add_vec)
  }
  return(vec)
}

data_vec = create_data(shops_num_data)

png(file='Shops_by_size.png', width=900, height = 800)

par(mar = c(6,6,6,2))


barp <- barplot(table(cut(data_vec/1000, breaks = c(0,20,100,400,Inf))), 
                main="Liczba sklepów w miejscowościach\nw zależności od liczby mieszkańców\nz podziałem na przedziały",
                xlab="Liczba mieszkańców[tys.]", ylab="Liczba sklepów",
                col='#800080', cex.main=2, cex.lab = 2, cex.axis = 1.3, cex.names = 1.3,
                ylim=c(0, 1200))
text(barp, table(cut(data_vec/1000, breaks = c(0,20,100,400,Inf))) + 30, 
     labels = table(cut(data_vec/1000, breaks = c(0,20,100,400,Inf))), cex = 1.3)

dev.off()
