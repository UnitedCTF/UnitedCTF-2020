# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

user_attributes = {
  id: 1,
  name: ENV['SUPPORT_ACCOUNT_NAME'],
  email: "support@invoicer.com",
  demo: true
}
user = User.find_or_create_by!(user_attributes) do |new_user|
  password = SecureRandom.hex
  puts "Support account (support@invoicer.com) password: #{password}"
  new_user.password = password
  new_user.password_confirmation = password
end

invoice = Invoice.find_or_create_by!(
  user: user,
  amount: 69,
  details: "Awesome product",
  recipient_name: user.name,
  recipient_email: user.email
)

invoice = Invoice.find_or_create_by!(
  user: user,
  amount: 420,
  details: "Blaze product",
  recipient_name: user.name,
  recipient_email: user.email
)

invoice = Invoice.find_or_create_by!(
  user: user,
  amount: 9_000,
  details: "This is a flag (maybe not)",
  recipient_name: user.name,
  recipient_email: user.email
)

SuperHiddenSecretFeature.find_or_create_by!(
  name: ENV['FLAG_3']
)
