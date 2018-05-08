
def is_inside([float(x),float(y)],[float(x1),float(y1),float(w),float(h)]):
    s=w*h
    s1=1/2*h*(abs(abs(x)-abs(x1))+abs(abs(x)-abs(abs(x1)+w)))+1/2*w*(abs(abs(y)-abs(abs(y1)+h))+abs(abs(abs(y)-abs(y1))))
    if s<s1:
        print("False")
    else:
        print("True")
    return is_inside
n=is_inside([100, 120], [140, 60, 100, 200])
print(n)
