def comparison(x,y,z):
    if x<y:
        if y<z:
            second = y
        else:
            if x<z:
                second = z
            else:
                second = x
    elif x<z:
        second = x
    else:
        print(-1)

    if x<=0 or y<=0 or z<=0:
        return -1
    if x*y*z == second*second*second:
        return "true"
    else:
        return "false"
