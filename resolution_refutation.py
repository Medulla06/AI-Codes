import pytholog as pl

kb = pl.KnowledgeBase("rr")

kb(["child(x) :- loves(x,santa)",
    "loves(x,santa) :- reindeer(y), loves(x,y)",
    "reindeer(rudolph)", "redNose(rudolph)" ,
    "redNose(x):-weird(x)","redNose(x):-clown(x)",
    "not(reindeer(x)):-clown(x)",
    "weird(x):- not(loves(scrooge,x))"])
    
print("Is scrooge a child?")    
result = kb.query(pl.Expr("not(child(scrooge))"))
print(result)
