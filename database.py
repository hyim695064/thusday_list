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