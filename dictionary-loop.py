import json

y = {
  "a" : {
  	"b" : {
    	"c" : "d"
    }
  } 
}

print(type(y))



def loop_d(x):
    for k,v in x.items():
        if isinstance(v, dict):
            #print(isinstance(v, dict))
            loop_d(v)
        else:
            print(v)

loop_d(y)
