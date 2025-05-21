import platform

def get_system_info():
    return {
        'system': platform.system(),
        'version': platform.version(),
        'machine': platform.machine(),
    }

