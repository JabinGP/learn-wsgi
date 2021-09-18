# WSGI server in Python
from wsgiref.simple_server import make_server


# 实现一个 wsgi 规范的 Application
def application(
        # 请求参数通过 environ 环境变量传递, 与曾经的 cgi 规范有关
        environ,
        # 用于向服务器发送 http 响应的 status 和 headers
        start_response
):

    print(environ)
    method = environ["REQUEST_METHOD"]
    if method == "POST":
        return _app_post(environ, start_response)

    return _app_get(environ, start_response)


def _app_get(environ, start_response):
    # 准备返回参数
    status = "200 OK"
    response_body = "HelloWorld!"
    response_headers = [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(response_body))),
    ]

    # 返回 http status 和 headers
    start_response(status, response_headers)
    # 返回 http body
    return [bytes(response_body, encoding="utf8")]


def _app_post(environ, start_response):
    # 读取输入
    req_body_size = 0
    try:
        req_body_size = int(environ.get("CONTENT_LENGTH", 0))
    except(ValueError):
        req_body_size = 0

    # http req body 会被封装成一个 BufferReader 对象保存在 env["wsgi.input"]
    # 利用 environ 中的 content_length 可以准确地读出请求内容
    req_body = environ["wsgi.input"].read(req_body_size)
    print("wsgi.input %s" % environ["wsgi.input"])
    print("req_body_size %s" % req_body_size)
    print("req_body %s" % req_body)

    # 准备返回
    status = "200 OK"
    response_body = "HelloWorld!"
    response_headers = [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(response_body)))
    ]
    # 返回
    start_response(status, response_headers)
    return [bytes(response_body, encoding="utf8")]


if __name__ == "__main__":
    # Instantiate the WSGI server.
    # It will receive the request, pass it to the application
    # and send the application's response to the client
    httpd = make_server(
        'localhost',  # The host name.
        8080,  # A port number where to wait for the request.
        application,  # Our application object name, in this case a function.
    )

    # Wait for a single request, serve it and quit.
    # httpd.handle_request()

    # Keep the server always alive with serve_forever()
    httpd.serve_forever()
