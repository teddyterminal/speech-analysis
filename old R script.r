library(tidytext)
library(dplyr)
library(hash)
library(randomcoloR)
library(readtext)
library(ggplot2)

setwd("~/speeches")

s = read.table("sss.txt", sep = "\t")
ss = s["V1"][[1]]

length(get_sentiments("bing")[[1]])
star = c("khizr.txt")

ggg = ggplot() + ylim(0, 0.065)

for (filen in star)
{
  x = readtext(filen)["text"][[1]]
  x = gsub("[[:punct:][:blank:]]+", " ", x)
  x = gsub("\n", "", x)
  x = tolower(x)
  print(x)
  
  x2 = strsplit(x, " ")[[1]]
  print(length(x2))
  
  hallo = integer(0)
  bye = integer(0)
  h = hash()
  #positive, negative, anger, anticipation, disgust, fear, joy, sadness, surprise, and trust
  running_sentiment = 0
  count = 0
  for (word in x2)
  {
    count = count + 1
    q = which(ss==word)
    if (length(q) > 0)
    {
      value = s[q, "V3"][[1]]
      running_sentiment = running_sentiment + value
    }
    
    hallo = append(hallo, running_sentiment/length(x2))
    bye = append(bye, count/length(x2))
  }
  
  h = data.frame(hallo, bye)
  if (filen %in% c("sotu17.txt", "sotu18.txt", "sotu19.txt", "sotu20.txt"))
  {
    ggg = ggg + geom_line(data = h, aes(x = bye, y = hallo), color = "red")
  }
  else
  {
    ggg = ggg + geom_line(data = h, aes(x = bye, y = hallo), color = randomColor())
  }
  print(filen)
  print(running_sentiment/length(x2))
}

ggg
