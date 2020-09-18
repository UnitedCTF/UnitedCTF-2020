class RenameResetPasswordToPasswordResetInUsers < ActiveRecord::Migration[6.0]
  def change
    rename_column :users, :reset_password_token, :password_reset_token
    rename_column :users, :reset_password_generated_at, :password_reset_generated_at
  end
end
