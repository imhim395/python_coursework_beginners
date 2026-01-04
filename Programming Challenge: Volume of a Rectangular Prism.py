l=int(input("enter length in feet: "))
w=int(input("enter width in feet: "))
h=int(input("enter height in feet: "))


def volume_calculater(l, w, h):
    return l * w * h
print("the volume of the rectangular prism is " + str(volume_calculater (l, w, h)) + " cubic feet")