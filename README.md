
# A continueing toolbox 

## Questions to answer

### Overriding question

    How do I develop a web api using Python?

1.  How do I get typing with Python like NodeJs?
    * Looks like Python goes down the road of linting checks, there are lot of linters. 
    * The project uses MyPy:
      * Can be tempermental, the mypy_cache needs to be kept up to date to prevent large parsing, ie it parses as you develop
      * To setup
        * VsCode install python, mypy extenstion
        * I had to install the mypy language server too via
          * python3 pip install venv
          * python3 -m venv ~/.mypyls
          * ~/.mypyls/bin/pip install "https://github.com/matangover/mypyls/archive/master.zip#egg=mypyls[default-mypy]"
          * then restart vscode
          * Vs Code might then ask again to install mypy extension, if so install it and it will parse the code and build that cache
          * ctrl + shift + p to open vscode commands, type "pythonL Select linter" go for mypy
      * To see it in action, open <projectRoot>/app/PersonService/PersonTest.py, theres a method that accepts a Teacher but is getting a student
      * you can run the command below to do a lint run, there is also a deamon option, I think thats what the Vscode extension uses
        * mypy app
  
2.  Tools for creation of REST API stubs?
    * Swagger jar can generate stubs based upon a spec, (client and server). Python implememtation is connexion built on top of flask
  
3.  How to debug?
    * Debugging is dependant on the IDE in use or if none there is a default on cmd version
      * This project used VSCode:
        * execute the below command in the app directory, this will start the server
          * python3 -m debugpy  --listen 0.0.0.0:5678   swagger_server
        * go into VScode and go to the debug pannel ( fourth on the left bar), run "Python swagger", this will attach the source code to the debugger

4.  How does Python do Unit testing?
    * quite nicley, allot like Golang. 
      * look at <rootProject>/app/PersonService/PersonRepo.py , you can run it on the command line
        * python3 <rootProject>/app/PersonService/PersonRepo.py
        * or 
        * go the file in VScode and click the play button, top right
  
5.  The use of pipenv ( dependency management )
   * To handle dependencies you use a virtual env, this means the host machines installation of python / pip /pip3  wont be affected. 
   * It also means if all depedencies are declared in this virtualenv then repeatable runs / common development can happen

6.  Anything wierd found?
    *  The buildtool to package the project as a pip module and the use of pipenv are seperate. If images are the distribution then its fine as the docker file is generated from answer to question 2
  
## Workflow

Create the stubs and copy over files for more persistent cut
  generate the swagger API
  place it at project root
  run createStub.sh
    this will generate the stubs at stubbedWeb
  copy over the files you want from stubbedWeb to app, 
    typically the controllers and definatley the swagger_server/swagger/swagger.yaml
  You can then create the image
    docker -t python-image <rootProject>/app/
