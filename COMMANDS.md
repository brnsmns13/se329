# Pip
Pip is the python package manager. All pip commands should be executed from the se329/ (root) project directory with your virtual environment activated.

- `pip install -r requirements_dev.txt` - Installs python dependencies in the _active_ virtual environment according to se329/requirements_dev.txt.
- `pip uninstall <package>` - Uninstall a python dependency from the _active_ virtual environment.
- `pip freeze` - List all installed python dependencies on the _active_ virtual environment.


# Nosetests
Nose is a python library for executing unit tests.  All nosetests commands should be executed from the quiz/ (root) project directory.

- `nosetests --config=.noserc` - Executes all python unit tests in the project.
- `nosetests --with-gae --with-coverage --cover-erase --cover-min-percentage 100 --cover-package=.` - Full command for executing nosetests with coverage.


# Git
These are far from all possible git commands, but they are the primary commands used in a typical workflow. For more information on git, take a look at [Using Git and GitHub](https://iastate.box.com/shared/static/v8j3uc6phm8453yad2behbk837gvkkgi.pdf).

- `git clone <repo_https>` - Create a local directory containing all of the files from the repository (along with a pre-configured remote to the repo named "origin").
- `git remote add <fork_remote_name> <fork_https>` - Add a remote to a fork.
- `git fetch origin` - Update references to the origin remote (should always be done before checking out a new branch).
- `git checkout origin/master -b <branch_name>` - Create a new local branch based from the master branch on the origin remote.
- `git pull origin master` - Update the current branch with all new commits from the master branch on the origin remote (use sparingly - can cause merge conflicts).
- `git add -A` - Add all modified file to the list of files to be included in the next commit ("staged" files).
- `git commit -m "<commit_message>"` - Create a new commit from the staged files.
- `git push <fork_remote_name> <branch_name>` - Push the current branch up to your fork. You must first setup the remote.
- `git stash` - "Stash" current modified files on a stack without committing them.
- `git stash pop` - Re-apply modified files from the top of the stack.
- `git branch` - List all local branches.
- `git checkout <branch_name>` - Switch to another local branch.
- `git branch -D <branch_name>` - Delete a local branch.
- `git log` - List all commit history on the current branch.
