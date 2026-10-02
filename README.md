# Getting Started 

## Access to GPU Workstations
Open terminal and ssh into one of the working stations (X--> your group number) using the provided credentials
```bash
ssh group_XX@university-hub.example
```


cd into your scratch folder 
```bash
cd /scratch/group_XX
```


## Get the Starter Repository (Once)
clone the starter repository into a new group repository (it will ask for your credentials)

```bash
git clone https://university-git.example/lecture-projects/bsem-ws26_starter.git bsem-ws26_groupX
cd bsem-ws26_groupX
```

rename starter from origin to starter, and instead add the group repository as origin for submission and synchronization between group members 

```bash
git remote rename origin starter
git remote add origin https://university-git.example/lecture-projects/bsem-ws26_groupX.git
git push -u origin main
```

test whether it worked 
```bash
git remote -v
```

This should show 
```bash
origin	https://university-git.example/lecture-projects/bsem-ws26_groupX.git (fetch)
origin	https://university-git.example/lecture-projects/bsem-ws26_groupX.git (push)
starter	https://university-git.example/lecture-projects/bsem-ws26_starter.git (fetch)
starter	https://university-git.example/lecture-projects/bsem-ws26_starter.git (push)
```

Second test
```bash
git status
```

This should show 
```bash
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

## Prerequisites for Running Code (Once)

### Create a symlink
Open terminal and ssh into one of the working stations (X--> your group number) using the provided credentials

```bash
ssh group_XX@university-hub.example
```

Create a symlink to access the scratch folder 
```bash
ln -s /scratch/<username> scratch
```

### Create a conda env

Test whether /opt/anaconda3/envs/course-env already exists 
```bash
conda env list
```

If it exists: 
```bash 
conda activate /opt/anaconda3/envs/course-env
python -m ipykernel install --user --name=course-env
```

If not, create it

```bash 
conda create -p /opt/anaconda3/envs/course-env python=3.14
conda activate /opt/anaconda3/envs/course-env
conda install ipykernel
python -m ipykernel install --user --name=course-env
conda install matplotlib
pip install "arbiter_analysis @git+https://example.invalid/course-tools.git"
```

### Open Jupyter
In your bowser open 
https://university-hub.example/hub/login?next=%2Fhub%2F

Login with your credentials.
Use the File Browser to navigate to your project directory (bsem-ws26_groupX)

make sure the kernel is course-env

# Daily Workflow

## SSH
```bash
ssh group_XX@university-hub.example
```

## Git 

**Start of a work session: get the latest changes**
```bash
git pull
```

**Check what you have changed locally**
```bash
git status        # which files are modified / untracked
git diff          # what exactly changed in tracked files
```

**Save and share your work**
```bash
git add <file1> <file2>     # stage specific files (recommended)
# or: git add --all         # stage everything, check `git status` first!
git commit -m "Short, descriptive message"
git pull                    # get teammates' changes first
git push
```

### Useful extras 

```bash
git log --oneline           # short commit history
git restore <file>          # discard local changes in a file (irreversible!)
```

### Tips

- **Commit small and often**, with meaningful messages (e.g. `Add results plot for Task 2`, not `changes`).
- **Always pull before you push.** If your push is rejected, run `git pull` and then push again.
- **Merge conflicts:** if `git pull` reports a conflict, open the marked files, resolve the
  `<<<<<<<` / `=======` / `>>>>>>>` sections, then `git add <file>` and `git commit`.
- **Don't commit** large generated files, credentials, or personal config. List them in a `.gitignore`.

## Jupyter 
In your bowser open 
https://university-hub.example/hub/login?next=%2Fhub%2F

Login with your credentials.
Use the File Browser to navigate to your project directory (bsem-ws26_groupX)


## Conda 
Any installations you make, affect everyone using the conda environment on that gpu workstation, so please coordinate! 

