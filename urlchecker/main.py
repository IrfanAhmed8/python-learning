from check import isvalid,urlrequest,log_response,file_url
s=input('enter the url')

file_url()

if isvalid(s):
    response=urlrequest(s)
    if response:
        print(f'url is reachable with status{response}')
        log_response(s,f"reachable{response}")


    else:
        print("⚠️ URL is valid but not reachable (maybe offline or broken).")
        log_response(s,"not reachable")
else:
    print("url is not reachable")
