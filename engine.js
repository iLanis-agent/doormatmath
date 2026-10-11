(function (root) {
  "use strict";
  function r0(x) { return Math.round(x); }
  function r1(x) { return Math.round(x * 10) / 10; }
  function r2(x) { return Math.round(x * 100) / 100; }
  function plural(n, word) { return n + " " + word + (n === 1 ? "" : "s"); }

  function sizePlan(doorWCm, extraCm, strideCm) {
    if (!(doorWCm > 0) || !(extraCm >= 0) || !(strideCm > 0)) return { error: "door and stride must be positive, extra zero or more" };
    var widthCm = r0(doorWCm + 2 * extraCm);
    var depthCm = r0(2 * strideCm);
    return { widthCm: widthCm, depthCm: depthCm };
  }

  function gritPlan(stepsPerVisit, visitsPerDay, gPerStep) {
    if (!(stepsPerVisit > 0) || !(visitsPerDay > 0) || !(gPerStep > 0)) return { error: "steps, visits and grit must be positive" };
    var gDay = r1(stepsPerVisit * visitsPerDay * gPerStep);
    var kgYear = r2(stepsPerVisit * visitsPerDay * gPerStep * 365 / 1000);
    return { gDay: gDay, kgYear: kgYear };
  }

  function dryPlan(matLCm, matWCm, mlPerM2, evapMlHour) {
    if (!(matLCm > 0) || !(matWCm > 0) || !(mlPerM2 > 0) || !(evapMlHour > 0)) return { error: "mat, soak and evaporation must be positive" };
    var areaM2 = r2(matLCm * matWCm / 10000);
    var wetMl = r0(matLCm * matWCm / 10000 * mlPerM2);
    var hours = r1(matLCm * matWCm / 10000 * mlPerM2 / evapMlHour);
    return { areaM2: areaM2, wetMl: wetMl, hours: hours };
  }

  function renderSize(r, doorW, extra, stride) {
    return "A " + doorW + " cm door with a labeled " + extra + " cm extra a side and two " + stride + " cm strides wants a mat about " + r.widthCm + " x " + r.depthCm + " cm.";
  }

  function renderGrit(r, stepsPerVisit, visitsPerDay, gPerStep) {
    return plural(stepsPerVisit, "step") + " a visit, " + plural(visitsPerDay, "visit") + " a day, at a labeled " + gPerStep + " g a step is " + r.gDay + " g of grit a day - " + r.kgYear + " kg a year stopped at the door.";
  }

  function renderDry(r, evapMlHour) {
    return "That mat holds about " + r.wetMl + " ml of rain at a labeled soak - about " + r.hours + " hours to dry at a labeled " + evapMlHour + " ml an hour.";
  }

  var api = { sizePlan: sizePlan, gritPlan: gritPlan, dryPlan: dryPlan, renderSize: renderSize, renderGrit: renderGrit, renderDry: renderDry };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.DoormatMath = api;
})(this);
