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
##  distributition with GLM.
glm_1 = glm(subscribed ~ ., family = binomial(), data = new_data)

summary(glm_1)

car::Anova(glm_1)

