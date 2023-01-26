library(RSQLite)
library(ggplot2)
library(ggpubr)

mydb <- dbConnect(RSQLite::SQLite(), "C:/Moje/Wykłady - notatki/3 semestr/Rachunek Prawdopodobieństwa i Statystyka/Website-reading/Database/shops.db")
shops_num_data <- dbGetQuery(mydb,'SELECT liczba_mieszkancow, liczba_sklepow FROM liczba_sklepow')
dbDisconnect(mydb)

citizens <- shops_num_data$liczba_mieszkancow
shops <- shops_num_data$liczba_sklepow

lm_shops_citizens <- lm(citizens ~ shops)
summary(lm_shops_citizens)

png(file='Linear_regression.png', width=675, height = 600)

shops_citizens_graph<-ggplot(shops_num_data, aes(x=citizens, y=shops)) + ggtitle("Regresja liniowa") +
  theme(panel.background = element_rect(fill="#FFFFB6", color = "#FFFFB6"),
        panel.grid.major = element_line(color = '#CCCCCC'),
        panel.grid.minor = element_line(color = '#CCCCCC'),
        axis.text = element_text(size = 15), plot.title = element_text(size = 20),
        axis.title = element_text(size = 20)) +
  geom_point(col='#800080') + geom_smooth(method = "lm", col='#666666') + 
  stat_regline_equation(label.x = 10000, label.y = 160) + 
  xlab("Liczba mieszkańców") + ylab("Liczba sklepów")
shops_citizens_graph

dev.off()



# counting
cor.test(citizens, shops)
