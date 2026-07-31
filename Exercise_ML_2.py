#1

"""
1. Binary
2. Multiclass
3. Binary
4. Binary
5. Multiclass
"""

#2
"""
1. 0.91 class 1             class 1=positive
2. 0.72 class 1
3. 0.49 class 0             class 0=negative
4. 0.21 class 0
5. 0.50 class 1
 
"""
#3
"""
if we calulate the sigmoide function ie 
Probality =  1/{1+E(raised to power Z)}
p=1/1+e(-5.2025)
p=0.9945
as probality is nearby 1 so we assign the class 1 to it
"""
#4
"""
Dataset -Age,BP,Cholesterol,Heart Disease
features-all except heart disease
target- heart disease

classification type-binary classification
"""
#5
"""
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score
df=pd.read_csv("heart.csv")
X=df.drop(columns=["HeartDisease"])
X = pd.get_dummies(X, drop_first=True)
y=df["HeartDisease"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=42) 
model=LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)
predictions=model.predict(X_test)
print("Accuracy")
print(accuracy_score(y_test,predictions))
print("Precision")
print(precision_score(y_test,predictions))
80:20 has highest accuracy and precission so we have to use it
"""
#6
"""
threshold: 0.5
class 0: .47,.31
remaing belongs to class 1
threshold :.7
class 0 : .65,.52,.31,.47
remaing belongs to class 1
changed class observations are :
0.65,0.52
"""    
#7
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score
df=pd.read_csv("heart.csv")
X=df.drop(columns=["HeartDisease"])
X=pd.get_dummies(X, drop_first=True)
y=df["HeartDisease"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)
y_predict=model.predict(X_test)
print("accuracy :")
print(accuracy_score(y_test,y_predict))
print("Precision :")
print(accuracy_score(y_test,y_predict))

"""

#8
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score,confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("heart.csv")
X=df.drop(columns=["HeartDisease"])
X=pd.get_dummies(X, drop_first=True)
y=df["HeartDisease"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)
y_predict=model.predict(X_test)
print("accuracy :")
print(accuracy_score(y_test,y_predict))
print("Precision :")
print(accuracy_score(y_test,y_predict))
cm=confusion_matrix(y_test,y_predict)
plt.figure(figsize=(6,6))
plt.subplot(1,2,1)
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["NO Disease","Disease"],
    yticklabels=["NO Disease","Disease"]
)
plt.xlabel("Predicted label")
plt.ylabel("Actual label")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()




"""
#9
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("diabetes.csv")
print(df.describe())
print(df.info())
print(df.isnull())
print(df.duplicated())
df=df.dropna()
df=df.drop_duplicates()
df.to_csv("diabetes.csv",index=False)
X=df.drop(columns=["Outcome"])
X=pd.get_dummies(X,drop_first=True)
y=df["Outcome"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)
y_predict=model.predict(X_test)
print(f"Accurecy is  {accuracy_score(y_test,y_predict)}")
print(f"Percision is  {precision_score(y_test,y_predict)}")
print(f"recall is  {recall_score(y_test,y_predict)}")
print(f"F1 is  {f1_score(y_test,y_predict)}")
cm=confusion_matrix(y_test,y_predict)
plt.figure(figsize=(6,6))
plt.subplot(2,2,1)
sns.heatmap(
    cm,
    annot =True,
    fmt="d",
    cmap="Blues",
    xticklabels=["No Diabetes","Diabetes"],
    yticklabels=["No Diabetes","Diabetes"]
)
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.title("Confusion Matrix")

plt.tight_layout
plt.show()
"""
#10
'''
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score
df=pd.read_csv("heart.csv")
X=df.drop(columns=["HeartDisease"])
X = pd.get_dummies(X, drop_first=True)
y=df["HeartDisease"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)
predictions=model.predict(X_test)
print("Accuracy")
print(accuracy_score(y_test,predictions))
print("Precision")
print(precision_score(y_test,predictions))
'''
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,accuracy_score
df=pd.read_csv("heart_2.csv")
X=df.drop(columns=["HeartRiskScore"])
X = pd.get_dummies(X, drop_first=True)
y=df["HeartRiskScore"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model=LinearRegression()
model.fit(X_train,y_train)
predictions = [0.2, 0.8, 0.4, 0.9]
predictions = (predictions >= 0.5).astype(int)

print("Accuracy:", accuracy_score(y_test, predictions))
