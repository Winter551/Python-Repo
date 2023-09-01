import requests

r = requests.get("http://172.25.0.29/index.php")

web_headers = r.headers
print("Here are the headers:")
print(web_headers)

web_html = r.text
print("Here is the html returned in the body of the webpage")
print(web_html)

web_status_code = r.status_code
print("Here is the HTTP status code")
print(web_status_code)

web_cookies = r.cookies
print("Here are the cookies from the page")
print(web_cookies)
