use chrono::NaiveDate;

fn main() {
    println!("Hello, world!");
}

fn count_days(date1: &NaiveDate, date2: &NaiveDate) -> i64 {
    let duration = date1.signed_duration_since(*date2);
    duration.num_days()
}

#[test]
fn test_count_days() {
    let date1 = NaiveDate::from_ymd_opt(2023, 6, 28).unwrap();
    let date2 = NaiveDate::from_ymd_opt(2023, 6, 17).unwrap();
    assert_eq!(count_days(&date1, &date2), 11);
}
