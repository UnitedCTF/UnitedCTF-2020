class CreateSuperHiddenSecretFeatures < ActiveRecord::Migration[6.0]
  def change
    create_table :super_hidden_secret_features do |t|
      t.string :name, null: false
      t.boolean :hidden, null: false, default: true

      t.timestamps
    end
  end
end
