echo [$(date)]: "START"
echo [$(date)]: "creating environment"
conda create -p svd_py python=3.9 -y
echo [$(date)]: "activate environment"
conda activate svd_py/

echo [$(date)]: "install requirements"
pip install -r requirements.txt
echo [$(date)]: "export conda environment"
conda env export > conda.yaml
echo "# ${PWD}" > README.md
echo [$(date)]: "first commit" 
# git init
# git remote add origin github_link
# git branch -M main
# git add .
# git commit -m "first commit"
# git push -u origin main
echo [$(date)]: "END"

# to remove everything -
# rm -rf venv/ .gitignore conda.yaml README.md .git/
