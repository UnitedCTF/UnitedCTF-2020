class SuperHiddenSecretFeature < ApplicationRecord
  validates :name, presence: true
  validates :hidden, inclusion: { in: [true, false] }
end
