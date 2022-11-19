use std::cmp::{min, max};

impl Solution {
    pub fn compute_area(ax1: i32, ay1: i32, ax2: i32, ay2: i32, bx1: i32, by1: i32, bx2: i32, by2: i32) -> i32
    {
        // plan:
        // get area of both rectangles and subtract the area of the overlap
        let (length1, width1) = (ay2-ay1,ax2-ax1);
        let (length2, width2) = (by2-by1,bx2-bx1);

        let area1 = length1 * width1;rust using namespace to avoid typing namespace
        let area2 = length2 * width2;

        let overlapArea = max(min(ay2,by2)-max(ay1,by1),0) * max(min(ax2,bx2)-max(ax1,bx1),0);

        area1 + area2 - overlapArea

    }
}
