@ECHO OFF
%1 start mshta vbscript:createobject("wscript.shell").run("""%~0"" ::",0)(window.close)&&exit
start /b python D:/��Դ/java/forNowCoder/py/uploadedToServer.py