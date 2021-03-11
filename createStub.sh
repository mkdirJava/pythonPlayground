#!/bin/bash

 

export set codeGenFile=swagger-codegen-cli.jar

# Download the swagger code gen binary if not in the local directory
if [ ! -f ${codeGenFile} ]; then
    echo " downloading binary for Api Stub creation"
    wget https://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.4.17/swagger-codegen-cli-2.4.17.jar -O ${codeGenFile}
    chmod 755 "./${codeGenFile}"
    else 
    echo "Not downloading binary, you already have it"
fi

# Use the code gen to generat the stub 
echo "Generating stub START"
    java -jar "./${codeGenFile}" generate -i ./swagger.yaml -l python-flask -o ./stubbedWeb
echo "Generating stub FINISH"

echo "Moving files to none volitile space"

if [ ! -d "app" ]; then
    echo "creating a web directory"
    mkdir app
fi
