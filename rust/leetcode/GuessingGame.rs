use rand::Rng;

fn main() {
    
    let mut rng = rand::thread_rng();
    println!("Integer: {}", rng.gen_range(0..10));
    // println!("Float: {}", rng.gen_range(0.0..10.0));
    
    let (mut lo, mut hi) = (1,3);
    println!("{},{}",lo,hi);


    let (mut lo, mut hi) = (1, n);
        let mut pick = lo + ((hi-lo) / 2);
        // println!("Integer: {}", rng.gen_range(1..n+1));
        loop {
            if 0 == guess(pick)
            {
                return pick
            }
            if 1 == guess(pick)
            {
                lo = pick+1;
            }
            else
            {
                hi = pick-1;
            }
            pick = lo + ((hi-lo) / 2);
        }


        /*
         match statement solution

       let (mut lo, mut hi) = (1, n);
        loop {
            
            let pick = lo + ((hi-lo) / 2);
            match guess(pick)
            {
                1 => lo = pick+1,
                -1 => hi = pick-1,
                _ => break pick
            }
        }  
         
         */
}






































