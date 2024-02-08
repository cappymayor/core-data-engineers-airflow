resource "aws_s3_bucket" "example" {
  bucket = "faker-raw-data"

  tags = {
    Team        = "Core Data Engineers"
    Manage_by_terraform = "True"
    service = "Airflow"
  }
}