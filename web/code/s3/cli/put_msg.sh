echo "hello world!" >> example.txt
aws s3api put-object --key "example.txt" --bucket ts-first-bucket