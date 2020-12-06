# Reading the data
## Training data - Covariates
X_train_SMOTE = read.csv("./DATA/X_train_SMOTE.csv")
## Training data - Response Variable
y_train_SMOTE = read.csv("./DATA/y_train_SMOTE.csv", header = F)

# Need to convert the dummy variables into one categorical variable

## Job 
job_cols <- as.matrix(X_train_SMOTE[7:17])
job_cat <- factor(job_cols %*% 1:ncol(job_cols), 
       labels = c("job_admin", colnames(job_cols)))

## Marital status
marital_cols <- as.matrix(X_train_SMOTE[18:19])
marital_cat <- factor(marital_cols %*% 1:ncol(marital_cols), 
                      labels = c("marital_divorced", colnames(marital_cols)))
## Education
education_cols <- as.matrix(X_train_SMOTE[20:22])
education_cat <- factor(education_cols %*% 1:ncol(education_cols), 
                      labels = c("education_primary", colnames(education_cols)))
## Month
month_cols <- as.matrix(X_train_SMOTE[23:33])
month_cat <- factor(month_cols %*% 1:ncol(month_cols), 
                      labels = c("month_apr", colnames(month_cols)))
## Poutcome
poutcome_cols <- as.matrix(X_train_SMOTE[34:36])
poutcome_cat <- factor(poutcome_cols %*% 1:ncol(poutcome_cols), 
                        labels = c("poutcome_failure", colnames(poutcome_cols)))
## Contact
contact_cols <- as.matrix(X_train_SMOTE[37:38])
contact_cat <- factor(contact_cols %*% 1:ncol(contact_cols), 
                       labels = c("contact_cellular", colnames(contact_cols)))

# Creating a new dataframe
new_data <- X_train_SMOTE[1:6]

# Adding the newly created categorical variables to the dataframe
new_data["job"] <- factor(gsub("job_", "", job_cat))
new_data["marital"] <- factor(gsub("marital_", "", marital_cat))
new_data["education"] <- factor(gsub("education_", "", education_cat))
new_data["month"] <- factor(gsub("month_", "", month_cat))
new_data["poutcome"] <- factor(gsub("poutcome_", "", poutcome_cat))
new_data["contact"] <- factor(gsub("contact_", "", contact_cat))

# Adding response variable to the dataframe
new_data["subscribed"] <- y_train_SMOTE


## Since outcome variable is dichotomous we will use binomial response
##  distribution with GLM.
glm_1 = glm(factor(subscribed) ~ ., family = binomial(), data = new_data)

summary(glm_1)

car::Anova(glm_1)

new_data_subset <- new_data[-c(31856), ]

glm_temp = glm(factor(subscribed) ~ ., family = binomial(),
               data = new_data_subset)

summary(glm_temp)

car::Anova(glm_temp)

car::avPlot(glm_temp, variable = "balance")

car::avPlot(glm_temp, variable = "day")

X_valid = read.csv("./DATA/X_valid.csv")

y_valid = read.csv("./DATA/y_valid.csv", header = F)

## Job 
job_cols <- as.matrix(X_valid[7:17])
job_cat <- factor(job_cols %*% 1:ncol(job_cols), 
                  labels = c("job_admin", colnames(job_cols)))

## Marital status
marital_cols <- as.matrix(X_valid[18:19])
marital_cat <- factor(marital_cols %*% 1:ncol(marital_cols), 
                      labels = c("marital_divorced", colnames(marital_cols)))
## Education
education_cols <- as.matrix(X_valid[20:22])
education_cat <- factor(education_cols %*% 1:ncol(education_cols), 
                        labels = c("education_primary", colnames(education_cols)))
## Month
month_cols <- as.matrix(X_valid[23:33])
month_cat <- factor(month_cols %*% 1:ncol(month_cols), 
                    labels = c("month_apr", colnames(month_cols)))
## Poutcome
poutcome_cols <- as.matrix(X_valid[34:36])
poutcome_cat <- factor(poutcome_cols %*% 1:ncol(poutcome_cols), 
                       labels = c("poutcome_failure", colnames(poutcome_cols)))
