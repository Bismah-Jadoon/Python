def http_status(status):
    match(status):
        case 200:
            return "OK"
        case 404:
            return "Page not found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown"
        
print(http_status(404))