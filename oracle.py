import json, math

def r0(x): return math.floor(x + 0.5)
def r1(x): return math.floor(x * 10 + 0.5) / 10
def r2(x): return math.floor(x * 100 + 0.5) / 100
def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word): return str(n) + " " + word + ("" if n == 1 else "s")
def fmt(x): return str(jsnum(x))

def size_plan(doorW, extra, stride):
    if not (doorW > 0) or not (extra >= 0) or not (stride > 0):
        return {"error": "door and stride must be positive, extra zero or more"}
    return {"widthCm": r0(doorW + 2 * extra), "depthCm": r0(2 * stride)}

def grit_plan(stepsPerVisit, visitsPerDay, gPerStep):
    if not (stepsPerVisit > 0) or not (visitsPerDay > 0) or not (gPerStep > 0):
        return {"error": "steps, visits and grit must be positive"}
    gDay = r1(stepsPerVisit * visitsPerDay * gPerStep)
    kgYear = r2(stepsPerVisit * visitsPerDay * gPerStep * 365 / 1000)
    return {"gDay": jsnum(gDay), "kgYear": jsnum(kgYear)}

def dry_plan(matL, matW, mlPerM2, evapMlHour):
    if not (matL > 0) or not (matW > 0) or not (mlPerM2 > 0) or not (evapMlHour > 0):
        return {"error": "mat, soak and evaporation must be positive"}
    areaM2 = r2(matL * matW / 10000)
    wetMl = r0(matL * matW / 10000 * mlPerM2)
    hours = r1(matL * matW / 10000 * mlPerM2 / evapMlHour)
    return {"areaM2": jsnum(areaM2), "wetMl": wetMl, "hours": jsnum(hours)}

def render_size(r, doorW, extra, stride):
    return ("A " + fmt(doorW) + " cm door with a labeled " + fmt(extra) + " cm extra a side and two "
            + fmt(stride) + " cm strides wants a mat about " + str(r["widthCm"]) + " x " + str(r["depthCm"]) + " cm.")

def render_grit(r, stepsPerVisit, visitsPerDay, gPerStep):
    return (plural(stepsPerVisit, "step") + " a visit, " + plural(visitsPerDay, "visit")
            + " a day, at a labeled " + fmt(gPerStep) + " g a step is " + fmt(r["gDay"])
            + " g of grit a day - " + fmt(r["kgYear"]) + " kg a year stopped at the door.")

def render_dry(r, evapMlHour):
    return ("That mat holds about " + fmt(r["wetMl"]) + " ml of rain at a labeled soak - about "
            + fmt(r["hours"]) + " hours to dry at a labeled " + fmt(evapMlHour) + " ml an hour.")

cases = []
for doorW, extra, stride in [(90, 10, 65), (80, 15, 70), (100, 5, 60), (0, 10, 65), (90, 10, 0)]:
    r = size_plan(doorW, extra, stride)
    cases.append({"fn": "sizePlan", "args": [doorW, extra, stride], "result": r,
                  "render": None if "error" in r else render_size(r, doorW, extra, stride)})
for stepsPerVisit, visitsPerDay, gPerStep in [(4, 3, 0.4), (6, 2, 0.5), (2, 5, 0.3), (1, 1, 0.4), (0, 3, 0.4)]:
    r = grit_plan(stepsPerVisit, visitsPerDay, gPerStep)
    cases.append({"fn": "gritPlan", "args": [stepsPerVisit, visitsPerDay, gPerStep], "result": r,
                  "render": None if "error" in r else render_grit(r, stepsPerVisit, visitsPerDay, gPerStep)})
for matL, matW, mlPerM2, evapMlHour in [(110, 130, 1000, 100), (80, 50, 1200, 80), (60, 40, 800, 120), (0, 130, 1000, 100)]:
    r = dry_plan(matL, matW, mlPerM2, evapMlHour)
    cases.append({"fn": "dryPlan", "args": [matL, matW, mlPerM2, evapMlHour], "result": r,
                  "render": None if "error" in r else render_dry(r, evapMlHour)})

with open("expected.json", "w") as f:
    f.write(json.dumps(cases, separators=(",", ":")) + "\n")
print("wrote", len(cases), "cases")
