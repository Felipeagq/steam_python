personas = {"felipe":[
    
    {"libro":"habitos atomicos",
    "fecha":"2023-02-14",
    "estado":"prestado"},
    
    {"libro":"Club 5 am",
    "fecha":"2023-02-14",
    "estado":"devuelto"},
],
"gabriela":[
    
    {"libro":"li¿broia",
    "fecha":"2023-02-14",
    "estado":"prestado"},
    
    {"libro":"b",
    "fecha":"2023-02-14",
    "estado":"devuelto"},
]}


print(personas.get("felipe",{"ESTADO":"No encontrado"}))