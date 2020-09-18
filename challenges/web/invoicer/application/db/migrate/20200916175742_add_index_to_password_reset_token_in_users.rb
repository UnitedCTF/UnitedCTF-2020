class AddIndexToPasswordResetTokenInUsers < ActiveRecord::Migration[6.0]
  def change
    add_index :users, :password_reset_token, unique: true
  end
end
