## **Creating venv**
--
**MLOPS(Main Folder) ==> Sim_Lin_Reg (Sub_Foldr) --> Create venv in sub_folder**

#### Command to create new folder or file
New-Item file_name

#### Deleting folder
Remove-Item "folder_name" -Recurse -Force

- Making directory like **.gitignore** and  **requirement.txt**<br>
1. ***New-Item .gitignore***<br>
2. ***pip freeze > requirements.txt*** <br>
3. ***pip install -r requirements.txt*** --> command to install required files

### Intalling required files with given names, write inside of **requirement.txt** file
```python
numpy
pandas
scikit-learn
matplotlib
seaborn
mlflow
dvc
```

### Files to be included inside of **.gitignore** which are not required to push to github
```python
.venv/ 
__pycache__
*.pyc 
mlruns/
.ipynb_checkpoints
.env
```

### Create ***venv*** inside of the ***Sim_Lin_Reg***
- python -m venv .venv --> creating virtual environment
- .\.venv\Scripts\Activate.ps1 --> activate venv
- **deactivate** --> current working environment
- **Remove-Item .venv -Recurse -Force** --> remove venv

#### **.ven** distinct the project from environment instance otherwise writing **venv** might mix the project from supporting folder which helps to build the project. dot(.) makes folder hidden without dot, the folder will be treated as normal folder.

***git init*** and ***dvc git*** should be initilized in the project root directory. The project root directory is the directory of specific project the developer is working on. The **Sim_Lin_Reg** is project root directory and **MLOPs** is general directory which might contains multiple projects of similar nature unlike project root directory; only contains the specific project files.
```python
(.venv) PS D:\MLOps\Sim_Lin_Reg> 
```
**NOTE:** **dvc git** git repo need to be initilized before initilizing the dvc otherwise **dvc init** will scans your current folder for a  **.git** directory. If it doesn't find one, it doesn't know how to integrate its tracking with your code versions.

**(.venv) PS D:\MLOps\Sim_Lin_Reg\scr>** ==> Create files **__init__.py** and **config.py** inside of the scr folder and similarely create other project files

Command to move one file to another 
```python
Move-Item src\data src\sim_lin_reg\
```
Command to rename

```python
Rename-Item -Path "scr" -NewName "src"
Rename-Item src\project load_data
```
command to create files and folder from project root directory
```python
(.venv) PS D:\MLOps\Sim_Lin_Reg> New-Item -ItemType File -Path "src\project\config.py"
New-Item -ItemType File -Path "src\project\data\__init__.py"
```
Move file form one folder to another (Source to destination)
```python
D:\MLOps\Sim_Lin_Reg> Move-Item src\project\config.py, src\project\__init__.py src\
```
Making files/folder form another folder location in hierarchical apprach.
```python
PS D:\MLOps\Sim_Lin_Reg\src> mkdir load_data\load_data.py
```
Removing directory 
```python
Remove-Item load_data\load_data.py -Confirm
```