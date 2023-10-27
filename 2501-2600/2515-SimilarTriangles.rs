// Problem: https://yukicoder.me/problems/no/2515
// Submission: https://yukicoder.me/submissions/923987

use std::io;

fn main(){

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let values: Vec<i32> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let _x1 = values[0];
    let y1 = values[1];
    let _x2 = values[2];
    let y2 = values[3];
    let _x3 = values[4];

    let ans: &str;

    if y1==y2 {
        ans = "Yes";
    }

    else{
        ans = "No";
    }

    println!("{}", ans);
}