
def long_loop():
    import ipdb;ipdb.set_trace()
    for i in range(int(1e04)):
        i+1
    result = 1 + 1
    return result

print long_loop()
        
