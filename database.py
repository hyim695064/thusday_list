define_agents = {"name": "alpha",
"level": 3,
"active": True}
print(define_agents)
print(define_agents["name"])
getting = define_agents.get("level")
#הגט נותן לי להדפיס את מה שיש בתוך המפתח בלי לקבל שגיאה
print(getting)
define_agents["score"]=95
print(define_agents)
define_agents["level"] = 5
print(define_agents)
define_agents.pop("active")
#זה מוחק לי את המפתח שביקשתי
print(define_agents)
#זה נותן רק את המפתחות עצמם
print("name" ,"level" ,"score")
#זה נותן את החלק השני של המפתח
print(define_agents["name"], define_agents["level"], define_agents["score"] )
#מראה אם יש כזה ערך או לא על ידי בוליין
print("score" in define_agents)
define_scores = {"alpha": 80,
"bravo": 95, "charlie": 70}
max_num = max(define_scores, key=define_scores.get)
print(max_num)
#בגלל הגט זה מדפיס את הערך של המפתח הכי גדול
print(define_scores)
copy_define_scores = define_scores.copy()
print(copy_define_scores)
copy_define_scores["alpha"] = 75
#זה מדפיס את הקופי עם השינוי 
print(copy_define_scores)

config = {}
config.setdefault("timeout", 30,)
#עשיתי רשימה חדשה ריקה והכנסתי לתוכה זוג
print(config)
config.setdefault("timeout", 50)
#ניסיון לשנות את הערך שהכנסתי ראשון
print(config)
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1|d2
print(d1|d2)