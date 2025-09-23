import socket 
import os 
import sys  
import datetime 



HOST = '127.0.0.1' # default ip address if not explicitly passed as cmd arg
PORT = 8080 # by default http server listens on port 8080 
RESOURCES_DIR = "resources" # directory from where html files will be served as response from server
BUFFER_SIZE = 4096 # max size of http request we can handle 

# step1 - enable command line arg for host and port 
"""
server.py    8080         127.0.0.1
sys.argv[0]  sys.argv[1]  sys.argv[2]
"""
if len(sys.argv)>1: # if there are more than 1 arguement. 0th arg is the script name - server.py
    PORT = int(sys.argv[1])
if len(sys.argv)>2:
    HOST = sys.argv[2]


# step2 - define the helper functions to be used later in the code 
def httpDate(): 
    now = datetime.datetime.now(datetime.timezone.utc) 
    return now.strftime("%a, %d %b %Y %H:%M:%S GMT") # eg - Tue, 23 Sep 2025 9:25:42 GMT 

def buildResponse(statusCode, statusMessage, body="", contentType="text/html" ):
        """
        Construct a valid HTTP/1.1 response. HTTP/1.1 is the version of HTTP. A valid HTTP/1.1 response must
        follow the format defined by the HTTP/1.1 specification

        status_code: e.g., 200
        status_message: e.g., "OK"
        body: response body (HTML string)
        content_type: default "text/html"
        """
        bodyEncoded = body.encode('utf-8')
        # headers will be a list of strings
        header = [
             f"HTTP/1.1 {statusCode} {statusMessage}",# this line is a must - the very first line in a response
             f"Date: {httpDate()}", # also a must 2nd line - date
             "Server: Simple HTTP server", # must 3rd line - name of the server
             f"Content-Type: {contentType}", # must 4th line - content type - text/html - an arg of fn
             f"Content-Length: {len(bodyEncoded)}", # must 5th line - content length - its the length of body
             "", # must 6th - to mark end of header
             "" # must 7th - before the body starts

        ]
        # \r\n means - Go to the beginning of the next line
        """
        Take a list of headers (like ["Date: ...", "Content-Type: ...", "Content-Length: ..."])
        and join them into one string, separating each with CRLF (\r\n).

        Date: Tue, 23 Sep 2025 12:00:00 GMT\r\n
        Content-Type: text/html; charset=UTF-8\r\n
        Content-Length: 48\r\n
        etc...\r\n
        """
        headerStr = "\r\n".join(header)
        return headerStr.encode('utf-8') + bodyEncoded

def errorPage(code, message, description):
     # to generate a simple HTML error page when something wrong happens
     return f"""
<!DOCTYPE html>
<html>
<head>
<title>An Error has occured</title>
</head>
<body>
<h1>{code} {message}</h1>
<p>{description}</p>
</body>
</html>            
"""

def isSafePath(base,path):
    # convert base to absolute path. Example: base - ./resources
    # os.path.abspath() will convert it to - /home/user/project/resources - absBase
    absBase = os.path.abspath(base)
    # convert base+(user sent path) to absolute path. Example: ./resources + ../../etc/passwd 
    # so absolute path of this would be - /home/user/etc/passwd - absBaseAndTarget
    absBaseAndTarget = os.path.abspath(os.path.join(base,path))
    # check if absBaseAndTarget starts with /home/user/project/resources
    # in this case, it doesn't - so the path sent by user is unsafe - can lead to path traversal attack
    # so return false
    return absBaseAndTarget.startswith(absBase) # returns a boolean


def handleRequest(reqData): # function to parse HTTP req from user and send appropriate response
    try:
        reqDecoded = reqData.decode('utf-8')
        lines = reqDecoded.split("\r\n") 
        reqLine = lines[0] # # First line of req body - METHOD PATH VERSION
        print(f"request: {reqLine}")
        # now splitting the first line of HTTP req body itself  
        parts = reqLine.split() 
        if len(parts)!=3:
            body = errorPage(400, "Bad Request", "Malformed HTTP request") 
            return buildResponse(400, "Bad Request",body) 
        method, path, version = parts # destructured path 
        if method != "GET": # since our server only support GET requests
            body = errorPage(400, "Method Not Allowed", "Only GET is supported") 
            return buildResponse(400, "Method Not Allowed",body) 
        # default path
        if path=="/":
            path = "/index.html"
        if not isSafePath(RESOURCES_DIR, path.lstrip("/")):
            body = errorPage(400, "Forbidden", "Access Denied") 
            return buildResponse(400, "Forbidden",body) 
        filePath = os.path.join(RESOURCES_DIR, path.lstrip("/"))
        if not os.path.exists(filePath):
            body = errorPage(404, "Not Found", "Requested resource doesn't Exist") 
            return buildResponse(404, "Not Found")  
        # if everything is fine 
        with open(filePath, "r", encoding="utf-8") as f: 
            content = f.read()
        return buildResponse(200, "OK", content)
    
            
    except Exception as e: 
        body = errorPage(500, "Internal Server Error", f"Server encountered an error: {e}")
        return buildResponse(500, "Internal Server Error", body)
    
    
def startServer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT)) 
        s.listen() 
        conn, addr = s.accept() 
        print(f"Connected by {addr}")
        try:
            while True:
                reqData = conn.recv(BUFFER_SIZE) 
                if not reqData:
                    break; 
                if reqData.decode('utf-8').lower()=="exit":
                    break
                response = handleRequest(reqData) 
                conn.sendall(response) 
        except KeyboardInterrupt:
            print("Shutting down gracefully...")
   
if __name__ == "__main__":
       startServer()
				

				
