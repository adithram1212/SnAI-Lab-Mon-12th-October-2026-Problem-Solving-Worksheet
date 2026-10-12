with open ("mylogs.txt",'r') as f:
    for i in f:
        if "error" in i:
            with open ("error.log", 'a') as l:
                l.write(i)
        elif "info" in i:
            with open ("info.log",'a') as k:
                k.write(i)