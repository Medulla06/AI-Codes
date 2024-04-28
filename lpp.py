import pytholog as pl

kb = pl.KnowledgeBase("facts")

kb(["likes(Shyam,mango)",
    "girl(Seema)",
    "likes(Bill,Cindy)",
    "red(Rose)",
    "owns(John,Gold)"])

what = "mango"

print("? - likes(Shyam,what)")
print(kb.query(pl.Expr("likes(Shyam, " + str(what) + ")")))
