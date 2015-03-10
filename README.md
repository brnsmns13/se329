# Contact Information
### Project 2
| Name | Position | Username | Email | Phone |
| ---- | -------- | -------- | ----- | ----- |
| Zachary Belloma | ??? | zbelloma | zbelloma@iastate.edu | ??? |
| Tyler Cobb | ??? | Tcobbs72 | tjcobb@iastate.edu | 612-963-1237 |
| William Park | ??? | wipark93 | wipark@iastate.edu | ??? |
| Brian Simons | ??? | brnsmns13 | bcsimons@iastate.edu | 319-651-0782 |

### Project 3
| Name | Position | Username | Email | Phone |
| ---- | -------- | -------- | ----- | ----- |
| Tyler Cobb | Systems Engineer | Tcobbs72 | tjcobb@iastate.edu | 612-963-1237 |
| Robert Kloster | Project Manager | RobertKloster | rkloster@iastate.edu | 515-720-5986 |
| Branden Lange | Quality Control | CivBase | blange@iastate.edu | 515-975-7491 |
| Brian Simons | Architect / Developer | brnsmns13 | bcsimons@iastate.edu | 319-651-0782 |

# Resources
### Project 2
- [Team Documents](???)

### Development Tools
- [draw.io](https://www.draw.io/) - Flowchart and UML diagram creation web application
- [Git](http://git-scm.com/) - Version control system
- [PyCharm](https://www.jetbrains.com/pycharm/) - Python interactive development environment

##### CSS
- [Bootstrap](http://getbootstrap.com/) - CSS style framework

##### Javascript
- [jQuery](http://jquery.com/) - Library for DOM querying and AJAX requests
- [NPM](https://www.npmjs.com/) - Javascript package manager (part of [NodeJS](http://nodejs.org/))

##### Python
- [Google Appengine](https://cloud.google.com/appengine/docs/python/gettingstartedpython27/introduction) - Web server framework
- [Jinja2](http://jinja.pocoo.org/docs/dev/) - HTML templating language for python
- [pip](https://pip.pypa.io/en/latest/) - Python package manager
- [webapp2](https://webapp-improved.appspot.com/) - Web server library/framework

# Configuration
### Git Setup
1. Download and install Git from [here](http://git-scm.com/downloads). Make sure you allow the installer to add Git to your system path!
2. Open Git Bash and navigate to the directory where you want your project directory to be located (I recommend ~/workspace) and clone the repository with `git clone https://github.com/brnsmns13/se329.git` or `git clone git@github.com:brnsmns13/se329.git` if you  have SSH key set up. Setting up SSH keys will allow you to avoid typing in your password every time you push/pull, but it is not necessary.
3. From within your project directory (e.g. ~/workspace/se329) configure Git to use the correct user with `git config user.name <username>` and `git config user.email <email>`. Be sure to use the same username and email as you use for your GitHub account.
4. Check out these [Using Git and GitHub](https://drive.google.com/a/iastate.edu/file/d/0B46XQUsoCZSwRDFpVGRuaHNwV1U/view) instructions for more information.
5. Check out COMMANDS.md for more information on git commands.

### Python Setup
1. If you're on Windows, install [Git](http://git-scm.com/downloads) first. I have found that Git's Git Bash terminal is much easier and more convenient than Command Prompt or Power Shell because of its Git, virtualenv, and bash support. All of my Windows instructions depend on you using Git Bash, so you may need to get creative otherwise.
2. Download and install Python 2.7 from [here](https://www.python.org/downloads/). It is important to get Python 2.7 and not Python 3.4.
3. Download and install the python package manager "pip" from [here](https://pip.pypa.io/en/latest/installing.html). If you have Python 2.7.9 or higher, pip will already be installed with python and this step can be skipped.
4. Add python and pip to your "Path" system environment variable. On Windows, open the system environment variables dialog and, for a standard Python 2.7.9 installation, you can just append `;C:\Python27\;C:\Python27\Scripts` to the end of the existing value (restart any terminals for it to take effect). On a UNIX machine, just add the lines `export PATH="/Library/Frameworks/Python.framework/Versions/2.7/bin:$PATH"` and `export PATH="/Library/Frameworks/Python.framework/Versions/2.7/bin/pip:$PATH"` to your ~/.bash_profile file (restart any terminals for it to take effect).
5. Check out COMMANDS.md for more information on python and pip commands.

### Appengine Setup
1. Download and install the Appengine SDK form [here](https://cloud.google.com/appengine/downloads).
2. Startup the newly-installed Appengine Launcher application and click the add button (plus icon in the bottom left).
3. Choose the se329 (root) project directory and click the "Create" button to add it to your list (it is named better-than-clickers-quiz-app).

# Execution
1. Open the Appengine Launcher, select the better-than-clickers-quiz-app application and then click the big green "Run" button in the top left of the window.
2. Click the "Browse" button at the top of the launcher window to open the app in your browser.

# Contributing
1. Do not push directly to the repository. Instead, create a fork using the "Fork" button at the top-right of the repository page.
2. Add the fork to your local workspace by navigating to the project directory and using the command `git remote add <fork_name> <fork_https>`. The fork name can be anything, but I prefer to use my own name. By using names, I can easily add remotes to access other forks and easily distinguish between them. The fork https url can be found on the fork's GitHub page.
3. Use `git push <fork_name> <branch_name>` to push branches to your fork. From there, you can create a pull request onto master in the "origin" repository. This allows us to review contributions and keep track of all changes.

__Note:__ All code used by this project should conform to [pep8 standards](https://www.python.org/dev/peps/pep-0008/). It seems trivial, but formatting standards make large-scale development much easier, so please try to adhere to it. PyCharm will automatically notify you of any lines which do not adhere to pep8 standards in the bar on the right of the editor.
