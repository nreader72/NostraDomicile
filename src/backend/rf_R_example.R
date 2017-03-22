

#a sample Durham zip code table
out <- read.csv("out.csv", comment.char="#")

#replacing na(missing) values
out$bathrooms[is.na(out$bathrooms)]<-3
out$lot_size_sq_footage[is.na(out$lot_size_sq_footage)]<-10000
out$year_built[is.na(out$year_built)]<-2000

#creating split point
index<-sample(1:nrow(out), size=0.2*nrow(out))


train80<-out[-index,]
train80<-train80[,c("home_type","year_built","finished_sq_footage","bedrooms","lot_size_sq_footage","bathrooms","sold_binary")]

test20<-out[index,]
test20<-test20[,c("home_type","year_built","finished_sq_footage","bedrooms","lot_size_sq_footage","bathrooms","sold_binary")]

#creates larger dataset
train<-rbind(train80,train80)
test<-rbind(test20,test20)
#View(test20)
set.seed(111)
#build forest
my_forest <- randomForest(as.factor(train$sold_binary) ~ home_type + bedrooms +  year_built + lot_size_sq_footage + bathrooms+ finished_sq_footage,data=train, importance=TRUE, ntree = 1000)

my_prediction<- predict(my_forest, test)


ismy_solution <- data.frame(originalOutcome = test$sold_binary, outcome = my_prediction)
#display most important factors
varImpPlot(my_forest)
#displays original outcome and prediction
ismy_solution
#shows confusion matrix on training data not test data
my_forest
