require 'securerandom'

class Invoice < ApplicationRecord
  belongs_to :user

  validates :user, presence: true
  validates :amount, numericality: { greater_than: 0 }
  validates :details, presence: true
  validates :details, length: { maximum: 255 }
  validates :recipient_email, presence: true
  validates :recipient_email, length: { maximum: 255 }
  validates :recipient_email, format: { with: /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]{2,})\z/i }
  validates :recipient_name, presence: true
  validates :recipient_name, length: { maximum: 255 }

  before_create do
    assign_secure_token(:public_token, 34)
  end

  private

  def assign_secure_token(column, length)
    attempt = 0
    maximum_attempt = 10
    while attempt < maximum_attempt
      self[column] = SecureRandom.hex(length / 2)
      return unless Invoice.exists?(column => self[column])

      attempt += 1
    end

    raise StandardError, "Could not generate #{column} after #{maximum_attempt} attempts."
  end
end
