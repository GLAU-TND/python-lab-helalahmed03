try:
    a=input()
    a.reverse()
except (AttributeError):
    print("not a valid attrbt")
except (ValueError):
    print("not a valid value")
except (TypeError):
    print("not a valid type")

    
    