## Contact
contact_cols <- as.matrix(X_valid[37:38])
contact_cat <- factor(contact_cols %*% 1:ncol(contact_cols), 
                      labels = c("contact_cellular", colnames(contact_cols)))

# Creating a new dataframe
new_data_valid <- X_valid[1:6]

# Adding the newly created categorical variables to the dataframe
new_data_valid["job"] <- factor(gsub("job_", "", job_cat))
new_data_valid["marital"] <- factor(gsub("marital_", "", marital_cat))
new_data_valid["education"] <- factor(gsub("education_", "", education_cat))
new_data_valid["month"] <- factor(gsub("month_", "", month_cat))
new_data_valid["poutcome"] <- factor(gsub("poutcome_", "", poutcome_cat))
new_data_valid["contact"] <- factor(gsub("contact_", "", contact_cat))

# Adding response variable to the dataframe
new_data_valid["subscribed"] <- y_valid

glm_1_pred = predict(glm_1, newdata = new_data_valid[1:12], type = "r")

temp_pred = as.factor(ifelse(glm_1_pred > 0.5, 1, 0))

caret::confusionMatrix(temp_pred, as.factor(y_valid$V1), positive = "1")


glm_1_pred_temp = predict.glm(glm_temp, newdata = new_data_valid[1:12], type = "r")

temp_pred = as.factor(ifelse(glm_1_pred_temp > 0.5, 1, 0))

caret::confusionMatrix(temp_pred, as.factor(y_valid$V1), positive = "1")

glm_2_pred = predict.glm(glm_2, newdata = new_data_valid[1:12], type = "r")

temp_pred = as.factor(ifelse(glm_2_pred > 0.5, 1, 0))

caret::confusionMatrix(temp_pred, as.factor(y_valid$V1), positive = "1")


glm_3_pred = predict(glm_3, newdata = new_data_valid[1:12], type = "r")

temp_pred = as.factor(ifelse(glm_3_pred > 0.5, 1, 0))

table(temp_pred, y_valid$V1)


car::avPlot(glm_1, "balance")

car::avPlot(glm_1, "day")

X_test = read.csv("./DATA/X_test.csv")

y_test = read.csv("./DATA/y_test.csv", header = F)

## Job 
job_cols <- as.matrix(X_test[7:17])
job_cat <- factor(job_cols %*% 1:ncol(job_cols), 
                  labels = c("job_admin", colnames(job_cols)))

## Marital status
marital_cols <- as.matrix(X_test[18:19])
marital_cat <- factor(marital_cols %*% 1:ncol(marital_cols), 
                      labels = c("marital_divorced", colnames(marital_cols)))
## Education
education_cols <- as.matrix(X_test[20:22])
education_cat <- factor(education_cols %*% 1:ncol(education_cols), 
                        labels = c("education_primary", colnames(education_cols)))
## Month
month_cols <- as.matrix(X_test[23:33])
month_cat <- factor(month_cols %*% 1:ncol(month_cols), 
                    labels = c("month_apr", colnames(month_cols)))
## Poutcome
poutcome_cols <- as.matrix(X_test[34:36])
poutcome_cat <- factor(poutcome_cols %*% 1:ncol(poutcome_cols), 
                       labels = c("poutcome_failure", colnames(poutcome_cols)))
## Contact
contact_cols <- as.matrix(X_test[37:38])
contact_cat <- factor(contact_cols %*% 1:ncol(contact_cols), 
                      labels = c("contact_cellular", colnames(contact_cols)))

# Creating a new dataframe
new_data_test <- X_test[1:6]

# Adding the newly created categorical variables to the dataframe
new_data_test["job"] <- factor(gsub("job_", "", job_cat))
new_data_test["marital"] <- factor(gsub("marital_", "", marital_cat))
new_data_test["education"] <- factor(gsub("education_", "", education_cat))
new_data_test["month"] <- factor(gsub("month_", "", month_cat))
new_data_test["poutcome"] <- factor(gsub("poutcome_", "", poutcome_cat))
new_data_test["contact"] <- factor(gsub("contact_", "", contact_cat))

# Adding response variable to the dataframe
new_data_test["subscribed"] <- y_test
