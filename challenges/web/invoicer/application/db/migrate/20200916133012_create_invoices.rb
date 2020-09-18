class CreateInvoices < ActiveRecord::Migration[6.0]
  def change
    create_table :invoices do |t|
      t.integer :amount, null: false
      t.string :details, null: false
      t.string :recipient_email, null: false
      t.string :recipient_name, null: false
      t.string :public_token, null: false
      t.references :user, null: false, foreign_key: true

      t.timestamps
    end

    add_index :invoices, :public_token, unique: true
  end
end
