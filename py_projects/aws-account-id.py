# Homework
# Write a program will display the account id from the arn below:
# arn:aws:iam::123456789012:user/Development/product_1234/*
# Display on the screen: the aws account id is: account_id.


# Solution

# Extraction of AWS account ID from an ARN

# Defining the ARN string
arn = "arn:aws:iam::123456789012:user/Development/product_1234/*"

# Spliting the ARN string by ':' to isolate the account ID
arn_parts = arn.split(':')

# The AWS account ID is in the 5th position (index 4)
account_id = arn_parts[4]

# Display the AWS account ID
print(f"The AWS account ID is: {account_id}")
