# Imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import numpy as np
import subprocess
import argparse
import wandb
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Set random seed
seed = 42

# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-k", "--key", required=True,
	help="wandb API key")
args = vars(ap.parse_args())

# Set wandb up
print(wandb.login(key=args["key"]))
print(wandb.init(project="wandb-github-actions", entity="sayakpaul"))

################################
########## DATA PREP ###########
################################

# Load in the data
df = pd.read_csv("wine_quality.csv")

# Split into train and test sections
y = df.pop("quality")
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=seed)

#################################
########## MODELLING ############
#################################

# Fit a model on the train section
regr = RandomForestRegressor(max_depth=5, random_state=seed)
regr.fit(X_train, y_train)

# Report training set score
train_score = regr.score(X_train, y_train) * 100
# Report test set score
test_score = regr.score(X_test, y_test) * 100

# Log plots for the regressor
wandb.sklearn.plot_regressor(regr, X_train, X_test, y_train, y_test)

# More logging
# This will be exported as a run artifact
api = wandb.Api()
run = api.run(f"{wandb.run.entity}/{wandb.run.project}/{wandb.run.id}")
metrics_dataframe = run.history()
metrics_dataframe.to_csv("metrics.csv")

# Generate a file containing the rul URL
with open("run.txt", "w") as f:
	f.write(wandb.run.get_url())
f.close()

# # Create a comment on the commit
# # Credits:
# # https://github.community/t/automatic-commenting-on-a-commit-with-results-from-a-script/129529/6?u=sayakpaul
print("Set git config...")
subprocess.Popen(["git", "config", "--global", "user.name", "github-actions[bot]"])
subprocess.Popen(["git", "config", "--global", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"])

print("Push to remote...")
subprocess.Popen(["git", "add", "-f", "run.txt"])
subprocess.Popen(["git", "commit", "-m", wandb.run.get_url()])
subprocess.Popen(["git", "push"])