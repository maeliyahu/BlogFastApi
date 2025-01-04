import debugpy
import os

def enable_debug(wait=False):
    if os.getenv("ENV", "production") == "development":
        port_for_debug = os.getenv("DEBUG_PORT", 5678)
        debugpy.listen(('0.0.0.0', port_for_debug ))
        if wait:
            debugpy.wait_for_client()
            debugpy.breakpoint()
