d={
    1:{
        'A':{1:"A"},
        2:"B"
       },
   3:"C",
   'B':"D",
   "D":'E'}
print(d[d[d[1][2]]],end="")
print(d[d[1]["A"][2]])



d={1:1,2:'2','1':'2',3:3}
d['1']=2
print(d[d[d[str(d[1])]]])