import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("kyphosis.csv")

print(df.head())
df.info()

sns.pairplot(df, hue="Kyphosis", palette="Set1")
plt.show()

x = df.drop("Kyphosis", axis=1)
y = df["Kyphosis"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()

dtree.fit(X_train, y_train)

predictions = dtree.predict(X_test)

df2 = pd.DataFrame(list(zip(y_test, predictions)), columns = ['y_test', 'predictions'])

print(df2.head())

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))

from IPython.display import Image  
from six import StringIO  
from sklearn.tree import export_graphviz
import pydot 

features = list(df.columns[1:])
print("Features: \n", features)

dot_data = StringIO()  
export_graphviz(dtree, out_file=dot_data,feature_names=features,filled=True,rounded=True)

graph, = pydot.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())