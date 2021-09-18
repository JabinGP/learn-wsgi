from werkzeug.local import(
    Local,
    LocalManager,
    LocalProxy,
    LocalStack,
)

l = Local()
l.user = {"id": 1}

print("l.user = %s" % l.user)

user = l.user
print("user = %s" % user)
user_proxy = LocalProxy(l, "user")
print("user_proxy = %s" % user_proxy)
l.user = {"ident": 199}
print("user_proxy = %s" % user_proxy)
print("user = %s" % user)
