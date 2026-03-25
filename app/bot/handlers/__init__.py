from .start import router as start_router

routers = [
    start_router
]

def register_routers(dp):
    for router in routers:
        dp.include_router(router)