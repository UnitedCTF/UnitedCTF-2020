class CreateUsers < ActiveRecord::Migration[6.0]
  def change
    create_table :users do |t|
      t.string :name, null: false
      t.string :email, null: false
      t.text :bio, null: true
      t.string :password_digest, null: false
      t.string :reset_password_token, null: true
      t.datetime :reset_password_generated_at, null: true
      t.boolean :demo, null: false, default: false

      t.timestamps
    end

    add_index :users, :email, unique: true
  end
end
