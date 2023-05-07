from cgitb import reset


def convert_sec(seconds):
        hrs=seconds//3600
        mins=(seconds-hrs*3600)//60
        rem_secs=seconds-(hrs*3600)-(mins*60)
        return hrs,mins,rem_secs
result=convert_sec(5000)
print(result)
print(type(result))
hours,minutes,seconds=convert_sec(9000000)
print(hours,minutes,seconds)