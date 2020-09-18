class ChangeDefaultValueForDemoInUsers < ActiveRecord::Migration[6.0]
  def change
    change_column_default :users, :demo, from: false, to: true
  end
end
