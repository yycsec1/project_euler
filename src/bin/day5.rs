fn main() {
    let mut n = 0;
    let mut not_found = true;
    while not_found {
        n += 20;
        for i in 2..=20 {
            if n % i != 0 {
                not_found = true;
                break;
            }
            not_found = false;
        }
    }
    println!("{}", n)
}