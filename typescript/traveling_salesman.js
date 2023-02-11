var __read = (this && this.__read) || function (o, n) {
    var m = typeof Symbol === "function" && o[Symbol.iterator];
    if (!m) return o;
    var i = m.call(o), r, ar = [], e;
    try {
        while ((n === void 0 || n-- > 0) && !(r = i.next()).done) ar.push(r.value);
    }
    catch (error) { e = { error: error }; }
    finally {
        try {
            if (r && !r.done && (m = i["return"])) m.call(i);
        }
        finally { if (e) throw e.error; }
    }
    return ar;
};
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
var __values = (this && this.__values) || function(o) {
    var s = typeof Symbol === "function" && Symbol.iterator, m = s && o[s], i = 0;
    if (m) return m.call(o);
    if (o && typeof o.length === "number") return {
        next: function () {
            if (o && i >= o.length) o = void 0;
            return { value: o && o[i++], done: !o };
        }
    };
    throw new TypeError(s ? "Object is not iterable." : "Symbol.iterator is not defined.");
};
function distance(p1, p2) {
    return Math.sqrt(Math.pow((p1.x - p2.x), 2) + Math.pow((p1.y - p2.y), 2));
}
function travelingSalesman(points) {
    var n = points.length;
    var min = Number.MAX_VALUE;
    function visit(path, remaining) {
        var e_1, _a;
        if (remaining.length === 0) {
            var d = 0;
            for (var i = 0; i < n - 1; i++) {
                d += distance(points[path[i]], points[path[i + 1]]);
            }
            d += distance(points[path[n - 1]], points[path[0]]);
            min = Math.min(min, d);
        }
        else {
            var _loop_1 = function (i) {
                var nextRemaining = remaining.filter(function (j) { return j !== i; });
                visit(__spreadArray(__spreadArray([], __read(path), false), [i], false), nextRemaining);
            };
            try {
                for (var remaining_1 = __values(remaining), remaining_1_1 = remaining_1.next(); !remaining_1_1.done; remaining_1_1 = remaining_1.next()) {
                    var i = remaining_1_1.value;
                    _loop_1(i);
                }
            }
            catch (e_1_1) { e_1 = { error: e_1_1 }; }
            finally {
                try {
                    if (remaining_1_1 && !remaining_1_1.done && (_a = remaining_1["return"])) _a.call(remaining_1);
                }
                finally { if (e_1) throw e_1.error; }
            }
        }
    }
    visit([0], __spreadArray([], __read(Array(n).keys()), false).slice(1));
    return min;
}
var cities = [
    { name: 'A', x: 0, y: 0 },
    { name: 'B', x: 1, y: 1 },
    { name: 'C', x: 2, y: 2 },
    { name: 'D', x: 3, y: 3 },
];
var result = travelingSalesman(cities);
console.log(result);
result = travelingSalesman([]);
console.log(result);
result = travelingSalesman([cities[0]]);
console.log(result);
