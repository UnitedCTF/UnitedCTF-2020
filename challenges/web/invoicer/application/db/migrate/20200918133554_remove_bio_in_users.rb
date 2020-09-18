class RemoveBioInUsers < ActiveRecord::Migration[6.0]
  def change
    remove_column :users, :bio, type: :text, null: true
  end
end
