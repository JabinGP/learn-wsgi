from werkzeug.local import(
    Local,
    LocalManager,
    LocalProxy,
    LocalStack,
)

l = Local()
l.user = {"id": 1}

print(f"l.user = %s"%l.user)

user = l.user
print(f"user = %s"%user)
user_proxy = LocalProxy(l, "user")
print(f"user_proxy = %s"%user_proxy)
l.user = {"ident": 199}
print(f"user_proxy = %s"%user_proxy)
print(f"user = %s"%user)
