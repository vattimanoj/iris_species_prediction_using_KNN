import pandas as pd
import pickle
import sys
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
warnings.filterwarnings("ignore")
class KNN:
    def __init__(self,path):
        try:
            self.df  = pd.read_csv(path)
            self.df = self.df.drop(['Id'],axis=1)
            d={}
            for i in range(len(self.df['Species'].unique())):
                d[self.df['Species'].unique()[i]]=i
            self.df['Species']=self.df['Species'].map(d)
            self.x=self.df.iloc[:,:4]
            self.y=self.df.iloc[:,-1]
            self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(self.x,self.y,test_size=0.2,random_state=42)
        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
            print(f"Error in line no : {er_line.tb_lineno} : due to : {er_msg} : reason : {er_ty}")
    def train(self):
        try:
            self.reg=KNeighborsClassifier()
            self.reg.fit(self.X_train,self.y_train)
            self.y_pred=self.reg.predict(self.X_train)
            print("train performance")
            print("confusion matrix:\n",confusion_matrix(self.y_train,self.y_pred))
            print("accuracy:",accuracy_score(self.y_train,self.y_pred))
            print("classification_report:",classification_report(self.y_train,self.y_pred))
            print("___________________________________________________________________________")

        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
            print(f"Error in line no : {er_line.tb_lineno} : due to : {er_msg} : reason : {er_ty}")
    def test(self):
        try:
            self.reg=KNeighborsClassifier()
            self.reg.fit(self.X_test,self.y_test)
            self.y_t_pred=self.reg.predict(self.X_test)
            print("test performance")
            print("confusion matrix:\n",confusion_matrix(self.y_test,self.y_t_pred))
            print("accuracy:",accuracy_score(self.y_test,self.y_t_pred))
            print("classification_report:",classification_report(self.y_test,self.y_t_pred))
            print("___________________________________________________________________________")
        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
            print(f"Error in line no : {er_line.tb_lineno} : due to : {er_msg} : reason : {er_ty}")
    def save_model(self):
        try:
             with open('model.pkl', 'wb') as f:
                 pickle.dump(self.reg, f)
        except Exception as e:
             er_ty, er_msg, er_line = sys.exc_info()
             print(f"Error in line no : {er_line.tb_lineno} : due to : {er_msg} : reason : {er_ty}")
    def test_model(self,a):
        try:
             print("the Flower:",self.reg.predict(a)[0])
        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
            print(f"Error in line no : {er_line.tb_lineno} : due to : {er_msg} : reason : {er_ty}")
if __name__ == "__main__":
    obj=KNN("iris.csv")
    obj.train()
    obj.test()
    obj.save_model()
    obj.test_model([[7.7,3.6,6,2]])
