define_agents = {"name": "alpha",
"level": 3,
"active": True}
print(define_agents)
print(define_agents["name"])
getting = define_agents.get("level")
print(getting)
define_agents["score"]=95
print(define_agents)
define_agents["level"] = 5
print(define_agents)
define_agents.pop("active")
print(define_agents)
print("name" ,"level" ,"score")
print(define_agents["name"], define_agents["level"], define_agents["score"] )
print("score" in define_agents)
define_scores = {"alpha": 80,
"bravo": 95, "charlie": 70}
max_num = max(define_scores, key=define_scores.get)
print(max_num)
print(define_scores)
copy_define_scores = define_scores.copy()
print(copy_define_scores)
copy_define_scores["alpha"] = 75
print(copy_define_scores)