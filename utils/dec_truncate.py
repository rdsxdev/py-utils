def truncate(num):
    n = int(input("Enter the number of decimal places to truncate to: "))
    s = str(num)
    if "." in s:
        whole, decimal = s.split(".")
        return whole + "." + decimal[:n]
    return s