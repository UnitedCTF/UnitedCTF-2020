class User < ApplicationRecord
  has_secure_password

  has_many :invoices

  validates :name, presence: true
  validates :name, length: { maximum: 255 }
  validates :name, uniqueness: { case_sensitive: false }
  validates :demo, inclusion: { in: [true, false] }
  validates :email, presence: true
  validates :email, length: { maximum: 255 }
  validates :email, format: { with: /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]{2,})\z/i }
  validates :email, uniqueness: { case_sensitive: false }
  validates(
    :password,
    length: { minimum: 12 },
    password_strength: { use_dictionary: true, min_word_length: 6, min_entropy: 18 },
    on: :create
  )
  validates(
    :password, 
    length: { minimum: 12 }, 
    password_strength: { use_dictionary: true, min_word_length: 6, min_entropy: 18 },
    on: :update, 
    if: -> { password.present? }
  )
  

  before_save do
    self.email = email.downcase if attribute_present?('email')
  end

  def send_password_reset
    assign_secure_token(:password_reset_token, 4)
    self.password_reset_generated_at = Time.zone.now
    save!
    # TODO: Send email.
  end

  def admin?
    id == 1
  end

  private

  def assign_secure_token(column, length)
    attempt = 0
    maximum_attempt = 10
    while attempt < maximum_attempt
      self[column] = length.times.map { rand(0..9) }.join('')
      return unless User.exists?(column => self[column])

      attempt += 1
    end

    raise StandardError, "Could not generate #{column} after #{maximum_attempt} attempts."
  end

  def verify_strong_password
    if password
    end
  end
end
