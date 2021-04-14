#![allow(unused)]
fn main()
{
    let s: &str = "a";
    let ss: String = s.to_owned();

    let v = &mut vec![1, 2];
    let mut vv: Vec<i32> = v.to_owned();

    vv[1] = 100;
    println!("vv: {:?}",vv);
    println!("v: {:?}",v);

}