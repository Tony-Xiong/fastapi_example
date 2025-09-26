from fastapi import FastAPI
from .routers import *
app = FastAPI()

app.include_router(router)
app.include_router(user_router)
# print("okk")
# ls = locals().copy()
# for key in ls.keys():
#     if key.find("router") != -1:
#         print(f"include {key} router.")
#         app.include_router(ls.get(key))
