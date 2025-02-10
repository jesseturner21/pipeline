import unittest
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

class TestIrisProject(unittest.TestCase):
  def setup(self):
    self.iris = load_iris()
    self.X = self.iris.data
    self.y = self.iris.target
    self.feature_names = self.iris.feature_names
    self.target_names = self.iris.target_names

  def test_data_loading(self):
    self.assertEqual(self.X.shape, (150, 4))
    self.assertEqual(self.y.shape, (150,))
    self.assertEqual(len(self.feature_names), 4)
    self.assertEqual(len(self.target_names), 3)

  def test_missing_and_duplicates(self):
    df = pd.Dataframe(self.X, columns= self.feature_names)
    self.assertTrue(df.isnull().sum().sum() == 0)

    duplicate_count = data.duplicated().sum()

    if duplicate_count > 0:
      print(f"number of duplicate rows: {duplicate_count})
      data.drop_duplicates(inplace=True)
    
