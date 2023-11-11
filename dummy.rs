use std::io;
fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let num: i32 =  input.trim()
                    .parse()
                    .expect("Please enter a valid integer");
    println!("{}", num);

    dummy(num);
}


fn dummy(x:i32){
    println!("{}",x^2);
}