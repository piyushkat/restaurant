def pagination(OFFSET,LIMIT,counter):
    if LIMIT > 100:
        LIMIT = 100 
    if counter == 0:
        OFFSET = OFFSET-LIMIT
        if OFFSET<=0:
            OFFSET = 0
    else:
        OFFSET = OFFSET+LIMIT
    return OFFSET,LIMIT
